import sys
import logging
def error_message_detail(error,error_detail:sys) ->str:
    """ Extract detailed error information including filename,line number and error message """
    #extract traceback details(exception information)
    _,_, exc_tb=error_detail.exc_info()
    #get the file name where the exception occured
    file_name=exc_tb.tb_frame.f_code.co_filename
    #create a formatted error message string with file name,line number and the actual error
    line_number=exc_tb.tb_lineno
    error_message=f"File: {file_name} at line number: {line_number} with error message: {str(error)}"

    #log the error for better tracking
    logging.error(error_message)
    return error_message
class MyException(Exception):
    """ Custom exception class to handle specific exceptions in the application """
    def __init__(self,error_message,error_detail:sys):
        #call the base class in instructor with theh error 
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message

    