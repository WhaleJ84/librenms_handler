"""Includes all the methods available to the Locations endpoint."""
from requests import delete, patch, post

from librenms_handler import LibreNMS


class Locations(LibreNMS):
    """Includes all the methods available to the Locations endpoint."""

    def __init__(self, url=None, token=None, verify=True):
        super().__init__(url, token, verify)
        self.base_url = self.url
        self.url = f"{self.url}/api/v0/locations"

    def add_location(self, location: str, lat=None, lng=None):
        """
        Add a new location.

        :param location: Name of the new location
        :param lat: Latitude
        :param lng: Longitude
        """
        data = dict(
            {
                "location": location,
                "lat": lat,
                "lng": lng,
            }
        )
        return post(
            self.url,
            json=data,
            headers=self.headers,
            verify=self.verify,
        )

    def delete_location(self, location: str):
        """
        Deletes an existing location.

        :param location: Name of the location to delete
        """
        return delete(
            f"{self.url}/{location}",
            headers=self.headers,
            verify=self.verify,
        )

    def edit_location(self, location: str, lat=None, lng=None):
        """
        Edits a location.

        :param location: Name of the location to edit
        :param lat: Latitude
        :param lng: Longitude
        """
        data = dict(
            {
                "lat": lat,
                "lng": lng,
            }
        )
        return patch(
            f"{self.url}/{location}",
            json=data,
            headers=self.headers,
            verify=self.verify,
        )
