from typing import Any, Generator, Tuple

from tree_node import TreeNode


class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.
        
        Raises:
            ValueError: root is not a TreeNode or not None.
        """

        #if root is TreeNode and root is not None:
            #raise ValueError('root is not a TreeNode or it is not None')

        self._root = root
        self._size = 0 if root is None else 1

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        if not isinstance(key, int):
            raise ValueError('Key is not an integer')

        prev_node = self._root
        tmp_node = self._root

        while True:
            if self._root is None:
                self._root = TreeNode(key, value, None, None, None)
                self._size = 1
                break
            else:
                if tmp_node is None:
                    if prev_node.key < key:
                        prev_node.right = TreeNode(key, value, None, None, prev_node)
                    elif prev_node.key > key:
                        prev_node.left = TreeNode(key, value, None, None, prev_node)
                    self._size += 1
                    break
                prev_node = tmp_node
                if key > tmp_node.key:
                    tmp_node = tmp_node.right
                elif key < tmp_node.key:
                    tmp_node = tmp_node.left
                elif tmp_node.key == key:
                    raise KeyError('Key is already present in the tree!')

    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        if not isinstance(key, int):
            raise ValueError('Key is not an integer.')

        tmp = self._root

        while True:
            if tmp is None:
                raise KeyError('Key is not present in the tree')
            elif tmp.key == key:
                return tmp
            elif tmp.key < key:
                tmp = tmp.right
            elif tmp.key > key:
                tmp = tmp.left

    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""
        return self._size

    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        if not isinstance(key, int):
            raise ValueError('Key is not an integer')

        self._size -= 1
        tmp_node = self._root
        prev_node = self._root

        node = self.find(key)

        if node.right is None and node.left is None:
            node.parent = None


    # Hint: The following 3 methods can be implemented recursively, and 
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here: 
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())

        if node:
            yield from self._inorder(node)

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())

        yield self._root

        tmp = self._root.left

        while True:
            if tmp is not None:
                yield tmp

            if tmp is None:
                break

            if tmp.left is None:
                tmp = tmp.right
            else:
                tmp = tmp.left

        tmp = self._root.right
        right = None

        while True:
            if tmp is not None:
                yield tmp

            if tmp is None:
                yield right
                break

            if tmp.left is None:
                tmp = tmp.right
            else:
                right = tmp.right
                tmp = tmp.left



    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())

        if node:
            yield from self._postorder(node)

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]:
        yield from self._preorder(self._root)

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""
        pass
        # TODO

    def return_min_key(self) -> TreeNode:
        """Return the node with the smallest key (None if tree is empty)."""
        if self._root is None:
            return None

        #small = self._root.key
        tmp = self._root

        while True:
            if tmp.left is None:
                return tmp
            tmp = tmp.left

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        python_list = list(node.key for node in self._preorder())
        # TODO

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})"

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self, current_node):
        if current_node:
            yield from self._inorder(current_node.left)
            yield current_node
            yield from self._inorder(current_node.right)

    def _preorder(self, current_node):
        self.preorder(current_node)

    def _postorder(self, current_node):
        if current_node:
            yield from self._postorder(current_node.left)
            yield from self._postorder(current_node.right)
            yield current_node

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)
