import requests

class NewsServicesException(Exception):
    pass

class NewsServices:

    @staticmethod
    def get_content(apikey: str, retry_attempts: int = 3) -> dict:
        """
        Obtener noticias

        Args:
            apikey (str): apikey para los accesos al endpoint

        Returns:
            dict: retorna noticias
        """
        endpoint = "https://content.guardianapis.com/search"
        params = {'q': 'debates', 'api-key': apikey}
        response = requests.get(endpoint, params= params)

        for attemp in range(1, retry_attempts + 1):
            try:
                response = requests.get(endpoint, params= params)
                response.raise_for_status()
            except requests.exceptions.HTTPError as http_error:
                if attemp >= retry_attempts:
                    print(f"Se supero el limite de intetos mayor a {retry_attempts}")
                    raise NewsServicesException from http_error
            else:
                break

        return response.json()