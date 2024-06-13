from fastapi import APIRouter
from db.models.models import session
from resources.market.market_service import get_market_data
from resources.common.error_schema import MessageData
from resources.alert_rules.alert_rule_schema import AlertRuleData
from fastapi.responses import JSONResponse

from resources.alert_rules.alert_rule_service import (
    create_new_rule_service,
    update_rule_service,
    delete_rule_service,
    get_rules_service,
)
from resources.alert_rules.alert_rule_schema import (
    AlertRuleCreate,
    # AlertRuleUpdate,
    # AlertRuleDelete,
)

router = APIRouter()


@router.post(
    "/",
    response_model=AlertRuleData,
    summary="Create Alert",
    description="Creates an alert rule with the following properties: name, threshold price, and symbol for the following symbols/tickers AAPL,MSFT,GOOG,AMZN,META",
)
async def create_new_alert(rule: AlertRuleCreate):
    response = create_new_rule_service(rule, session=session).to_dict()
    response["status"] = True

    return response


@router.patch(
    "/{id}",
    response_model=MessageData,
    responses={404: {"error": MessageData}},
    summary="Update Alert",
    description="Update an alert rule by ID with the following properties: name, threshold price, and symbol for the following symbols/tickers AAPL,MSFT,GOOG,AMZN,META",
)
async def update_alert(id: str, rule: AlertRuleCreate):
    response = update_rule_service(id, rule, session=session)

    if response["status"]:
        return response
    else:
        return JSONResponse(status_code=404, content=response)


@router.delete(
    "/{id}",
    response_model=MessageData,
    responses={404: {"error": MessageData}},
    summary="Delete Alert",
    description="Delete an alert rule by ID",
)
async def delete_alert(id: str):
    response = delete_rule_service(id, session=session)

    if response["status"]:
        return response
    else:
        return JSONResponse(status_code=404, content=response)


@router.get(
    "/",
    # response_model=MessageData,
    summary="Get Alert Rules",
    description="Returns all alert rules",
)
async def get_alert():
    response = get_rules_service(session=session)

    return response
