from resources.market.market_service import get_market_data
from resources.alert_rules.alert_rule_service import get_rules_service
from db.models.models import session
from core.messaging import send_message
from worker.app import app
import json


@app.task
def fetch_data_and_check_rules():
    rules = get_rules_service(session)
    for rule in rules:
        print(f"Fetching data for {rule.symbol}...")
        market = get_market_data([rule.symbol])
        if (
            market["symbol"] == rule.symbol
            and float(market["price"]) >= float(rule.threshold_price)
        ):
            publish_threshold_alert(rule.symbol)


def publish_threshold_alert(rule):
    # Publish a message
    print(f"Publishing threshold alert for {rule}...")
    message_body = {"eventName": "THRESHOLD_ALERT", "eventData": {"symbol": [rule]}}
    print(f"Published threshold alert for {rule} successfully!")
    send_message(message_body)
