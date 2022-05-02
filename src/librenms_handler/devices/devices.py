"""Includes all the methods available to the Devices endpoint."""
from requests import delete, get, patch, post, put

from librenms_handler import LibreNMS


class Devices(LibreNMS):  # pylint: disable=R0904
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
        self, device: str, health_type: str = None, sensor_id: int = None
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

    def list_available_wireless_graphs(
        self, device: str, wireless_type: str = None, sensor_id: int = None
    ):
        """
        This function allows to do three things:
         - Get a list of overall wireless graphs available.
         - Get a list of wireless graphs based on provided class.
         - Get the wireless sensors information based on ID.

        :param device: Can be either device hostname or ID
        :param wireless_type: Optional wireless type / wireless class
        :param sensor_id:a Optional sensor ID to retrieve specific information
        """
        if wireless_type:
            if sensor_id:
                return get(
                    f"{self.url}/{device}/wireless/{wireless_type}/{sensor_id}",
                    headers=self.headers,
                    verify=self.verify,
                )
            return get(
                f"{self.url}/{device}/wireless/{wireless_type}",
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.url}/{device}/wireless",
            headers=self.headers,
            verify=self.verify,
        )

    def get_health_graph(self, device: str, health_type: str, sensor_id: int = None):
        """
        Get a particular health class graph for a device.
        If you provide a sensor_id as well then a single sensor graph will be provided.
        If no sensor_id value is provided then you will be sent a stacked sensor graph.

        :param device: Can be either device hostname or ID
        :param health_type: Health graph as returned by list_available_health_graphs()
        :param sensor_id: Optional sensor ID graph to return from health graph
        """
        if sensor_id:
            return get(
                f"{self.url}/{device}/graphs/health/{health_type}/{sensor_id}",
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.url}/{device}/graphs/health/{health_type}",
            headers=self.headers,
            verify=self.verify,
        )

    def get_wireless_graph(self, device: str, graph_type: str, senor_id: int = None):
        """
        Get a particular wireless class graph for a device.
        If you provide a sensor_id as well then a single sensor graph will be provided.
        If no sensor_id value is provided then you will be sent a stacked wireless graph.

        :param device: Can be either device hostname or ID
        :param graph_type: Name of wireless graph as returned by list_available_wireless_graphs()
        :param senor_id: Optional sensor ID graph to return from wireless sensor graph
        """
        if senor_id:
            return get(
                f"{self.url}/{device}/graphs/wireless/{graph_type}",
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.url}/{device}/graphs/wireless/{graph_type}/{senor_id}",
            headers=self.headers,
            verify=self.verify,
        )

    def get_graph_generic_by_hostname(  # pylint: disable=R0913
        self,
        device: str,
        graph_type: str,
        date_from: str = None,
        date_to: str = None,
        width: int = None,
        height: int = None,
        output: str = None,
    ):
        """
        Get a specific graph for a device, this does not include ports.

        :param device: Can be either device hostname or ID
        :param graph_type: Type of graph to use. Use get_graphs() to see available graphs.
        :param date_from: date you would like the graph to start
        :param date_to: date you would like the graph to end
        :param width: graph width, defaults to 1075.
        :param height: graph height, defaults to 300.
        :param output: how the graph should be outputted (base64, display), defaults to display.
        """
        parameters = dict(
            {
                "from": date_from,
                "to": date_to,
                "width": width,
                "height": height,
                "output": output,
            }
        )
        return get(
            f"{self.url}/{device}/{graph_type}",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def get_port_graphs(self, device: str, columns: str = None):
        """
        Get a list of ports for a particular device.

        :param device: Can be either the device hostname or ID
        :param columns: Comma separated list of columns you want returned.
        """
        parameters = dict({"columns": columns})
        return get(
            f"{self.url}/{device}/ports",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def get_device_fdb(self, device: str):
        """
        Get a list of FDB entries associated with a device.

        :param device: Can be either the device hostname or ID
        """
        return get(f"{self.url}/{device}/fdb", headers=self.headers, verify=self.verify)

    def get_device_ip_addresses(self, device: str):
        """
        Get a list of IP addresses (v4 and v6) associated with a device.

        :param device: Can be either the device hostname or ID
        """
        return get(f"{self.url}/{device}/ip", headers=self.headers, verify=self.verify)

    def get_port_stack(self, device: str):
        """
        Get a list of port mappings for a device.
        This is useful for showing physical ports that are in a virtual port-channel.

        :param device: Can be either the device hostname or ID
        """
        return get(
            f"{self.url}/{device}/port_stack", headers=self.headers, verify=self.verify
        )

    def get_components(  # pylint: disable=R0913
        self,
        device: str,
        filter_type: str = None,
        component_id: int = None,
        label=None,
        status=None,
        disabled=None,
        ignore=None,
    ):
        """
        Get a list of components for a particular device.

        :param device: Can be either the device hostname or ID
        :param filter_type: Filter the result by type (Equals)
        :param component_id: Filter the result by id (Equals)
        :param label: Filter the result by label (Contains)
        :param status: Filter the result by status (Equals)
        :param disabled: Filter the result by disabled (Equals)
        :param ignore: Filter the result by ignore (Equals)
        """
        parameters = dict(
            {
                "type": filter_type,
                "id": component_id,
                "label": label,
                "status": status,
                "disabled": disabled,
                "ignore": ignore,
            }
        )
        return get(
            f"{self.url}/{device}/components",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def add_components(self, device: str, component_type: str):
        """
        Create a new component of a type on a particular device.

        :param device: Can be either the device hostname or ID
        :param component_type: Type of component to add
        """
        return post(
            f"{self.url}/{device}/components/{component_type}",
            headers=self.headers,
            verify=self.verify,
        )

    def edit_components(  # pylint: disable=R0913
        self,
        device: str,
        component_id: int,
        component_type: str = None,
        label: str = None,
        status: int = None,
        ignore: int = None,
        disabled: int = None,
        error: str = None,
    ):
        """
        Edit an existing component on a particular device.

        :param device: Can be either the decice hostname or ID
        :param component_id:
        :param component_type:
        :param label:
        :param status:
        :param ignore:
        :param disabled:
        :param error:
        """
        data = dict(
            {
                component_id: {
                    "type": component_type,
                    "label": label,
                    "status": status,
                    "ignore": ignore,
                    "disabled": disabled,
                    "error": error,
                }
            }
        )
        return put(
            f"{self.url}/{device}/components",
            data,
            headers=self.headers,
            verify=self.verify,
        )

    def delete_components(self, device: str, component: int):
        """
        Delete an existing component on a particular device.

        :param device: Can be either the device hostname or ID
        :param component: Component ID to be deleted
        """
        return delete(
            f"{self.url}/{device}/components/{component}",
            headers=self.headers,
            verify=self.verify,
        )

    def get_port_stats_by_port_hostname(
        self, device: str, interface_name: str, columns: str = None
    ):
        """
        Get information about a particular port for a device.

        :param device: Can be either the device hostname or ID
        :param interface_name: Any of the interface names for the device which can be obtained using get_port_graphs.
        Please ensure that the ifname is urlencoded if it needs to be (i.e Gi0/1/0 would need to be urlencoded.
        :param columns: Comma separated list of columns you want returned
        """
        parameters = dict({"columns": columns})
        return get(
            f"{self.url}/{device}/ports/{interface_name}",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def get_graph_by_port_hostname(  # pylint: disable=R0913
        self,
        device: str,
        interface_name: str,
        port_type: str,
        date_from: str = None,
        date_to: str = None,
        width: int = None,
        height: int = None,
        interface_description: bool = None,
    ):
        """
        Get a graph of a port for a particular device.

        :param device: Can be either the device hostname or ID
        :param interface_name: Any of the interface names for the device which can be obtained using get_port_graphs.
        Please ensure that the ifname is urlencoded if it needs to be (i.e Gi0/1/0 would need to be urlencoded.
        :param port_type: Type is the port type you want the graph for.
        You can request a list of ports for a device with get_port_graphs
        :param date_from: date you would like the graph to start
        :param date_to: date you would like the graph to end
        :param width: graph width, defaults to 1075.
        :param height: graph height, defaults to 300.
        :param interface_description: Will use ifDescr to lookup the port instead of ifName when true.
        Pass the ifDescr value you want to search as you would ifName.
        """
        parameters = dict(
            {
                "from": date_from,
                "to": date_to,
                "width": width,
                "height": height,
                "ifDescr": interface_description,
            }
        )
        return get(
            f"{self.url}/{device}/ports/{interface_name}/{port_type}",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

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

    def list_oxidized(self, device: str = None):
        """
        List devices for use with Oxidized.
        If you have group support enabled then a group will also be returned based on your config.

        :param device: Can be either the device hostname or ID
        """
        if device:
            return get(
                f"{self.base_url}/api/v0/oxidized/{device}",
                headers=self.headers,
                verify=self.verify,
            )
        return get(
            f"{self.base_url}/api/v0/oxidized",
            headers=self.headers,
            verify=self.verify,
        )

    def update_device_field(self, device: str, field=None, data=None):
        """
        Updates devices field in the database.

        :param device: Can be either the device hostname or ID
        :param field: Column name within the database (can be an array of fields)
        :param data: Data to update the column with (can be an array of data)
        """
        data = dict(
            {
                "field": field,
                "data": data,
            }
        )
        return patch(
            f"{self.url}/{device}",
            json=data,
            headers=self.headers,
            verify=self.verify,
        )

    def rename_device(self, device: str, new_hostname: str):
        """
        Rename device.

        :param device: Can be either the device hostname or ID
        :param new_hostname: New hostname for the device
        """
        return patch(
            f"{self.url}/{device}/rename/{new_hostname}",
            headers=self.headers,
            verify=self.verify,
        )

    def get_device_groups(self, device: str):
        """
        List the device groups that a device is matched on.

        :param device: Can be either the device hostname or ID
        """
        return get(
            f"{self.url}/{device}/groups",
            headers=self.headers,
            verify=self.verify,
        )

    def search_oxidized(self, search_string: str):
        """
        Search all oxidized device configs for a string.

        :param search_string: The Specific string you would like to search for
        """
        return get(
            f"{self.base_url}/api/v0/oxidized/config/search/{search_string}",
            headers=self.headers,
            verify=self.verify,
        )

    def get_oxidized_config(self, device_name: str):
        """
        Returns a specific device's config from oxidized.

        :param device_name: The full DNS name of the device used when adding the device to LibreNMS
        """
        return get(
            f"{self.base_url}/api/v0/oxidized/config/{device_name}",
            headers=self.headers,
            verify=self.verify,
        )

    def add_parents_to_host(self, device: str, parent_ids):
        """
        Add one or more parents to host.

        :param device: Can be either the device hostname or ID
        :param parent_ids: One or more parent IDs or hostnames
        """
        data = dict(
            {
                "parent_ids": parent_ids,
            }
        )
        return post(
            f"{self.url}/{device}/parents",
            json=data,
            headers=self.headers,
            verify=self.verify,
        )

    def delete_parents_from_host(self, device: str, parent_ids=None):
        """
        Deletes some or all of the parents from a host.

        :param device: Can be either the device hostname or ID
        :param parent_ids: One or more parent IDs or hostnames.
        If not specified deletes all parents from host.
        """
        data = dict(
            {
                "parent_ids": parent_ids,
            }
        )
        return delete(
            f"{self.url}/{device}/parents",
            data=data,
            headers=self.headers,
            verify=self.verify,
        )

    def maintenance_device(self, device: str, notes: str, duration: str):
        """
        Set a device into maintenance mode.

        :param device: Can be either the device hostname or ID
        :param notes: Some description for the Maintenance
        :param duration: Duration of Maintenance in format H:m
        """
        data = dict(
            {
                "notes": notes,
                "duration": duration
            }
        )
        return post(
            f"{self.url}/{device}/maintenance",
            json=data,
            headers=self.headers,
            verify=self.verify,
        )
