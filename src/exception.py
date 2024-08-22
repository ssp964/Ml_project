import sys
from src.logger import logging

# extracts and formats info about where the error happened along with the error message
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # extract only tracback
    file_name=exc_tb.tb_frame.f_code.co_filename # get file name from the tracback
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
# enhances the built-in 'Exception' by adding detailed context of the error occurred
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): # create an object to inherit exception class
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self): # override the default string reprensentation to the custom representation (i.e error_message)
        return self.error_message
