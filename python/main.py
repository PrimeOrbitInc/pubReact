class OptException(Exception):

    def __init__(self, error_code, params):
        """
        Creates a new OptScale exception

        :type error_code: Enum
        :type params: list
        """
        reason = error_code.value[0]
        reason = reason % tuple(params)
        super().__init__(reason)
        self.reason = reason
        self.err_code = error_code
        self.error_code = error_code.name
        self.params = params

class OptHTTPError():
    def __init__(self, status_code, error_code, params):
        """
        Creates a new OptScale HTTP error

        :type status_code: int
        :type error_code: Enum
        :type params: list
        """
        reason = error_code.value[0]
        reason = reason % tuple(params)
        base_params = [status_code, None, *params]
        self.error_code = error_code.name
        self.reason = reason
        self.params = params

    @classmethod
    def from_opt_exception(cls, status_code, opt_exception):
        """
        Creates a new OptScale HTTP error from provided OptScale exception

        :type status_code: int
        :type opt_exception: OptException
        :rtype: OptHTTPError
        """
        return cls(status_code, opt_exception.err_code,
                   opt_exception.params)

if __name__ == '__main__':    
    ret = OptHTTPError.from_opt_exception(404) 
    print(ret)
