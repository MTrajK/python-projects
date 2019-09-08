from .api_base import ApiBase

class Refunds(ApiBase):
    """Class for Refunds APIs."""

    GET_REFUNDS = '/api/tpa/v1/refunds'
    GET_REFUNDS_COUNT = '/api/tpa/v1/refunds/count'
  
    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get a list of existing Refunds.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Refunds that are exported alone will be returned. (optional)

        Returns:
            List with dicts in Refunds schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported
        }, Refunds.GET_REFUNDS)

    def count(self, updated_at=None, exported=None):
        """Get the count of existing Refunds that match the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all Refunds that are exported alone will be returned. (optional)

        Returns:
            Count of Refunds.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported
        }, Refunds.GET_REFUNDS_COUNT)