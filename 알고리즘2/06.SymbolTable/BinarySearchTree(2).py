

if __name__ == "__main__":   
    bst = BST() 
    print(bst.size())
    print("min", bst.min())
    print("max", bst.max())

    bst.put("a",1)
    bst.put("c",2)
    bst.put("e",3)
    bst.put("b",4)
    bst.put("c",5)
    print(bst.size())

    print(bst.get("a"))
    print(bst.get("b"))
    print(bst.get("c"))
    print(bst.get("d"))
    print(bst.get("e"))
    print(bst.floor("a"))
    print(bst.floor("b"))   

    print("ceiling") 
    print(bst.ceiling("a"))
    print(bst.ceiling("b"))
    print(bst.ceiling("c"))
    print(bst.ceiling("d"))
    print(bst.ceiling("e"))
    print(bst.ceiling("f"))

    print("min", bst.min())
    print("max", bst.max())

    print("rank")
    print(bst.rank("a"))
    print(bst.rank("b"))
    print(bst.rank("c"))
    print(bst.rank("d"))
    print(bst.rank("e"))
    print(bst.rank("f"))

    print("select")
    print(bst.select(-1))
    print(bst.select(0))
    print(bst.select(1))
    print(bst.select(2))
    print(bst.select(3))
    print(bst.select(4))
    print(bst.select(5))
    print(bst.select(6))

    print("inorder traversal")
    bst2 = BST()
    bst2.put("S",1)
    bst2.put("E",2)
    bst2.put("Y",3)
    bst2.put("A",4)
    bst2.put("R",5)
    bst2.put("C",6)
    bst2.put("H",7)
    bst2.put("M",8)
    for k in bst2.inorder():
        print(k)
    print(bst2.rank("H"))
    print(bst2.select(4))

    print("delete")
    bst2.delete("C")
    print(bst2.inorder())   
    
    bst2.delete("E")
    print(bst2.inorder())   

    bst2.delete("Y")
    print(bst2.inorder())   

    bst2.delete("S")
    print(bst2.inorder())   

    bst2.delete("F") # Delete a key not in BST, so BST remains the same
    print(bst2.inorder())   


