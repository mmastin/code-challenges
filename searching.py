def search_first_key(A: List[int], k: int) -> int:
    left, right, result = 0, len(A - 1), -1
    #A[left:right + 1] is the candidate set
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else: #a[mid] < k
            left = mid + 1
    return result


def search_entry_equal_to_index(A: List[int]) -> int:
    left, right = 0, len(A - 1)
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else:
            left = mid + 1

    return -1

import collections
MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))

def find_min_max(A: list[int]) -> MinMax:
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)

    if len(A) <= 1:
        return MinMax(A[0], A[0])

    global_min_max = min_max(A[0], A[1])
    # process two elements at a time
    for i in range(2, len(A) - 1, 2):
        local_min_max = min_max(A[i], A[i + 1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest)
        )

    # if there is odd number of elements in array, still need to
    # compare the last element with the existing answer
    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )

    return global_min_max


import itertools
def find_missing_element(stream: Iterator[int]) -> int:
    num_bucket = 1 << 16
    counter = [0] * num_bucket
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part_x = x >> 16
        counter[cupper_part_x] += 1

    # look for a bucket that contains less than (1 << 16) elements
    bucket_capacity = 1 << 16
    candidate_bucket = next(
        i for i, c in enumerate(counter) if c < bucket_capacity
    )

    # finds all IP addressses in the stream whose first 16 bits are equal
    # to candidate bucket
    candidates = [0] * bucket_capacity
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # records the presence of 16 LSB of x
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1

    # at least one of the LSB combos is absent, find it
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidates_bucket << 16) | i


# DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
#     ('duplicate', 'missing'))
# def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
#     # compute the xor of all numbers from 0 to |A| - 1 and all entries in A
#     miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1],
#         enumerate(A), 0)

    