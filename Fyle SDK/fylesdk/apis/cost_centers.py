from .api_base import ApiBase

class CostCenters(ApiBase):
    """Class for Cost Centers APIs."""

    GET_COST_CENTERS = '/api/tpa/v1/cost_centers'
  
    def get(self, active_only=None):
        """Get the list of existing CostCenters.

        Parameters:
            active_only (bool): When set as false, the result will include all the Cost Centers for the organization. (optional)

        Returns:
            List with dicts in CostCenters schema.
        """
        return self._get_request({
            'active_only': active_only
        }, CostCenters.GET_COST_CENTERS)