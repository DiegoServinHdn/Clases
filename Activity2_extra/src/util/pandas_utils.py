from util.commun_utils import CommonUtils
import pandas as pd
import pyarrow.parquet as pq
from typing import List
from IPython.display import display

def create_dataframe(result:dict)-> dict:
    """_summary_

    Args:
        result (dict): _description_

    Returns:
        dict: _description_
    """
    note = {"section_Id":[],
            "section_Name": [],
            "web_Title": [],
            "web_Url": []
            }
    for news_detail in result:
        news = result.get(news_detail).get("results")
        for i in range(len(news)):
            note["section_Id"].append(news[i].get("sectionId"))
            note["section_Name"].append(news[i].get("sectionName"))
            note["web_Title"].append(news[i].get("webTitle"))
            note["web_Url"].append(news[i].get("webUrl"))
    tabla_note = pd.DataFrame({
          'section_Id':note["section_Id"],
          'section_Name':note["section_Name"],
          'web_Title':note["web_Title"],
          'web_Url':note["web_Url"],
          })
    return tabla_note

def save_dictionary_to_parquet(tabla_note:dict)->dict:
    """
    Guarda response en formato parquet

    Args:
        tabla_note (DataFrame): recibe respuesta del api
    """
    timestamp = "%y%m%d-%H%M%S"
    output_folder = "../parquets"
    file_basename = "theguardian"
    time_creation = CommonUtils.get_current_time(timestamp)
    tabla_note.to_parquet(f"{output_folder}/{file_basename}.{time_creation}.parquet")


def read_parquet_file(parquet_file):
    """_summary_

    Args:
        parquet_file (file): _description_
    """
    pd.set_option('display.max_columns', None)
    df = pq.read_table(parquet_file).to_pandas()
    display(df)
