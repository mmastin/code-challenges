# brute force
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i-1]) and a in B]

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] = k

    return [
        a for i, a in enumerate(A)
        if (i == 0 or a != A[i - 1]) and is_present(a)
    ]

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:  # A[i] > B[j]
            j += 1
    return intersection_A_B


