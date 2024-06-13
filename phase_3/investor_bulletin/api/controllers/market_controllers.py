from fastapi import APIRouter
from resources.market.market_service import get_market_data
from resources.common.error_schema import MessageData
from resources.common.symbols_schema import Symbols
from resources.market.market_schema import MarketData
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get(
    "/",
    response_model=MarketData,
    responses={404: {"error": MessageData}},
    summary="Retrieve market data",
    description="Retrieve market data Required symbols/tickers AAPL,MSFT,GOOG,AMZN,META",
)
async def get_market_data_route(symbol: Symbols):
    response = get_market_data(symbol)

    if response["status"]:
        return response
    else:
        return JSONResponse(status_code=404, content=response)
