class MyValidateError(Exception)
    title = None
    detail = None

    def __str__(self):

        return str(self.title)
    
    class My