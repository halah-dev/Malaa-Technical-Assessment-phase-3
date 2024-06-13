from api.controllers.market_controllers import router as MarketRouter
from api.controllers.rules_controller import router as RulesRouter
from api.controllers.alerts_controller import router as AlertsRouter


def init_routes(app):
    app.include_router(MarketRouter, prefix="/market-prices", tags=["Market"])
    app.include_router(RulesRouter, prefix="/alert-rules", tags=["Rules"])
    app.include_router(AlertsRouter, prefix="/alerts", tags=["Alerts"])
    return app
