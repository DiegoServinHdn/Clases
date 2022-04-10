import pandas as pd
from typing import List

def save_dictionary_to_parquet(records:List[dict])->None:
    """
    Guarda response en formato parquet

    Args:
        records (List[dict]): recibe respuesta del api
    """
    df = pd.DataFrame.from_records(records)
    df.to_parquet("../parquets/total_supply.parquet")
