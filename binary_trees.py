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


