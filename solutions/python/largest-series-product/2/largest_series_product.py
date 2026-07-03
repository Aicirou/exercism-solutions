def largest_product(series, size):
    
    total = 0

    if (len(series) < size):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    
    for i in range(len(series) - size + 1):
        product = 1
        for j in range(i, i + size):
            product = int(series[j])*product
        print(product)
            
        total = max(total, product)
        
    return total
            
