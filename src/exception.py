import sys # gives access to Python system-level details — like the current exception info.
from src.logger import logging

# This function is designed to extract detailed information about an error.
# Parameters:
# error → the actual error/exception object.
# error_detail → the sys module, passed so it can access traceback info.
def error_message_detail(error,error_detail:sys):

# exc_info() returns a tuple of three values:
#   1. The exception type
#   2. The exception value (actual error)
#   3. The traceback object (which contains file, line number, etc.)
# Here, only exc_tb (the traceback object) is needed, so the first two values are ignored using _.
    _,_,exc_tb=error_detail.exc_info()

# Extracts the file name from the traceback object where the error occurred.
#   exc_tb.tb_frame.f_code.co_filename means:
#       tb_frame → the current stack frame.
#       f_code → the code object being executed.
#       co_filename → the filename of the source code.
# So this line gives the exact Python file where the exception happened.
    file_name=exc_tb.tb_frame.f_code.co_filename

# This constructs a readable and descriptive error message that includes:
# File name
# Line number (exc_tb.tb_lineno)
# Actual error message (str(error))
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


        