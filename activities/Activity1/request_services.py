import requests


class RequestServicesException(Exception):
    pass

class RequestServices:
    @staticmethod
    def get_request(url: str) -> requests.Response:
        """
        Makes a http get request

        Returns:
            requests.Response: get response
        """
        response = requests.get(url)

        if not response.content:
            raise RequestServicesException(ValueError)

        return response