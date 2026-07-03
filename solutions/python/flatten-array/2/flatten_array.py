def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if item is None:
            continue
        elif isinstance(item, (tuple, list)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


