up = [1,2,4,5,6,8,9,10,20]
down = [15,3,2,1,0]

new = []

upmax = up[-1]
downmax = down[0]

if upmax == downmax:
    up.pop()
    new = up + down
else:
    new = up + down
    
print(new)