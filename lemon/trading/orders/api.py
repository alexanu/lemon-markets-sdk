from datetime import datetime
from typing import Optional

from lemon.helpers import ApiClient
from lemon.trading.orders.models import (
    GetOrdersResponse,
    OrderSide,
    OrderStatus,
    OrderType,
)


class Orders:
    def __init__(self, client: ApiClient):
        self._client = client

    def get(
        self,
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        isin: Optional[str] = None,
        side: Optional[OrderSide] = None,
        status: Optional[OrderStatus] = None,
        type: Optional[OrderType] = None,
        key_creation_id: Optional[str] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> GetOrdersResponse:
        resp = self._client.get(
            "/orders",
            query_params={
                "from": from_,
                "to": to,
                "isin": isin,
                "side": side,
                "status": status,
                "type": type,
                "key_creation_id": key_creation_id,
                "limit": limit,
                "page": page,
            },
        )
        return GetOrdersResponse._from_data(resp.json())
