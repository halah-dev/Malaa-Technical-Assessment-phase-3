from celery import Celery
from celery.schedules import crontab
import os

from core.messaging import Publisher
from resources.alert_rules.alert_rule_service import get_rules_service
from resources.market.market_service import get_market_data
from db.models.models import session


def create_celery_app():
    app = Celery(
        "tasks",
        broker=f"pyamqp://{os.getenv('RMQ-USER')}:{os.getenv('RMQ-PASS')}@{os.getenv('RMQ-HOST')}:{os.getenv('RMQ-PORT')}//",
    )
    app.conf.update(
        beat_schedule={
            "run-every-5-minutes": {
                "task": "tasks.check_market_data",
                "schedule": crontab(minute="*/5"),
            },
        }
    ),
    return app


celery_app = create_celery_app()


@celery_app.task(name="tasks.check_market_data")
def check_market_data_and_rules():
    rules = get_rules_service(session=session)

    alerts = []
    for rule in rules:
        symbol = rule.symbol
        threshold_price = rule.threshold_price
        market_data = get_market_data(symbol)
        if float(market_data["price"]) < threshold_price:
            alert_message = f"Alert: {symbol} has fallen below {threshold_price}"
            alerts.append(alert_message)

            # Publish THRESHOLD_ALERT event
            event = {
                "message": alert_message,
                "name": "Price Dropped",
                "threshold_price": threshold_price,
                "symbol": symbol,
            }

            publisher = Publisher()
            publisher.publish(os.getenv("RMQ-ROUTING-KEY"), event)

    return alerts
