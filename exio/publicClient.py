#
#
# For public requests to the EXIO exchange

import requests


class PublicClient(object):
    """EXIO public client API.

    All requests default to the `product_id` specified at object
    creation if not otherwise specified.

    Attributes:
        url (Optional[str]): API URL. Defaults to EXIO API.

    """

    def __init__(self, api_url='https://api.sandbox.ex.io/v1', timeout=30):
        """Create EXIO API public client.

        Args:
            api_url (Optional[str]): API URL. Defaults to EXIO API.

        """
        self.url = api_url.rstrip('/')
        self.timeout = timeout

    def _get(self, path, params=None):
        """Perform get request"""

        r = requests.get(self.url + path, params=params, timeout=self.timeout)
        # r.raise_for_status()
        return r.json()

    def getProducts(self):
        """Get a list of available currency pairs for trading.

        Returns:
            list: Info about all currency pairs. Example::
                {
  "msg": "ok",
  "symbols": [
    {
      "name": "eth-btc",
      "description": "Ethereum / Bitcoin",
      "base": "eth",
      "base_min_tick": "0.01",
      "base_min_size": "0.1",
      "base_max_size": "100000",
      "quote": "btc",
      "quote_min_tick": "0.00001",
      "fees": "btc"
    },
    {
      "name": "eth-usdt",
      "description": "Ethereum / U.S Dollar Tether",
      "base": "eth",
      "base_min_tick": "0.01",
      "base_min_size": "0.1",
      "base_max_size": "100000",
      "quote": "usdt",
      "quote_min_tick": "0.1",
      "fees": "usdt"
    },
    {
      "name": "btc-usdt",
      "description": "Bitcoin / U.S Dollar Tether",
      "base": "btc",
      "base_min_tick": "0.0001",
      "base_min_size": "0.01",
      "base_max_size": "100000",
      "quote": "usdt",
      "quote_min_tick": "1",
      "fees": "usdt"
    }
  ]
}

        """
        return self._get('/symbols')

    # def get_product_order_book(self, product_id, level=1):
    #     """Get a list of open orders for a product.

    #     The amount of detail shown can be customized with the `level`
    #     parameter:
    #     * 1: Only the best bid and ask
    #     * 2: Top 50 bids and asks (aggregated)
    #     * 3: Full order book (non aggregated)

    #     Level 1 and Level 2 are recommended for polling. For the most
    #     up-to-date data, consider using the websocket stream.

    #     **Caution**: Level 3 is only recommended for users wishing to
    #     maintain a full real-time order book using the websocket
    #     stream. Abuse of Level 3 via polling will cause your access to
    #     be limited or blocked.

    #     Args:
    #         product_id (str): Product
    #         level (Optional[int]): Order book level (1, 2, or 3).
    #             Default is 1.

    #     Returns:
    #         dict: Order book. Example for level 1::
    #             {
    #                 "sequence": "3",
    #                 "bids": [
    #                     [ price, size, num-orders ],
    #                 ],
    #                 "asks": [
    #                     [ price, size, num-orders ],
    #                 ]
    #             }

    #     """

    #     # Supported levels are 1, 2 or 3
    #     level = level if level in range(1, 4) else 1
    #     return self._get('/products/{}/book'.format(str(product_id)), params={'level': level})

    # def get_product_ticker(self, product_id):
    #     """Snapshot about the last trade (tick), best bid/ask and 24h volume.

    #     **Caution**: Polling is discouraged in favor of connecting via
    #     the websocket stream and listening for match messages.

    #     Args:
    #         product_id (str): Product

    #     Returns:
    #         dict: Ticker info. Example::
    #             {
    #               "trade_id": 4729088,
    #               "price": "333.99",
    #               "size": "0.193",
    #               "bid": "333.98",
    #               "ask": "333.99",
    #               "volume": "5957.11914015",
    #               "time": "2015-11-14T20:46:03.511254Z"
    #             }

    #     """
    #     return self._get('/products/{}/ticker'.format(str(product_id)))

    # def get_product_trades(self, product_id, before='', after='', limit='', result=[]):
    #     """List the latest trades for a product.
    #     Args:
    #          product_id (str): Product
    #          before (Optional[str]): start time in ISO 8601
    #          after (Optional[str]): end time in ISO 8601
    #          limit (Optional[int]): the desired number of trades (can be more than 100,
    #                       automatically paginated)
    #          results (Optional[list]): list of results that is used for the pagination
    #     Returns:
    #          list: Latest trades. Example::
    #              [{
    #                  "time": "2014-11-07T22:19:28.578544Z",
    #                  "trade_id": 74,
    #                  "price": "10.00000000",
    #                  "size": "0.01000000",
    #                  "side": "buy"
    #              }, {
    #                  "time": "2014-11-07T01:08:43.642366Z",
    #                  "trade_id": 73,
    #                  "price": "100.00000000",
    #                  "size": "0.01000000",
    #                  "side": "sell"
    #      }]
    #     """
    #     url = self.url + '/products/{}/trades'.format(str(product_id))
    #     params = {}

    #     if before:
    #         params['before'] = str(before)
    #     if after:
    #         params['after'] = str(after)
    #     if limit and limit < 100:
    #         # the default limit is 100
    #         # we only add it if the limit is less than 100
    #         params['limit'] = limit

    #     r = requests.get(url, params=params)
    #     # r.raise_for_status()

    #     result.extend(r.json())

    #     if 'cb-after' in r.headers and limit is not len(result):
    #         # update limit
    #         limit -= len(result)
    #         if limit <= 0:
    #             return result

    #         # TODO: need a way to ensure that we don't get rate-limited/blocked
    #         # time.sleep(0.4)
    #         return self.get_product_trades(product_id=product_id, after=r.headers['cb-after'], limit=limit, result=result)

    #     return result

    # def get_product_historic_rates(self, product_id, start=None, end=None,
    #                                granularity=None):
    #     """Historic rates for a product.

    #     Rates are returned in grouped buckets based on requested
    #     `granularity`. If start, end, and granularity aren't provided,
    #     the exchange will assume some (currently unknown) default values.

    #     Historical rate data may be incomplete. No data is published for
    #     intervals where there are no ticks.

    #     **Caution**: Historical rates should not be polled frequently.
    #     If you need real-time information, use the trade and book
    #     endpoints along with the websocket feed.

    #     The maximum number of data points for a single request is 200
    #     candles. If your selection of start/end time and granularity
    #     will result in more than 200 data points, your request will be
    #     rejected. If you wish to retrieve fine granularity data over a
    #     larger time range, you will need to make multiple requests with
    #     new start/end ranges.

    #     Args:
    #         product_id (str): Product
    #         start (Optional[str]): Start time in ISO 8601
    #         end (Optional[str]): End time in ISO 8601
    #         granularity (Optional[str]): Desired time slice in seconds

    #     Returns:
    #         list: Historic candle data. Example::
    #             [
    #                 [ time, low, high, open, close, volume ],
    #                 [ 1415398768, 0.32, 4.2, 0.35, 4.2, 12.3 ],
    #                 ...
    #             ]

    #     """
    #     params = {}
    #     if start is not None:
    #         params['start'] = start
    #     if end is not None:
    #         params['end'] = end
    #     if granularity is not None:
    #         acceptedGrans = [60, 300, 900, 3600, 21600, 86400]
    #         if granularity not in acceptedGrans:
    #             newGranularity = min(acceptedGrans, key=lambda x:abs(x-granularity))
    #             print(granularity,' is not a valid granularity level, using',newGranularity,' instead.')
    #             granularity = newGranularity
    #         params['granularity'] = granularity

    #     return self._get('/products/{}/candles'.format(str(product_id)), params=params)

    # def get_product_24hr_stats(self, product_id):
    #     """Get 24 hr stats for the product.

    #     Args:
    #         product_id (str): Product

    #     Returns:
    #         dict: 24 hour stats. Volume is in base currency units.
    #             Open, high, low are in quote currency units. Example::
    #                 {
    #                     "open": "34.19000000",
    #                     "high": "95.70000000",
    #                     "low": "7.06000000",
    #                     "volume": "2.41000000"
    #                 }

    #     """
    #     return self._get('/products/{}/stats'.format(str(product_id)))

    def getCurrencies(self):
        """List known currencies.

        Returns:
            list: List of currencies. Example::
                [{
                    "id": "BTC",
                    "name": "Bitcoin",
                    "min_size": "0.00000001"
                }, {
                    "id": "USD",
                    "name": "United States Dollar",
                    "min_size": "0.01000000"
                }]

        """
        return self._get('/currencies')

    # def get_time(self):
    #     """Get the API server time.

    #     Returns:
    #         dict: Server time in ISO and epoch format (decimal seconds
    #             since Unix epoch). Example::
    #                 {
    #                     "iso": "2015-01-07T23:47:25.201Z",
    #                     "epoch": 1420674445.201
    #                 }

    #     """
    #     return self._get('/time')

if __name__ == '__main__':
    client = PublicClient()

    print client.getProducts()

    print client.getCurrencies()