def divisible_by_3(number):
    return number % 3 == 0

def divisible_by_5(number):
    return number % 5 == 0

def divisible_by_7(number):
    return number % 7 == 0

def convert(number):
    tempString = ""
    if divisible_by_3(number): tempString += "Pling"
    if divisible_by_5(number): tempString += "Plang"
    if divisible_by_7(number): tempString += "Plong"
    return str(number) if tempString == "" else tempString
        
    
    