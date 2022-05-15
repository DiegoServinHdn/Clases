import requests

class NomicsServicesException(Exception):
    pass

class NomicsServices:

    __currency_endpoint = "currencies/ticker"
    __global_endpoint = ""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_currency_ticker(self, currency):
        end_point = self.__currency_endpoint
        params = {
            curl "https://api.nomics.com/v1/currencies/ticker?
            key=your-key-here&
            ids=BTC,ETH,XRP&interval=1d,30d&
            convert=EUR&
            platform-currency=ETH&
            per-page=100&
            page=1"
        }
        
