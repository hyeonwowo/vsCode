class Player:
    def __init__(self,name,pos,ovl):
        self.name = name
        self.pos = pos
        self.ovl = ovl
    
    def print_stat(self):
        print(f"{self.name} {self.pos} {self.ovl}")
    
    def update_info(self,pos):
        print(f"{self.pos} -> {pos}")
        self.pos = pos


Son = Player("SON","LW",92)
Kane = Player("KANE","ST",93)
Kross = Player("KROSS","MF",90)

Son.print_stat()
Kane.print_stat()
Kross.print_stat()
print()

Son.update_info("RW")
Son.print_stat()