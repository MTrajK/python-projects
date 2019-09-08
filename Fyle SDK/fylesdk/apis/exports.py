from .api_base import ApiBase

class Exports(ApiBase):
    """Class for Exports APIs."""

    POST_EXPORTS = '/api/tpa/v1/exports'
    GET_EXPORTS = '/api/tpa/v1/exports'
    GET_EXPORTS_COUNT = '/api/tpa/v1/exports/count'
    GET_EXPORT_BY_ID = '/api/tpa/v1/exports/{0}'

    def post(self, data):
        """Mark Third Party Export of Fyle objects as Successful or Failed.

        Parameters:
            data (list): List of dicts in Exports schema.
        """
        return self._post_request(data, Exports.POST_EXPORTS)
        
    def get(self, updated_at=None, offset=None, limit=None):
        """Returns the details of Third Party Exports.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)

        Returns:
            List with dicts in Exports schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit
        }, Exports.GET_EXPORTS)

    def count(self, updated_at=None):
        """Returns the count of Third Party Exports, that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)

        Returns:
            Count of Exports.
        """
        return self._get_request({
            'updated_at': updated_at
        }, Exports.GET_EXPORTS_COUNT)

    def get_by_id(self, export_id):
        """Get the details of a Third Party Export.

        Parameters:
            expense_id (str): Unique ID to find an Export. (required)

        Returns:
            Dict in Export schema.
        """
        return self._get_request({}, Exports.GET_EXPORT_BY_ID.format(export_id))