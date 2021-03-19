"""Includes all the methods available to the ARP endpoint."""
from requests import get

from librenms_handler import LibreNMS


class ARP(LibreNMS):  # pylint: disable=R0903
    """Includes all the methods available to the ARP endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/resources/ip/arp"

    def list_arp(self, query: str):
        """
        Retrieve a specific ARP entry or all ARP entries for a device

        Acceptable queries:

        - IP address
        - MAC address
        - CIDR network (192.168.1.0/24)
        - `all` and set `?device=hostname` (or device ID)

        :param query: device if you specify all for the query then you need to populate this with the hostname
        or id of the device.
        """
        return get(
            f"{self.url}/{query}",
            headers=self.headers,
            verify=self.verify,
        )
