import logging
import os
import sys 
from datetime import datetime


LOG_FILE_NAME=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #Name of the file

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE_NAME)  #The path of the logs
os.makedirs(logs_path,exist_ok=True)  #making a directory
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE_NAME) #final path



logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s], %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,
)