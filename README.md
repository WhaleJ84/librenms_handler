# LibreNMS handler

[![PyPI](https://img.shields.io/pypi/v/librenms-handler.svg)](https://pypi.python.org/pypi/librenms-handler)
[![image](https://img.shields.io/pypi/pyversions/librenms-handler.svg)](https://python.org/pypi/librenms-handler)
[![Downloads](https://pepy.tech/badge/librenms-handler)](https://pepy.tech/project/librenms-handler)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Bandit](https://github.com/WhaleJ84/librenms_handler/actions/workflows/bandit.yml/badge.svg)](https://github.com/WhaleJ84/librenms_handler/actions/workflows/bandit.yml)
[![CodeQL](https://github.com/WhaleJ84/librenms_handler/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/WhaleJ84/librenms_handler/actions/workflows/codeql-analysis.yml)

A Python library to interact with the LibreNMS API (v0).

The project aims to provide the user with as much information as if they were looking at the [reference guide](https://docs.librenms.org/API/) themselves.

I have not used it myself so I cannot endorse it, but a quick search shows that [LibreNMSAPI](https://github.com/RobertH1993/LibreNMSAPI) has a similar goal with a different outlook.
Consider checking it out if this project doesn't suit your needs!

## Usage

The package is installed with the following package managers like so:

### Pip

`pip install librenms-handler`

### Pipenv

`pipenv install librenms-handler`

The following statement will initialise the chosen endpoint:

```python
from librenms_handler.devices import Devices

devices = Devices(
    'https://librenms.example.com',
    'e4ef9234abab59a90628dd3f616a60b4'
)
```

**NOTE:** If you are using a self-signed certificate for your server, you can bypass the errors by passing the initialisation option `verify=False`.

Once done, a list of methods will be available to you such as `devices.list_devices()`.
Upon operation, the method will execute and return the required request to your LibreNMS instance.

```
>>> devices.add_device('test_device', snmp_disable=True, force_add=True)
{'status': 'ok', 'message': 'Device test_device (13) has been added successfully'}
>>> devices.del_device('test')
{'status': 'ok', 'devices': [{'device_id': 13, 'inserted': '2021-03-13 15:56:19', 'hostname': 'test_device', 'sysName': '', 'ip': None, 'overwrite_ip': None, 'community': '', 'authlevel': None, 'authname': None, 'authpass': None, 'authalgo': None, 'cryptopass': None, 'cryptoalgo': None, 'snmpver': 'v2c', 'port': 161, 'transport': 'udp', 'timeout': None, 'retries': None, 'snmp_disable': 1, 'bgpLocalAs': None, 'sysObjectID': None, 'sysDescr': None, 'sysContact': None, 'version': None, 'hardware': '', 'features': None, 'location_id': None, 'os': 'ping', 'status': True, 'status_reason': '', 'ignore': 0, 'disabled': 0, 'uptime': None, 'agent_uptime': 0, 'last_polled': None, 'last_poll_attempted': None, 'last_polled_timetaken': None, 'last_discovered_timetaken': None, 'last_discovered': None, 'last_ping': None, 'last_ping_timetaken': None, 'purpose': None, 'type': 'server', 'serial': None, 'icon': 'images/os/ping.svg', 'poller_group': 0, 'override_sysLocation': 0, 'notes': None, 'port_association_mode': 1, 'max_depth': 0, 'disable_notify': 0, 'location': None, 'lat': None, 'lng': None, 'attribs': [], 'vrf_lite_cisco': []}], 'message': 'Removed device test_device\n', 'count': 1}
```

The output is exactly the same as if you were using Curl to make the requests.

Should you wish to use any other endpoint, the situation would be the same: `from librenms_handler.endpoint import Endpoint`

## Environment variables

While initialising the handler, the following parameters are required.
The handler first checks for the following environment variables, should you choose to use them.

| Environment variable | Description | Type | Example |
| -------------------- | ----------- | ---- | ------- |
| LIBRENMS_URL         | Full URL to the target LibreNMS instance | string | https://librenms.example.com |
| LIBRENMS_TOKEN       | Token generated from `LIBRENMS_URL/api-access` | string | e4ef9234abab59a90628dd3f616a60b4 |

## Endpoints

The progress of API endpoints are shown in their respective projects below:
See [Projects](https://github.com/WhaleJ84/librenms_handler/projects) to track the progress of the endpoints or select individual ones below.

It is not possible to say when an endpoint is 'done', as they are being expanded as time goes on.
Each function will have its own issue tracked, so you can search to see if implemented or not.

| Endpoint                                                                 | Started |
| ------------------------------------------------------------------------ | ------- |
| [Alerts](https://github.com/WhaleJ84/librenms_handler/projects/5)        | False   |
| [ARP](https://github.com/WhaleJ84/librenms_handler/projects/10)          | True    |
| [Bills](https://github.com/WhaleJ84/librenms_handler/projects/9)         | False   |
| [Device Groups](https://github.com/WhaleJ84/librenms_handler/projects/2) | True    |
| [Devices](https://github.com/WhaleJ84/librenms_handler/projects/1)       | True    |
| [Inventory](https://github.com/WhaleJ84/librenms_handler/projects/8)     | True    |
| [Locations](https://github.com/WhaleJ84/librenms_handler/projects/14)    | True    |
| [Logs](https://github.com/WhaleJ84/librenms_handler/projects/13)         | True    |
| [Port Groups](https://github.com/WhaleJ84/librenms_handler/projects/4)   | False   |
| [Ports](https://github.com/WhaleJ84/librenms_handler/projects/3)         | False   |
| [Routing](https://github.com/WhaleJ84/librenms_handler/projects/6)       | False   |
| [Services](https://github.com/WhaleJ84/librenms_handler/projects/11)     | False   |
| [Switching](https://github.com/WhaleJ84/librenms_handler/projects/7)     | True    |
| [System](https://github.com/WhaleJ84/librenms_handler/projects/12)       | True    | 

## Collaboration

The project has no complex logic behind it - all you need to do is read the [API docs](https://docs.librenms.org/API/) and follow the existing code structure.
Sometimes the documentation is not consistent, so providing more information in the docstring is preferred than not explaining arguments.

All code should be formatted by [Black](https://github.com/psf/black) before submission and adhere to [Pylint](https://github.com/PyCQA/pylint) recommendations where reasonable.
Linting is not absolute; functionality is the priority.

By following these standards, the code should be easy for people from all skill-sets to help out!
