from .api_base import ApiBase

class Advances(ApiBase):
    """Class for Advances APIs."""

    GET_ADVANCES = '/api/tpa/v1/advances'
    GET_ADVANCES_COUNT = '/api/tpa/v1/advances/count'
  
    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get a list of existing Advances.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Advances that are exported alone will be returned. (optional)

        Returns:
            List with dicts in Advance schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported
        }, Advances.GET_ADVANCES)

    def count(self, updated_at=None, exported=None):
        """Get a count of the existing Advances that match the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            exported (bool): If set to true, all Advances that are exported alone will be returned. (optional)

        Returns:
            Count of Advances.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported
        }, Advances.GET_ADVANCES_COUNT)