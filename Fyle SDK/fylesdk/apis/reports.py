from .api_base import ApiBase

class Reports(ApiBase):
    """Class for Reports APIs."""

    GET_REPORTS = '/api/tpa/v1/reports'
    GET_REPORTS_COUNT = '/api/tpa/v1/reports/count'
  
    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get a list of Reports.
        
        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Reports that are already submitted will alone be returned. (optional)

        Returns:
            List with dicts in Reports schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported
        }, Reports.GET_REPORTS)

    def count(self, updated_at=None, exported=None):
        """Get the count of Reports that match the parameters.
        
        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all Reports that are already submitted will alone be returned. (optional)

        Returns:
            Count of Reports.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported
        }, Reports.GET_REPORTS_COUNT)