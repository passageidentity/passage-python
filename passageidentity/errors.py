"""
Error class for Passage errors
"""
class PassageError(Exception):
    def __init__(self, message="Error in Passage"):
        self.message = message
        super().__init__(self.message)

