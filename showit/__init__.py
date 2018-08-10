import json
import os

from pkg_resources import resource_string

from .showit import (tile, image)

def get_version():
    try:
        # decode('utf-8') is used for python3.4, which reads all files as bytes.
        version_json = json.loads(
            resource_string(__name__, "VERSION").decode('utf-8'))
    except Exception as ex:
        raise ValueError("Cannot find VERSION file", ex)

    return version_json['string']

__version__ = get_version()
