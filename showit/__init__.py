import json
import os
from .showit import (tile, image)

def get_version():
    version_json = None
    dirname = os.path.dirname(__file__)
    for candidatepath in (
            [dirname, ".."], # this is the non-installed path
            [dirname, "..", "..", "..", "..", "share", "showit"],
            ):
        try:
            candidatepath.append("VERSION")
            with open(os.path.join(*candidatepath), "r") as fh:
                version_json = json.loads(fh.read())
        except (IOError, OSError):
            pass

    if version_json is None:
        raise ValueError("Cannot find VERSION file")

    return version_json['string']

__version__ = get_version()
