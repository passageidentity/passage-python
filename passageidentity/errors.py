"""
Error class for Passage errors
"""
class PassageError(Exception):
    def __init__(self, message, status_code:int=None, status_text:str=None, body:dict=None):
        self.message = message
        self.status_code = status_code
        self.status_text = status_text
        if body != None:
            self.error = body["error"]
        else:
            self.error = None

