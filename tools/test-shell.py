# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

import json
from pprint import pprint
import sys

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

    books = pyzohoapi.books.ZohoBooks(td['orgid'], td['region'], **td['api'])
    inv = pyzohoapi.inventory.ZohoInventory(td['orgid'], td['region'], **td['api'])

    print("\nTest shell loaded. Here's what you have:")
    print("\nModules:\n\tjson;")
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
