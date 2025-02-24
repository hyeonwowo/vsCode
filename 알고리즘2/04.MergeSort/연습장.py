points = [(0,0),(1,2),(2,2),(3,7),(4,10),(5,0)]
result = []

for point in points:
    slopes = []
    for other in points:
        if other == point:
            continue
        
        if other[0]-point[0] == 0:
            slope = float('inf')
        else:
            slope = (other[1] - point[1]) / (other[0] - point[0]) 
        slopes.append((slope,other))
    result.append((point, slopes))
         
print(result)