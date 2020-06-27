# reordering array so evens appear first, without additional
# storage allocation
def even_odd(A: List[int]) -> None:
    next_even, next_odd = 0, len(A-1)
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
        next_odd -= 1



RED, WHITE, BLUE = range(3)
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # first pass, group elements smaller than pivot
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # second pass, group elements larger than pivot
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

# to reduce time complexity:
def dutch_flag_partition_faster(pivot_index, A):
    pivot = A[pivot_index]

    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


def can_reach_end(A):
    furthest_reached_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reached_so_far and furthest_reached_so_far < last_index:
        furthest_reached_so_far = max(furthest_reached_so_far, A[i] + 1)
        i += 1
    return furthest_reached_so_far >= last_index


# returns number of valid entries after deletion
def delete_duplicates(A):
    if not A:
        return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

    