from Tree import Tree
class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    
    #------------------------ additional abstract methods --------------------------------
    def left(self, p):
        """Return a Position representing p's left child.
        
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclasses')
    
    def right(self, p):
        """Return a Position representing p's right child.
        
        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclasses')
    
    # ------------------------ concrete methods implemented in this class ---------------
    def sibling(self, p):
        """ Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                                 # p must be the root
            return None                                    # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)                  # can be None
            else :
                return self.left(parent)                   # can be None
            
    def children(self, p):
        """Geenerate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # ------------------------- traversal method (inorder by default) -------------------
    def positions(self):
        """ method overriden from the parent to make inorder traversal as default traversal method."""
        return self.inorder()                              # make inorder default
    