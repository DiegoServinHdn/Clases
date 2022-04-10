import os
from select import select
import shutil
from tkinter.messagebox import RETRY

class TmpFilesUtilsException(Exception):
    pass


class TmpFilesUtils:
    tmp_dir_name = "tmp"

    def __init__(self) -> None:
        pass

    def __enter__(self) -> None:
        if not os.path.exists(f"./{self.tmp_dir_name}"):
            os.makedirs(f"./{self.tmp_dir_name}")
        
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        if os.path.exists(f"./{self.tmp_dir_name}"):
            shutil.rmtree(f"./{self.tmp_dir_name}")


    def create_file_from_content(self, file_name: str, content: bytes) -> str:
        output_path = f"{self.tmp_dir_name}/{file_name}"

        with open(output_path, 'wb') as file:
            file.write(content)

        return output_path
        
        
