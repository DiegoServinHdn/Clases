import requests

class EtherServicesException(Exception):
    pass

class EtherServices:

    @staticmethod
    def get_total_supply(apikey: str, retry_attempts: int = 3) -> dict:
        """
        Obtener el total ether que circulan

        Args:
            apikey (str): apikey para los accesos al endpoint

        Returns:
            dict: retorna los ether en circulacion
        """
        endpoint = "https://api.etherscan.io/api"
        params = {'module': 'stats', 'action': 'ethsupply', 'apikey': apikey}
        response = requests.get(endpoint, params= params)

        for attemp in range(1, retry_attempts + 1):
            try:
                response = requests.get(endpoint, params= params)
                response.raise_for_status()
            except requests.exceptions.HTTPError as http_error:
                if attemp >= retry_attempts:
                    print(f"Se supero el limite de intetos mayor a {retry_attempts}")
                    raise EtherServicesException from http_error
            else:
                break

        return response.json()