import math
def score(x, y):
    Inner_Radius = 1
    Middle_Radius = 5
    Outer_Radius = 10
    distance = math.sqrt(x ** 2 + y ** 2)
    if distance <=Inner_Radius: return 10
    if distance <=Middle_Radius: return 5
    if distance <= Outer_Radius: return 1
    return 0
        
    
            
        
            
        
        
    
