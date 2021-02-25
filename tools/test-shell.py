# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

import json
from pprint import pprint
import sys

sys.path.insert(0, "..")

if sys.flags.interactive:
    import pyzohoapi
    import private
    td = private.testdata

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

    books = pyzohoapi.inventory.ZohoBooks(private.t['orgid'], private.t['region'], **private.t['api'])
    inv = pyzohoapi.inventory.ZohoInventory(private.t['orgid'], private.t['region'], **private.t['api'])

    print("\nTest shell loaded. Here's what you have:")
    print("\nModules: json;")
    print("\nFunctions:")
    print("\tpprint();")
    print("\tdump(object, key=None) -> dumps a Zoho Object (or optional attribute);")
    print("\nObjects:")
    print("\tprivate.testdata -> dict, aliased to td;")
    print("\tbooks -> ZohoBooks object : configured via testdata;")
    print("\tinv -> ZohoInventory object : configured via testdata;")
    print("Enjoy your testing!\n")

else:
    print("\nThis script bootstraps an interactive test enviroment, but only this way:")
    print(f"\t> python -i {__file__}")
    print("Otherwise, it's all for naught.\n")
