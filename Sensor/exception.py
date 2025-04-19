import sys
import os


def error_msg_details(error,error_detail:sys):  #kaun si file me error ,kya error and kaunse line me error
    _,_,exc_tb=error_detail.exc_info()   #first two important nhi hai,tuple 3 chix dega hme sirf 3rd wale ki jarurat
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_msg=error
    error_message=f"error occured in {file_name} in line number {line_number} and the error is {error_msg} "
    return error_message



class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #to use the inherited class
        self.error_msg=error_msg_details(error_message,error_detail=error_detail)

    def __str__(self):  #string ki form me error dikhayega
        return self.error_msg

