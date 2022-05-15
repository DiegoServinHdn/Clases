import os
import requests
class NomicsServicesException(Exception):
    pass

class NomicsServices:
    __api_versions_urls = {
        "v1": "https://api.nomics.com/v1"
    }

    __currency_endpoint = "currencies/ticker"
    __global_endpoint = "global-ticker"

    def __init__(self, api_key: str, version:str="v1") -> None:
        self.api_key = api_key

        self.__api_base_url = self.__api_versions_urls.get(version)

    def get_currency_ticker(self, ids: str, interval: str, convert: str, per_page: int=100, page: str=1):
        end_point = f"{self.__api_base_url}/{self.__currency_endpoint}"

        params = {
            "key": os.environ.get("NOMIC_API_KEY") or self.api_key,
            "ids": ids,
            "interval": interval,
            "convert": convert,
            "per-page": per_page,
            "page": page
        }
        
        try:
            response = requests.get(url=end_point, params=params)
            response.raise_for_status()

        except (requests.exceptions.HTTPError) as error:
            raise NomicsServicesException(error) from error

        return response.json()
