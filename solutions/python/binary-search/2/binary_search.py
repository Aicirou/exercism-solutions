def find(search_list, value):
    search_list.sort()
    low, high = 0, len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] == value:
            return mid
        low, high = (mid+1, high) if search_list[mid] < value else (low, mid - 1)

    raise ValueError("value not in array")