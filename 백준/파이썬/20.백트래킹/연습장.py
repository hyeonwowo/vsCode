numbers = [1,2,3]
path = []

def backtrack():
    if len(path) == 2:
        print(path)
        return
    for element in numbers:
        if element not in path:
            path.append(element)
            backtrack()
            path.pop()
            
backtrack()