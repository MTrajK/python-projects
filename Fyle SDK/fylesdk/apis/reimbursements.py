from .api_base import ApiBase

class Reimbursements(ApiBase):
    """Class for Reimbursements APIs."""

    GET_REIMBURSEMENTS = '/api/tpa/v1/reimbursements'
    GET_REIMBURSEMENTS_COUNT = '/api/tpa/v1/reimbursements/count'
  
    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get Reimbursments that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Reimbursments that are exported alone will be returned. (optional)

        Returns:
            List with dicts in Reimbursments schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported
        }, Reimbursements.GET_REIMBURSEMENTS)

    def count(self, updated_at=None, exported=None):
        """Get the number of Reimbursements that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all Reimbursements that are exported alone will be returned. (optional)

        Returns:
            Count of Reimbursements.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported
        }, Reimbursements.GET_REIMBURSEMENTS_COUNT)