import collections

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.napedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                and check_symmetric(subtree_0.left, subtree_1.right)
                and check_symmetric(subtree_0.right, subtree_1.left))
        # one subtree empty, and the other is not
        return False

    return not tree or check_symmetric(tree.left, tree.right)


