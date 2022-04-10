import json
from datetime import datetime, timedelta


class CommonUtilsExeption(Exception):
    pass


class CommonUtils:
    @staticmethod
    def get_json_data(data_request):
        """
        Method to get json from string
        Args:
            data_request (str):
        Returns:
            [json]: Json with data
        """
        try:
            data_json = json.loads(json.dumps(data_request))
        except ValueError as e:
            print(e)
        return data_json

    @staticmethod
    def get_current_time(date_format:str):
        """
        Method to get the current time with the date format specified
        Args:
            date_format (str): The format of the date that the string will have
        Returns:
            [str]: The current time formatted
        """
        time_object = datetime.now()
        return time_object.strftime(date_format)
