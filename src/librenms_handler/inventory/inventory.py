"""Includes all the methods available to the Inventory endpoint."""
from requests import get

from librenms_handler import LibreNMS


class Inventory(LibreNMS):
    """Includes all the methods available to the Inventory endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/inventory"

    def get_inventory(
        self,
        device: str,
        ent_physical_class: str = None,
        ent_physical_contained_in: str = None,
    ):
        """
        Retrieve the inventory for a device.
        If you call this without any parameters then you will only get part of the inventory.
        This is because a lot of devices nest each component.
        For instance you may initially have the chassis,
        within this the ports - 1 being an SFP cage, then the SFP itself.
        The way this API call is designed is to enable a recursive lookup.
        The first call will retrieve the root entry, included within this response will be entPhysicalIndex.
        You can then call for entPhysicalContainedIn which will then return the next layer of results.
        To retrieve all items together, see get_inventory_for_device.

        :param device: Can be either the device hostname or ID
        :param ent_physical_class: Used to restrict the class of the inventory.
        For example you can specify chassis to only return items in the inventory that are labelled as chassis.
        :param ent_physical_contained_in: Used to retrieve items within the inventory assigned to a previous component.
        For example specifying the chassis (entPhysicalIndex) will retrieve all items where the chassis is the parent.
        """
        parameters = dict(
            {
                "entPhysicalClass": ent_physical_class,
                "entPhysicalContainedIn": ent_physical_contained_in,
            }
        )
        return get(
            f"{self.url}/{device}",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )

    def get_inventory_for_device(
        self,
        device: str,
        ent_physical_class: str = None,
        ent_physical_contained_in: str = None,
    ):
        """
        Retrieve the flattened inventory for a device.
        This retrieves all inventory items for a device regardless of their structure,
        and may be more useful for devices with with nested components.

        :param device: Can be either the device hostname or ID
        :param ent_physical_class: Used to restrict the class of the inventory.
        For example you can specify chassis to only return items in the inventory that are labelled as chassis.
        :param ent_physical_contained_in: Used to retrieve items within the inventory assigned to a previous component.
        For example specifying the chassis (entPhysicalIndex) will retrieve all items where the chassis is the parent.
        """
        parameters = dict(
            {
                "entPhysicalClass": ent_physical_class,
                "entPhysicalContainedIn": ent_physical_contained_in,
            }
        )
        return get(
            f"{self.url}/{device}/all",
            parameters,
            headers=self.headers,
            verify=self.verify,
        )
