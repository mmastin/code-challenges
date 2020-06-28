def print_linked_list_in_reverse(head: ListNode):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())


class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
                                                ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        self._element_with_cached_max[-1].max

    def pop(self):
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x
                if self.empty() else max(x, self.max()))
        )


def is_well_formed(s):
    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.apend(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            # unmatched right char or mismatched
            return False
    return not left_chars


class Queue:
    def __init__(self):
        self._data = collections.dequeue()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)


def binary_tree_depth_order(tree) -> List[List[int]]:
    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child for curr in curr_depth_nodes
            for child in (curr.left, curr.right) if child
        ]

    return result