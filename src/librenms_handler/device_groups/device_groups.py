"""Includes all the methods available to the DeviceGroups endpoint."""
from requests import delete, get, patch, post

from librenms_handler import LibreNMS


class DeviceGroups(LibreNMS):
    """Includes all the methods available to the DeviceGroups endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/devicegroups"

    def get_devicegroups(self):
        """List all device groups."""
        return get(
            self.url,
            headers=self.headers,
            verify=self.verify,
        )

    def add_devicegroups(  # pylint: disable=R0913
        self,
        name: str,
        group_type: str,
        desc: str = None,
        rules: str = None,
        devices: list = None,
    ):
        """
        Add a new device group.
        Upon success, the ID of the new device group is returned and the HTTP response code is 201.

        :param name: Name of the group
        :param group_type: Should be `static` or `dynamic`.
        Setting this to static requires that the devices input be provided.
        :param desc: Description of the device group
        :param rules: required if type == dynamic.
        A set of rules to determine which devices should be included in this device group
        :param devices: required if type == static.
        A list of devices that should be included in this group. This is a static list of devices
        """
        data = dict(
            {
                "name": name,
                "type": group_type,
                "desc": desc,
            }
        )
        if group_type == "static":
            data.update({"devices": devices})
        elif group_type == "dynamic":
            data.update({"rules": rules})

        return post(
            self.url,
            json=data,
            headers=self.headers,
            verify=self.verify,
        )

    def delete_devicegroup(self, name: str):
        """
        Deletes a device group.

        :param name: name of the device group which can be obtained using get_devicegroups.
        Please ensure that the name is urlencoded if it needs to be (i.e. Linux Servers would need to be urlencoded.)
        """
        return delete(
            f"{self.url}/{name}",
            headers=self.headers,
            verify=self.verify,
        )

    def update_devicegroups(  # pylint: disable=R0913
        self,
        name: str,
        new_name: str = None,
        group_type: str = None,
        desc: str = None,
        rules: str = None,
        devices: list = None,
    ):
        """
        Updates a device group.

        :param name: Name of the group
        :param new_name: optional - New name for this group
        :param group_type: optional - Should be `static` or `dynamic`.
        Setting this to static requires that the devices input be provided.
        :param desc: optional - Description of the device group
        :param rules: required if type == dynamic.
        A set of rules to determine which devices should be included in this device group
        :param devices: required if type == static.
        A list of devices that should be included in this group. This is a static list of devices
        """
        data = {}
        if new_name:
            data.update({"name": new_name})
        if group_type:
            data.update({"type": group_type})
        if desc:
            data.update({"desc": desc})
        if devices:
            data.update({"devices": devices})
        if rules:
            data.update({"rules": rules})

        return patch(
            f"{self.url}/{name}",
            json=data,
            headers=self.headers,
            verify=self.verify,
        )

    def get_devices_by_group(self, name: str):
        """
        List all devices matching the group provided.

        :param name: name of the device group which can be obtained using get_devicegroups.
        Please ensure that the name is urlencoded if it needs to be (i.e. Linux Servers would need to be urlencoded.)
        """
        return get(
            f"{self.url}/{name}",
            headers=self.headers,
            verify=self.verify,
        )

    def add_devices_to_group(
            self,
            name: str,
            devices: list[str]
    ):
        """
        Add devices to a device group.

        :param name: name of the device group which can be obtained using get_devicegroups.
        Please ensure that the name is urlencoded if it needs to be (i.e. Linux Servers would need to be urlencoded.)
        :param devices: A list of devices to be added to the group.
        """
        parameters = {"devices": devices}
        return post(
            f"{self.url}/{name}/devices",
            json=parameters,
            headers=self.headers,
            verify=self.verify
        )

    def del_devices_from_group(
            self,
            name: str,
            devices: list[str]
    ):
        """
        Removes devices from a device group.

        :param name: name of the device group which can be obtained using get_devicegroups.
        Please ensure that the name is urlencoded if it needs to be (i.e. Linux Servers would need to be urlencoded.)
        :param devices: A list of devices to be removed from the group.
        """
        parameters = {"devices": devices}
        return delete(
            f"{self.url}/{name}/devices",
            json=parameters,
            headers=self.headers,
            verify=self.verify
        )
