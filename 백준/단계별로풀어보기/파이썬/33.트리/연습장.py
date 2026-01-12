import sys

class ArrayBST:
    def __init__(self):
        self.tree = [None]
    
    def _ensure_size(self, idx):
        if idx >= len(self.len):
            self.tree.extend([None] * (idx-len(self.tree)+1))
    
    def insert(self, key):
        idx = 1
        while True:
            self._ensure_size(idx)
            
            if self.tree[idx] is None:
                self.tree[idx] = key
                return
            
            if key < self.tree[idx]:
                idx = idx * 2
            else:
                idx = idx * 2 + 1
    
    def search(self, key):
        idx = 1
        while idx < len(self.tree) and self.tree[idx] is not None:
            if self.tree[idx] == key:
                return True
            elif key < self.tree[idx]:
                idx = idx * 2
            else:
                idx = idx * 2 + 1
        return False
    
    def inorder(self):
        result = []
        
        def _inorder(idx):
            if idx >= len(self.tree) or self.tree[idx] is None:
                return
            _inorder(idx * 2)
            result.append(self.tree[idx])
            _inorder(idx * 2 + 1)
        _inorder(1)
        return result

if __name__ == "__main__":
    bst = ArrayBST()
    
    for x in [50,30,70,20,40,60,80]:
        bst.insert(x)
    
    print("Search 40:", bst.search(40))
    print("Search 100:", bst.search(100))
    print("Inorder:", bst.inorder())