def flatten(nested_list):
    null_values = (None, 'nil', 'null')
    flat_list = []
    for item in nested_list:
        if item in null_values:
            continue
        elif isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list