"""Includes all the methods available to the base class."""
import logging
from os import getenv


class LibreNMS:  # pylint: disable=R0903
    """Includes all the methods available to the base class."""

    def __init__(self, url, token, verify=True):
        self.url = getenv("LIBRENMS_URL") or url
        self.token = getenv("LIBRENMS_TOKEN") or token
        self.verify = verify
        self.headers = dict({"X-Auth-Token": self.token})
        logging.basicConfig(level=logging.DEBUG)
