import os
import pandas as pd
from services.services_news import NewsServices
from util.commun_utils import CommonUtils
from util.pandas_utils import save_dictionary_to_parquet
from util.pandas_utils import create_dataframe
from util.pandas_utils import read_parquet_file


def lambda_handler(event, context):
    result = NewsServices.get_content(os.environ.get("API_KEY_THEGUARDIAN"))
    result_resumen = CommonUtils.get_json_data(result)
    note = create_dataframe(result_resumen)
    save_dictionary_to_parquet(note)
    read_parquet_file("../parquets/theguardian.220329-001134.parquet")

if __name__ == "__main__":
    lambda_handler("","")