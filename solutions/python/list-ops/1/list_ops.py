def append(list1, list2):
    return list1 + list2


def concat(lists):
    result=[]
    for list in lists:
        result+=list
    return result


def filter(func, list):
    result=[]
    for item in list:
        if func(item):
            result.append(item)
    return result


def length(list):
    count=0
    for _ in list:
        count+=1
    return count


def map(func, list):
    result=[]
    for item in list:
        result.append(func(item))
    return result


def foldl(func, list, init_accum):
    for item in list:
        init_accum = func(init_accum, item) 
    return init_accum


def foldr(func, list, init_accum):
    for item in list[::-1]: #reversed
        init_accum = func(init_accum, item) 
    return init_accum


def reverse(list):
    return list[::-1] #reversed
