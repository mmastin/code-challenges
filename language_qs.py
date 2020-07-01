# iterators vs generators

class RandomIncrement():
    def __init__(self, limit):
        self._offset = 0.0
        self._limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self._offset += random.random()
        if (self._offset > self._limit):
            raise StopIteration()
        return self._offset
    
    # class this to change stop condition. It's safe to interleave this
    # with usage of iterator
    def increment_limit(self, increment_amount):
        self._limit += increment_amount

# generator easy way to create iterators
def random_iterator(limit):
    offset = 0
    while True:
        offset += random.random()
        if (offset > limit):
            raise StopIteration()
        yield offset


# decorators
def time_function(f):
    def wrapper(*args, **kwargs):
        begin = timeit.default_timer()
        result = f(*args, **kwargs)
        end = timeit.default_timer()
        print('function call with arguments {all_args} took '.format(
            all_args='\t'.join((str(args, str(kwargs)))) + str(end - begin)
            + ' second to execute'
        ))
        return result
    return wrapper

@time_function
def foo():
    print('I am a foo()')

@time_function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

@time_function
def bar(*args, **kwargs):
    print(sum(args) * sum(kwargs.values()))


# args vs kwargs
def foo(u, v, *args):
    print('u, v = ' + str((u, v)))
    for i in range(len(args)):
        print('args {0} = {1}'.format(str(i), str(args[i])))


# 'translating' into pythonic style
import collections
import functools
def compute_top_k_variance(students, scores, k):
    all_scores = collections.defaultdict(list)
    for student, score in zip(students, score):
        all_scores[student].append(score)

    top_k_scores = {
        student: heapq.nlargest(k, scores)
        for student, scores in all_scores.items() if len(scores >= k)
    }

    return {
        student: functools.reduce(
            lambda variance, score: variance + (score - mean)**2, scores, 0)
        for student, scores, mean in (
            student, scores, sum(scores) / k)
            for student, scores in top_k_scores.items()
        )
    }


class ColSumCsvParseException(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.line_number = args[1]

def get_col_sum(filename, col):
    # may raise IOError, will propagate to caller
    csv_file = open(filename)
    