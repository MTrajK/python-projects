If something is not okay with the request then the Fyle API will return an error code: 400, 401, 403, 404, 498, 500, etc.

In this SDK are implemented all of these errors, you can use try..except to handle these responses.

### FyleSDKError
The base exception class for FyleSDK.

**Parameters:**
* msg (str): Short description of the error.
* response: Error response from the API call.

### NotFoundClientError
Client not found OAuth2 authorization, 404 error.

### UnauthorizedClientError
Wrong client secret and/or refresh token, 401 error.

### ExpiredTokenError
Expired (old) access token, 498 error.

### InvalidTokenError
Wrong/non-existing access token, 401 error.

### NoPrivilegeError
The user has insufficient privilege, 403 error.

### WrongParamsError
Some of the parameters (HTTP params or request body) are wrong, 400 error.

### NotFoundItemError
Not found the item from URL, 404 error.

### InternalServerError
The rest FyleSDK errors, 500 error.

