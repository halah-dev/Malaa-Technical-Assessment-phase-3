""" Alert Rule Service"""

"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from resources.alert_rules.alert_rule_dal import (
    create_alert_rule,
    update_alert_rule,
    delete_alert_rule,
    get_alert_rules,
)


def create_new_rule_service(rule: AlertRuleCreate, session):
    return create_alert_rule(rule, session=session)


def update_rule_service(id: str, rule: AlertRuleCreate, session):
    return update_alert_rule(id, rule, session=session)


def delete_rule_service(id: str, session):
    return delete_alert_rule(id, session=session)


def get_rules_service(session):
    return get_alert_rules(session=session)
