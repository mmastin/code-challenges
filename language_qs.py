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
    csv_reader = csv.reader(csv_file)
    running_sum = line_number = 0
    try:
        for row in csv_reader:
            if col >= len(row):
                raise IndexError('not enough entries in row ' + str(row))
            value = row[col]
            # will skip rows for which the corresponding columns can't
            # be parsed to an int, logging the fact
            try:
                running_sum += int(value)
            except ValueError:
                print('cannot convert ' + value + 'to int, ignoring')
            line_number += 1
    except csv.Error:
        # program should raise exceptions appropriate to their level of
        # abstraction, so we propagate the csv.Error upwards as a 
        # ColSumCsvParseException
        print('in csv.Error handler')
        raise ColSumCsvParseException('error processing csv', line_number)
    else:
        print('sum = ' + str(running_sum))
    finally:
        # ensure there is no resource leak
        csv_file.close()
        return running_sum


# Scoping
x, y, z = 'global-x', 'global-y', 'global-z'

def basic_scoping():
    print(x) # global x
    y = 'local-y'
    global z
    z = 'local-z'

def inner_outer_scoping():
    def inner1():
        print(x) # outer-x

    def inner2():
        x = 'inner2-x'
        print(x) # inner2-x

    def inner3():
        nonlocal x
        x = 'inner3-x'
        print(x) # inner3-x

    x = 'outer-x'
    # inner1(), inner2(), inner3()