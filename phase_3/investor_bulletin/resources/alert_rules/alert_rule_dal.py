""" Alert Rule  DAL"""

"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from db.models import AlertRule
from psycopg2.errors import InvalidTextRepresentation
from psycopg2.errors import InFailedSqlTransaction


def create_alert_rule(rule: AlertRuleCreate, session):
    data = AlertRule(
        name=rule.name, symbol=rule.symbol, threshold_price=rule.threshold_price
    )
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


def update_alert_rule(id: str, rule: AlertRuleCreate, session):

    try:
        update_rule = session.query(AlertRule).get(id)
    except Exception as e:
        session.rollback()
        return {
            "status": False,
            "message": "The requested ID is in the incorrect format",
        }

    if update_rule is None:
        return {
            "status": False,
            "message": "The requested ID {} was not found".format(id),
        }

    if rule.name:
        update_rule.name = rule.name
    if rule.threshold_price:
        update_rule.threshold_price = rule.threshold_price
    if rule.symbol:
        update_rule.symbol = rule.symbol

    session.commit()

    return {
        "status": True,
        "message": "Alert Rule with ID {} is successfully updated".format(id),
    }


def delete_alert_rule(id: str, session):

    try:
        delete_rule = session.query(AlertRule).get(id)
    except Exception as e:
        session.rollback()
        return {
            "status": False,
            "message": "The requested ID is in the incorrect format",
        }

    if delete_rule is None:
        return {
            "status": False,
            "message": "The requested ID {} was not found".format(id),
        }

    session.delete(delete_rule)
    session.commit()

    return {
        "status": True,
        "message": "Alert Rule with ID {} is successfully deleted".format(id),
    }


def get_alert_rules(session):
    return session.query(AlertRule).all()
