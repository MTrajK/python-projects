from .api_base import ApiBase

class BalanceTransfers(ApiBase):
    """Class for Balance Transfers APIs."""

    GET_BALANCE_TRANSFERS = '/api/tpa/v1/balance_transfers'
    GET_BALANCE_TRANSFERS_COUNT = '/api/tpa/v1/balance_transfers/count'
  
    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get a list of existing Balance Transfers.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all BalanceTransfers that are exported alone will be returned. (optional)

        Returns:
            List with dicts in BalanceTransfers schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported
        }, BalanceTransfers.GET_BALANCE_TRANSFERS)

    def count(self, updated_at=None, exported=None):
        """Get the count of existing Balance Transfers.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all BalanceTransfers that are exported alone will be returned. (optional)

        Returns:
            Count of Refunds.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported
        }, BalanceTransfers.GET_BALANCE_TRANSFERS_COUNT)