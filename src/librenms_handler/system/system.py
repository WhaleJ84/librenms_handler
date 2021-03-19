"""Includes all the methods available to the System endpoint."""
from requests import get

from librenms_handler import LibreNMS


class System(LibreNMS):  # pylint: disable=R0903
    """Includes all the methods available to the System endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/system"

    def system(self):
        """Display LibreNMS instance information."""
        return get(self.url, headers=self.headers, verify=self.verify)
