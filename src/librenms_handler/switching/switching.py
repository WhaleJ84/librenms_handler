"""Includes all the methods available to the Devices endpoint."""
from requests import get

from librenms_handler import LibreNMS


class Switching(LibreNMS):
    """Includes all the methods available to the Switching endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/resources"

    def list_vlans(self):
        """
        Get a list of all VLANs.
        """
        return get(f"{self.url}/vlans", headers=self.headers, verify=self.verify)

    def get_vlans(self, device: str):
        """
        Get a list of all VLANs for a given device

        :param device: Can be either the device hostname or ID
        """
        return get(
            f"{self.base_url}/api/v0/devices/{device}/vlans",
            headers=self.headers,
            verify=self.verify,
        )

    def list_links(self):
        """
        Get a list of all Links.
        """
        return get(f"{self.url}/links", headers=self.headers, verify=self.verify)

    def get_links(self, device: str):
        """
        Get a list of all Links for a given device

        :param device: Can be either the device hostname or ID
        """
        return get(
            f"{self.base_url}/api/v0/devices/{device}/links",
            headers=self.headers,
            verify=self.verify,
        )

    def get_link(self, link: str):
        """
        Retrieves Link by ID

        :param link: Should be a link ID (integer)
        """
        return get(f"{self.url}/links/{link}", headers=self.headers, verify=self.verify)

    def list_fdb(self, mac: str = None):
        """
        Get a list of all ports FDB

        :param mac: is the specific MAC address you would like to query
        """
        if not mac:
            mac = ''

        return get(f"{self.url}/fdb/{mac}", headers=self.headers, verify=self.verify)
