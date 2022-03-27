from services.services_ether import EtherServices
import pandas as pd
from utils.pandas_utils import save_dictionary_to_parquet
import os

def lambda_handler(event, context):
    result = EtherServices.get_total_supply(os.environ.get("API_KEY_ETHER"))
    save_dictionary_to_parquet([result])
    print(result)

if __name__ == "__main__":
    lambda_handler("","")