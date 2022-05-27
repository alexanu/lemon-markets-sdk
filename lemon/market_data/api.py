from lemon.config import Config
from lemon.helpers import ApiClient
from lemon.market_data.instruments.api import Instruments
from lemon.market_data.ohlc.api import Ohlc
from lemon.market_data.quotes.api import Quotes
from lemon.market_data.trades.api import Trades
from lemon.market_data.venues.api import Venues


class MarketDataApi:
    def __init__(self, config: Config):
        self._config = config

    @property
    def venues(self) -> Venues:
        return Venues(ApiClient(self._config.market_data_api_url, self._config))

    @property
    def instruments(self) -> Instruments:
        return Instruments(ApiClient(self._config.market_data_api_url, self._config))

    @property
    def trades(self) -> Trades:
        return Trades(ApiClient(self._config.market_data_api_url, self._config))

    @property
    def quotes(self) -> Quotes:
        return Quotes(ApiClient(self._config.market_data_api_url, self._config))

    @property
    def ohlc(self) -> Ohlc:
        return Ohlc(ApiClient(self._config.market_data_api_url, self._config))
