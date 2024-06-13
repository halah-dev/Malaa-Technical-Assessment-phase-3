from fastapi import APIRouter
from db.models.models import session
from resources.market.market_service import get_market_data
from resources.common.error_schema import MessageData

# from resources.alert_rules.alert_rule_schema import AlertData
from fastapi.responses import JSONResponse

from resources.alerts.alert_service import (
    get_alerts_service,
)
from resources.alert_rules.alert_rule_schema import (
    AlertRuleCreate,
)

router = APIRouter()


@router.get(
    "/",
    # response_model=MessageData,
    summary="Get Alerts",
    description="Returns all alerts",
)
async def get_alert():
    response = get_alerts_service(session=session)

    return response
