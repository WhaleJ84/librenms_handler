"""Includes all the methods available to the Logs endpoint."""
from requests import get

from librenms_handler import LibreNMS


class Logs(LibreNMS):
    """Includes all the methods available to the Logs endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/logs"

    def list_eventlog(  # pylint: disable=R0913
        self,
        device: str = None,
        start=None,
        limit: int = None,
        date_from=None,
        date_to=None,
    ):
        """
        Retrieve all event logs or event logs for a specific device.

        :param device: ID or hostname of the specific device
        :param start:
        :param limit:
        :param date_from:
        :param date_to:
        """
        parameters = dict(
            {
                "start": start,
                "limit": limit,
                "from": date_from,
                "to": date_to,
            }
        )
        if device:
            return get(
                f"{self.url}/eventlog/{device}",
                parameters,
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.url}/eventlog",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def list_syslog(  # pylint: disable=R0913
        self,
        device: str = None,
        start=None,
        limit: int = None,
        date_from=None,
        date_to=None,
    ):
        """
        Retrieve all syslogs or syslogs for a specific device.

        :param device: ID or hostname of the specific device
        :param start:
        :param limit:
        :param date_from:
        :param date_to:
        """
        parameters = dict(
            {
                "start": start,
                "limit": limit,
                "from": date_from,
                "to": date_to,
            }
        )
        if device:
            return get(
                f"{self.url}/syslog/{device}",
                parameters,
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.url}/syslog",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def list_alertlog(  # pylint: disable=R0913
        self,
        device: str = None,
        start=None,
        limit: int = None,
        date_from=None,
        date_to=None,
    ):
        """
        Retrieve all alert logs or alert logs for a specific device.

        :param device: ID or hostname of the specific device
        :param start:
        :param limit:
        :param date_from:
        :param date_to:
        """
        parameters = dict(
            {
                "start": start,
                "limit": limit,
                "from": date_from,
                "to": date_to,
            }
        )
        if device:
            return get(
                f"{self.url}/alertlog/{device}",
                parameters,
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.url}/alertlog",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def list_authlog(  # pylint: disable=R0913
        self,
        start=None,
        limit: int = None,
        date_from=None,
        date_to=None,
    ):
        """
        Retrieve all auth logs or auth logs for a specific device.

        :param start:
        :param limit:
        :param date_from:
        :param date_to:
        """
        parameters = dict(
            {
                "start": start,
                "limit": limit,
                "from": date_from,
                "to": date_to,
            }
        )
        return get(
            f"{self.url}/authlog",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )
