# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

import json
from pprint import pprint
import sys

if sys.flags.interactive:
    from pyzohoapi.inventory import ZohoInventory
    from pyzohoapi.exceptions import *
    from private import testdata

    z = ZohoInventory(testdata['orgid'], testdata['region'], **testdata['api'])

    print("\nTest shell loaded. Here's what you have:")
    print("\nModules: json, ZohoException (and subclasses);")
    print("\nFunctions: pprint();")
    print("\nObjects:")
    print("\ttestdata -> dict : loaded from the 'private' module;")
    print("\tz -> ZohoInventory object : configured via testdata;")
    print("Enjoy your testing!\n")
else:
    print("\nThis script bootstraps an interactive test enviroment, but only this way:")
    print("\t> python -i run-me-interactively.py")
    print("Otherwise, it's all for naught.\n")
