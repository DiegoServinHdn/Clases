from cgi import print_arguments
from unicodedata import name
import pandas as pd
import re
from utils import read_json
from request_services import RequestServices
from tmp_files_utils import TmpFilesUtils

# lambda_hanlder(event, context):
#       response = RequestServices(context.get('url'))

def lambda_handler(event, context):
    response = RequestServices.get_request(context)

    read_config = read_json("read_configs.json")

    with TmpFilesUtils() as tmp_folder:
        test_file_name = "test.xlsx"
        test_file_path = tmp_folder.create_file_from_content(test_file_name, response.content)
        df = pd.read_excel(test_file_path, **read_config)
        
        df_columns = list(df.columns)
        replace_columns_dict = {column: re.sub(pattern=r"([A-Z][^A-Z][a-z]+|[A-Z]+)", repl=lambda m: f"_{m.group(1)}", string=column)[1:].lower() for column in df_columns}

        df = df.rename(columns=replace_columns_dict)

        df.to_parquet("test.parquet")


lambda_handler("test", "https://filesamples.com/samples/document/xlsx/sample3.xlsx")
