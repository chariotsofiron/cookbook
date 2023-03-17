def flatten_json(y, prefix=""):
    """flatten json/dict containing inner dicts and lists"""
    out = {}

    def flatten(element, name=""):
        if isinstance(element, dict):
            for a in element:
                flatten(element[a], name + a + "_")
        elif isinstance(element, list):
            for i, a in enumerate(element):
                flatten(a, name + str(i) + "_")
        else:
            out[name[:-1]] = element

    flatten(y, prefix)
    return out
