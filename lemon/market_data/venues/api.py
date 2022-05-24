from typing import List, Optional

from lemon.helpers import ApiClient, Sorting, encode_query_string
from lemon.market_data.venues.models import GetVenuesResponse


class Venues:
    def __init__(self, client: ApiClient):
        self._client = client

    def get(
        self,
        mic: Optional[List[str]] = None,
        sorting: Optional[Sorting] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> GetVenuesResponse:
        query_params = encode_query_string(
            mic=mic, sorting=sorting, limit=limit, page=page
        )
        resp = self._client.get(f"/venues?{query_params}")
        return GetVenuesResponse._from_data(resp.json())