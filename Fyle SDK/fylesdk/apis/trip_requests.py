from .api_base import ApiBase

class TripRequests(ApiBase):
    """Class for Trip Requests APIs."""

    GET_TRIP_REQUESTS = '/api/tpa/v1/trip_requests'
    GET_TRIP_REQUESTS_COUNT = '/api/tpa/v1/trip_requests/count'
  
    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get a list of existing Trip Request matching the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)

        Returns:
            List with dicts in TripRequests schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit
        }, TripRequests.GET_TRIP_REQUESTS)

    def count(self, updated_at=None, exported=None):
        """Get the count of existing Trip Requests.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)

        Returns:
            Count of Trip Request.
        """
        return self._get_request({
            'updated_at': updated_at
        }, TripRequests.GET_TRIP_REQUESTS_COUNT)