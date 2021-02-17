# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

from importlib import reload
import json
from pprint import pprint
import sys

if sys.flags.interactive:
    import pyzohoapi
    import private

    def r():
        # reload(pyzohoapi)
        # reload(private)
        return pyzohoapi.inventory.ZohoInventory(private.t['orgid'], private.t['region'], **private.t['api'])

    def dump(o, key=None):
        if key:
            pprint(o._data.to_python().get(key), indent=2)
        else:
            for k, v in o._data.to_python().items():
                if isinstance(v, dict):
                    print(f"{k}: {{...}}")
                elif isinstance(v, list):
                    print(f"{k}: [...]")
                else:
                    print(f"{k}: {v}")

    print("\nTest shell loaded. Here's what you have:")
    print("\nModules: json;")
    print("\nFunctions:\n\tpprint();")
    # print("\tr() -> reloads modules, returns new 'z'")
    print("\nObjects:")
    print("\tprivate.testdata -> dict, aliased to private.t;")
    print("\tz -> ZohoInventory object : configured via testdata;")
    print("Enjoy your testing!\n")
    z = r()
else:
    print("\nThis script bootstraps an interactive test enviroment, but only this way:")
    print("\t> python -i run-me-interactively.py")
    print("Otherwise, it's all for naught.\n")
