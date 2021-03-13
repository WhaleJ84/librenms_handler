"""Includes all the methods available to the Devices endpoint."""
from requests import delete, get, post

from librenms_handler import LibreNMS


class Devices(LibreNMS):
    """Includes all the methods available to the Devices endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/devices"

    def del_device(self, device: str):
        """
        Delete a given device.

        :param device: Can be either the device hostname or ID
        """
        return delete(f"{self.url}/{device}", headers=self.headers, verify=self.verify)

    def get_device(self, device: str):
        """
        Get details of a given device.

        :param device: Can be either the device hostname or ID
        """
        return get(f"{self.url}/{device}", headers=self.headers, verify=self.verify)

    def discover_device(self, device: str):
        """
        Trigger a discovery of given device.

        :param device: Can be either the device hostname or ID
        """
        return get(
            f"{self.url}/{device}/discover", headers=self.headers, verify=self.verify
        )

    def availability(self, device: str):
        """
        Get calculated availabilities of given device.

        :param device: Can be either the device hostname or ID
        """
        return get(
            f"{self.url}/{device}/availability",
            headers=self.headers,
            verify=self.verify,
        )

    def outages(self, device: str):
        """
        Get detected outages of given device.

        :param device: Can be either the device hostname or ID
        """
        return get(
            f"{self.url}/{device}/outages", headers=self.headers, verify=self.verify
        )

    def get_graphs(self, device: str):
        """
        Get a list of available graphs for a device, this does not include ports.

        :param device:  Can be either the device hostname or ID
        """
        return get(
            f"{self.url}/{device}/graphs", headers=self.headers, verify=self.verify
        )

    def list_available_health_graphs(
        self, device: str, health_type: str = None, sensor_id: str = None
    ):
        """
        This function allows to do three things:
         - Get a list of overall health graphs available.
         - Get a list of health graphs based on provided class.
         - Get the health sensors information based on ID.

        :param device: Can be either device hostname or ID
        :param health_type: Optional health type / sensor class
        :param sensor_id: Optional sensor ID to retrieve specific information
        """
        if health_type:
            if sensor_id:
                return get(
                    f"{self.url}/{device}/health/{health_type}/{sensor_id}",
                    headers=self.headers,
                    verify=self.verify,
                )
            return get(
                f"{self.url}/{device}/health/{health_type}",
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.url}/{device}/health", headers=self.headers, verify=self.verify
        )

    # def _get_health_graph(self, device: str, health_type: str, sensor_id: str = None):
    #     """
    #
    #     :param device:
    #     :param health_type:
    #     :param sensor_id:
    #     """
    #     pass
    #
    # def _get_wireless_graph(self, device: str, graph_type: str, senor_id: str = None):
    #     """
    #
    #     :param device:
    #     :param graph_type:
    #     :param senor_id:
    #     """
    #     pass
    #
    # def _get_graph_generic_by_hostname(self, device: str, graph_type: str):
    #     """
    #
    #     :param device:
    #     :param graph_type:
    #     """
    #     pass
    #
    # def _get_port_graphs(self, device: str):
    #     """
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _get_device_fdb(self, device: str):
    #     """
    #
    #     :param device:
    #     """
    #     pass

    def get_device_ip_addresses(self, device: str):
        """
        Get a list of IP addresses (v4 and v6) associated with a device.

        :param device: Can be either the device hostname or ID
        """
        return get(f"{self.url}/{device}/ip", headers=self.headers, verify=self.verify)

    # def _get_port_stack(self, device: str):
    #     """
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _get_components(self, device: str):
    #     """
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _add_components(self, device: str, component_type: str):
    #     """
    #
    #     :param device:
    #     :param component_type:
    #     """
    #     pass
    #
    # def _edit_components(self, device: str):
    #     """
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _delete_components(self, device: str, component: str):
    #     """
    #
    #     :param device:
    #     :param component:
    #     """
    #     pass
    #
    # def _get_port_stats_by_port_hostname(self, device: str, interface_name: str):
    #     """
    #
    #     :param device:
    #     :param interface_name:
    #     """
    #     pass
    #
    # def _get_graph_by_port_hostname(
    #     self, device: str, interface_name: str, port_type: str
    # ):
    #     """
    #
    #     :param device:
    #     :param interface_name:
    #     :param port_type:
    #     """
    #     pass

    def list_locations(self):
        """Return a list of locations."""
        return get(
            f"{self.base_url}/api/v0/resources/locations",
            headers=self.headers,
            verify=self.verify,
        )

    def list_sensors(self):
        """Get a list of all Sensors."""
        return get(
            f"{self.base_url}/api/v0/resources/sensors",
            headers=self.headers,
            verify=self.verify,
        )

    def list_devices(
        self, order: str = None, order_type: str = None, query: str = None
    ):
        """
        Return a list of devices.

        === Order Types ===

        - all: All devices
        - active: Only not ignored and not disabled devices
        - ignored: Only ignored devices
        - up: Only devices that are up
        - down: Only devices that are down
        - disabled: Disabled devices
        - os: search by os type
        - mac: search by mac address
        - ipv4: search by IPv4 address
        - ipv6: search by IPv6 address
        - location: search by location
        - hostname: search by hostname

        :param order: Orders output. Defaults 'hostname'. Can be prepended by DESC or ASC to change the order
        :param order_type: Filter or search by one of the parameters shown above
        :param query: If searching by, then this will be used as the input
        """
        parameters = dict({"order": order, "type": order_type, "query": query})
        return get(self.url, parameters, headers=self.headers, verify=self.verify)

    def add_device(  # pylint: disable=C0103, R0913, R0914
        self,
        hostname: str,
        overwrite_ip: str = None,
        port: int = None,
        transport: str = None,
        version: str = None,
        poller_group: int = None,
        force_add: bool = None,
        community: str = None,
        authlevel: str = None,
        authname: str = None,
        authpass: str = None,
        authalgo: str = None,
        cryptopass: str = None,
        cryptoalgo: str = None,
        snmp_disable: bool = None,
        os: str = None,
        hardware: str = None,
    ):
        """
        Add a new device.

        :param hostname: device hostname
        :param overwrite_ip: alternate polling IP. Will be use instead of hostname (optional)
        :param port: SNMP port (defaults to port defined in config).
        :param transport: SNMP protocol (defaults to transport defined in config).
        :param version: SNMP version to use, v1, v2c or v3. Defaults to v2c.
        :param poller_group: This is the poller_group id used for distributed poller setup. Defaults to 0.
        :param force_add: Force the device to be added regardless of it being able to respond to snmp or icmp.
        :param community: Required for SNMP v1 or v2c.
        :param authlevel: SNMP authlevel (noAuthNoPriv, authNoPriv, authPriv).
        :param authname: SNMP Auth username
        :param authpass: SNMP Auth password
        :param authalgo: SNMP Auth algorithm (MD5, SHA)
        :param cryptopass: SNMP Crypto Password
        :param cryptoalgo: SNMP Crypto algorithm (AES, DES)
        :param snmp_disable: Boolean, set to true for ICMP only.
        :param os: OS short name for the device (defaults to ping).
        :param hardware: Device hardware.
        """
        data = dict(
            {
                "hostname": hostname,
                "overwrite_ip": overwrite_ip,
                "port": port,
                "transport": transport,
                "version": version,
                "poller_group": poller_group,
                "force_add": force_add,
                "community": community,
                "authlevel": authlevel,
                "authname": authname,
                "authpass": authpass,
                "authalgo": authalgo,
                "cryptopass": cryptopass,
                "cryptoalgo": cryptoalgo,
                "snmp_disable": snmp_disable,
                "os": os,
                "hardware": hardware,
            }
        )
        return post(self.url, json=data, headers=self.headers, verify=self.verify)

    # def _list_oxidized(self, device: str):
    #     """
    #     List devices for use with Oxidized.
    #     If you have group support enabled then a group will also be returned based on your config.
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _update_device_field(self, device: str):
    #     """
    #     Updates devices field in the database.
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _rename_device(self, device: str, new_hostname: str):
    #     """
    #     Rename device.
    #
    #     :param device:
    #     :param new_hostname:
    #     """
    #     pass
    #
    # def _get_device_groups(self, device: str):
    #     """
    #     List the device groups that a device is matched on.
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _search_oxidized(self, search_string: str):
    #     """
    #     Search all oxidized device configs for a string.
    #
    #     :param search_string:
    #     """
    #     pass
    #
    # def _get_oxidized_config(self, device_name: str):
    #     """
    #     Returns a specific device's config from oxidized.
    #
    #     :param device_name:
    #     """
    #     pass
    #
    # def _add_parents_to_host(self, device: str):
    #     """
    #     Add one or more parents to host.
    #
    #     :param device:
    #     """
    #     pass
    #
    # def _delete_parents_from_host(self, device: str):
    #     """
    #     Deletes some or all of the parents from a host.
    #
    #     :param device:
    #     """
    #     pass
