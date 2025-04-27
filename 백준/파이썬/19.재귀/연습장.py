import sys

def draw_star(n):
    if n == 3: return "***\n* *\n***"
    else:
        prev = draw_star(3 ** n-1)
        new = ""
    
        # top
        for _ in range(3):
            new += prev * 3
        
        # middle
        new += prev
        new += " " * 3
        new += prev
        
        # bottom
        for _ in range(3):
            new += prev * 3
            
        return new
if __name__ == "__main__":
    print(draw_star(int(input())))