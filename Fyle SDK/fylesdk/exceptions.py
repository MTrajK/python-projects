
class FyleSDKError(Exception):
    """The base exception class for FyleSDK.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(FyleSDKError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        return repr(self.message)


class NotFoundClientError(FyleSDKError):
    """Client not found OAuth2 authorization, 404 error."""
    pass


class UnauthorizedClientError(FyleSDKError):
    """Wrong client secret and/or refresh token, 401 error."""
    pass


class ExpiredTokenError(FyleSDKError):
    """Expired (old) access token, 498 error."""
    pass


class InvalidTokenError(FyleSDKError):
    """Wrong/non-existing access token, 401 error."""
    pass


class NoPrivilegeError(FyleSDKError):
    """The user has insufficient privilege, 403 error."""
    pass


class WrongParamsError(FyleSDKError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""
    pass


class NotFoundItemError(FyleSDKError):
    """Not found the item from URL, 404 error."""
    pass
    

class InternalServerError(FyleSDKError):
    """The rest FyleSDK errors, 500 error."""
    pass