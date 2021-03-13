# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

def diff(orig, new):
    """ Calculates the difference between two dictionaries.

    Any key with a child list or dict which is, itself, changed will be
    considered changed.

    :param orig: the original (unmodified) dictionary
    :param new: the modified dictionary
    :return: a dictionary contianing only those keys which were changed.
    """
    updated = {}
    for k, v in new.items():
        if k not in orig:
            updated[k] = v
        elif isinstance(v, list):
            if len(v) != len(orig[k]):
                updated[k] = v
            else:
                has_change = False
                for i in range(len(v)):
                    if isinstance(v[i], dict) and diff(orig[k][i], v[i]):
                        has_change = True
                        break
                    elif v[i] != orig[k][i]:
                        has_change = True
                        break
                if has_change:
                    # the update needs to contain the ENTIRE new list, so
                    # Zoho doesn't zap non-updated elements
                    updated[k] = v
        elif isinstance(v, dict):
            if diff(v, orig[k]):
                # the update needs to contain the ENTIRE new dict, so
                # Zoho doesn't zap non-updated values
                updated[k] = v
        elif v != orig[k]:
            updated[k] = v
    return updated
