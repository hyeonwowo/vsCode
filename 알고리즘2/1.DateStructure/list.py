class List:
    def __init__(self):
        self.List = []

    def insertFirst(self, element):
        self.List.insert(0,element)

    def insertLast(self, element):
        self.List.append(element)

    def deleteFirst(self):
        del self.List[0]

    def deleteLast(self):
        del self.List[-1]

    def deleteElement(self,element):
        self.List.remove(element)

    def printList(self):
        result = " -> ".join(map(str,self.List))
        print(result)

def printOption():
    print("1. insert First")
    print("2. insert Last")
    print("3. delete First")
    print("4. delete Last")
    print("5. delete Element")
    print("6. print List")
    print("7. EXIT")

if __name__ == "__main__":
    LinkedList = List()

    printOption()
    while(1):
        option = int(input("type option >> "))
        if option == 1:
            print("Insert First")
            element = int(input("type element >> "))
            LinkedList.insertFirst(element)

        elif option == 2:
            print("Insert Last")
            element = int(input("type element >> "))
            LinkedList.insertLast(element)

        elif option == 3:
            print("Delete First")
            LinkedList.deleteFirst()

        elif option == 4:
            print("Delete Last")
            LinkedList.deleteLast()

        elif option == 5:
            print("Delete Element")
            element = int(input("type element >> "))
            LinkedList.deleteElement(element)

        elif option == 6:
            print("Print List")
            LinkedList.printList()

        elif option == 7:
            print("QUIT")
            break

        else:
            print("Invaild option.. choose again.") 
        
    print("ListResult : ")
    LinkedList.printList()
    

        