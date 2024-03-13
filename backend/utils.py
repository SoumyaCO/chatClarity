'''
Utils cotains all the utility functions related to neither model inference nor data processing
'''
from config import ALLOWED_EXTENSIONS


# check the file is allowed or not
def allowed_file(filename):
    """
    Check if the given filename has an allowed extension.
    
    Args:
        filename (str): The name of the file to check.
        
    Returns:
        bool: True if the file has an allowed extension, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

