# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

from decimal import Decimal
import simplejson as json
from pprint import pprint
import sys

if sys.flags.interactive:
    import pyzohoapi
    import private
    td = private.testdata

    def testshell():
        """Test shell loaded. Here's what you have:

        Modules:
            decimal.Decimal (as Decimal);
            json (simplejson, aliased to json);

        Functions:
            pprint();
            show(object, key=None) -> shows a Zoho Object (or optional attribute);

        Objects:
            private.testdata -> dict, aliased to td;
            books -> ZohoBooks object : configured via testdata;
            inv -> ZohoInventory object : configured via testdata;

        Type `help(testshell)` to get this help again.

        Enjoy your testing!
        """
        ...

    def show(o, key=None):
        """ Shows all of a Zoho object's attributes, or the attribute specified.
        You can use dotted notation to drill down into attributes.
        """
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

    help(testshell)
else:
    print("\nThis script bootstraps an interactive test enviroment, but only this way:")
    print(f"\t> python -i {__file__}")
    print("Otherwise, it's all for naught.\n")
