from .api_base import ApiBase

class HotelRequests(ApiBase):
    """Class for Hotel Requests APIs."""

    GET_HOTEL_REQUESTS = '/api/tpa/v1/hotel_requests'
    GET_HOTEL_REQUESTS_COUNT = '/api/tpa/v1/hotel_requests/count'
  
    def get(self, trip_request_id=None, updated_at=None, offset=None, limit=None):
        """Get a list of existing Hotel Request matching the parameters.

        Parameters:
            trip_request_id (str): Unique id of TripRequest object, if this value is passed it returns objects assiocated with a trip. (optional)
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)

        Returns:
            List with dicts in HotelRequests schema.
        """
        return self._get_request({
            'trip_request_id': trip_request_id,
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit
        }, HotelRequests.GET_HOTEL_REQUESTS)

    def count(self, trip_request_id=None, updated_at=None):
        """Get the count of existing Hotel Requests.

        Parameters:
            trip_request_id (str): Unique id of TripRequest object, if this value is passed it returns objects assiocated with a trip. (optional)
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)

        Returns:
            Count of Hotel Requests.
        """
        return self._get_request({
            'trip_request_id': trip_request_id,
            'updated_at': updated_at
        }, HotelRequests.GET_HOTEL_REQUESTS_COUNT)