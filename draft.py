'''cs61a draft'''
from operator import sub, mul, add
from functools import reduce

'''def two_of_three(i, j, k):
    return i*i + j*j + k*k - max(i, j, k)*max(i, j, k)

print(two_of_three(1, 2, 3))'''


'''def largest_factor(s):    
    m = s - 1
    while True:
        if s % m == 0:
            return m
        else:
            m -= 1

print(largest_factor(20))'''


'''def hailstone(s):
    count = 0
    while s != 1:
        if s % 2 == 0:
            s = s // 2
            print(s)
            count += 1
        else:
            s = s * 3 + 1
            print(s)
            count += 1
    count += 1
    return count

print(hailstone(int(input())))'''


'''debug = True

# >>>>>>>>DEBUG<<<<<<<<<

def foo(s):
    i = 0
    while i < s:
        i += func(i)
        if debug:
            print("DEBUG: i is", i)'''



'''def falling(s, k):
    i = 0
    result = 1

    if k == 0:
        return 1
    
    while i < k:
        result = s * result
        s -= 1
        i += 1
    
    return result

print(falling(6, 3))'''


'''def digit(s, k):
    if k > len(str(s)):
        return 0
    
    return ((s // pow(10, k) % 10))'''


'''def middle(a, b, c):
    mid = a*a + b*b + c*c - pow(max(a, b, c), 2) - pow(min(a, b, c), 2)
    mid = int(mid ** 0.5)
    return mid

print(middle(20, 99 ,1))'''


'''def falling(s, k):
    count = 1
    result = 1
    
    if k == 0:
        return 1
    
    while count <= k:
        result *= s
        s -= 1
        count += 1
    
    return result

print(falling(28, 9))'''


'''def divisible_by_k(s, k):
    count = 0
    i = 1

    if k > s:
        return 0
    
    while i <= s:
        if i % k == 0:
            print(i)
            count += 1
        i += 1

    return count

print(divisible_by_k(10, 2))'''


'''def sum_digits(y):
    lst = []
    k = str(y)
    for num in k:
        lst.append(int(num))
    
    return sum(lst)

print(sum_digits(1321))'''


'''def double_eights(s):
    str_n = str(s)
    count = str_n.count("8")
    
    if count >= 2:
        return True
    else:
        return False

print(double_eights(808))'''


'''def prime_factor(s):
    while s > 1:
        k = smallest_prime_factor(s)
        s = s // k
        print(k)

def smallest_prime_factor(s):
    k = 2
    while s % k != 0:
        k += 1
    return k'''


'''pi = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
str_pi = str(pi)
print(pi // pow(10, (100 - 29)) % 10)
print(str_pi[29])'''

'''big = 36
small = 24
for i in range(small, 9, -1):
                if big % i == 0 and small % i == 0:
                    gcd = i
print(gcd)'''


'''pi = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
pi = pi // pow(10, (100 - 80)) % 10
#print(pi % 10 + 3)
#print(max((83 // 10) - 4, 0))'''


'''def sum_naturals(s):
    total, k = 0, 1
    while k <= s:
        total, k = total + k, k + 1
    return total

def summation(s, trem):
    total, k = 0, 1
    while k <= s:
        total, k = total + trem(k), k + 1
    return total

def cube(k):
    return k*k*k

def identity(k):
    return k

print(summation(2, identity))'''


'''def square(x):
    return x * x

def make_adder(s):
    def adder(k):
        return k + s
    return adder

def compose(f, g):
    def h(x):
        return f(g(x))
    return h

print(compose(square, make_adder(2))(3))'''


'''def view(re):
    ice = 4
    def k(means):
        return re(means)
    return k

def review(pr):
    return re(pr * 2)

ice = 3
re = view(lambda pr: pr * ice)
review(1)'''


'''def remove(s, digit):
    kept, digits = 0, 0
    while s > 0:
        s, last = s // 10, s % 10
        if last != digit:
            kept = kept + last*10**digits
            digits += 1
    return kept

print(remove(231, 3))'''


'''def sum_digits(s):
    if s < 10:
        return s
    else:
        all_but_last, last = s // 10, s % 10
        return sum_digits(all_but_last) + last

print(sum_digits(18117))'''


'''def is_even(s):
    if s == 0:
        return True
    else:
        return is_odd(s - 1)
    
def is_odd(s):
    if s == 0:
        return False
    else:
        return is_even(s - 1)
    
#print((is_odd(3)))'''


'''def cascade(s):
    print(s)
    if s >= 10:
        cascade(s//10)
        print(s)

cascade(2012)'''


'''def play_alice(s):
    if s == 0:
        print('bob wins')
    else:
        return play_bob(s - 1)
    
def play_bob(s):
    if s == 0:
        print('alice wins!')
    elif is_even(s):
        play_alice(s - 2)
    else:
        play_alice(s - 1)

play_alice(20)
play_alice(11)'''


'''def fib(s):
    if s == 0:
        return 0
    if s == 1:
        return 1
    else:
        return fib(s - 2) + fib(s - 1)

print(fib(10))

def fib_itr(s):
    if s == 1:
        return 1
    prev, cur = 0, 1
    for _ in range(s - 1):
        prev, cur = cur, prev + cur
    return cur

print(fib_itr(10))'''


'''def count_partitions(s, m):
    if s < 0:
        return 0
    elif s == 0:
        return 1
    elif m == 0:
        return  0
    else:
        return count_partitions(s-m, m) + count_partitions(s, m-1)
    
print(count_partitions(20, 4))'''


'''def factorial(s):
    fact = 1
    i = 1
    while i <= s:
        fact *= i
        i += 1
    return fact

print(factorial(3))

def factorial_rec(s):
    if s == 0:
        return 1
    else:
        return s * factorial_rec(s - 1)

print(factorial_rec(3))'''


'''def cascade(s):
    if s < 10:
        print(s)
    else:
        print(s)
        cascade(s//10)
        print(s)

cascade(1234)


def inverse_cascade(s):
    grow(s)
    print(s)
    shrink(s)

def f_then_g(f, g, s):
    if s:
        f(s)
        g(s)

grow = lambda s: f_then_g(grow, print, s//10)
shrink = lambda s: f_then_g(print, shrink, s//10)

inverse_cascade(1234)'''


'''def move_disk(disk_number, from_peg, to_peg):
    print("Move disk" + str(disk_number) + " from peg"\
          + str(from_peg) + " to peg" + str(to_peg) + ".")


def solve_hanoi(s, start_peg, end_peg):
    if s == 1:
        move_disk(s, start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        solve_hanoi(s - 1, start_peg, spare_peg)
        move_disk(s, start_peg, end_peg)
        solve_hanoi(s - 1, spare_peg, end_peg)

solve_hanoi(2, 2, 1)'''


'''def pingpong_itr(s):
    index, ppn, dir = 1, 1, 1
    while index < s:
        index += 1
        ppn += dir
        if index % 10 == 8 or index % 8 == 0:
            dir = -dir
        print(index, "ppn", ppn)
    return ppn

pingpong_itr(33)'''


'''def num_eights(x):
    if x % 10 == 8:
         return 1 + num_eights(x//10)
    elif x < 10:
         return 0
    else:
         return num_eights(x//10)'''


'''def pingpong(s):
    def helper(i, ppn, dir):
        if i == s:
               return ppn
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(i+1, ppn-dir, -dir)
        else:
            return helper(i+1, ppn+dir, dir)
    return helper(1, 1, 1)

print(pingpong(9))'''


'''def missing_digits(s):
    if s < 10:
        return 0
    else:
        last, rest = s % 10, s // 10
        return max(last - rest % 10 - 1, 0) + missing_digits(rest)

print(missing_digits(1239))'''


'''def make_anonymous_factorial():
    return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))

print(make_anonymous_factorial()(6))


def fact(s):
    if s == 1:
        return 1
    else:
        return s * fact(s - 1)

print(fact(6))'''


'''def mysum(L):
    total = 0
    for num in L:
        total += num
    return total

print(mysum([2, 3, 4]))

def mysum_rec(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum_rec([2, 3, 4]))'''


'''def sum_itr(s):
    total = 0
    for i in range(s+1):
        total += i
    return total

print(sum_itr(5))


def sum_rec(s):
    if s == 0:
        return 0
    else:
        return s + sum_rec(s-1)

print(sum_rec(5))'''


'''def reverse_itr(s):
    reversed_word = ""
    for i in s:
        reversed_word = i + reversed_word
    return reversed_word

print(reverse_itr("word"))


def reverse_rec(s):
    if len(s) == 1:
        return s
    else:
        return reverse_rec(s[1:]) + s[0]

print(reverse_rec("word"))'''


'''def fact(s):
    def fact_helper(k, result):
        if k > s:
            return result 
        else:
            return fact_helper(k + 1, result * k)
    return fact_helper(1, 1)

print(fact(3))
print(fact(5))
print(fact(4))'''


'''def max_subseq(s, t):
    if s == 0 or t == 0:
        return 0
    else:
        with_last = max_subseq(s//10, t-1) * 10 + s%10
        without_last = max_subseq(s//10, t)
        return max(with_last, without_last)

print(max_subseq(78781124, 4))'''


'''def count_leaves(t):
    assert is_tree(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

count_leaves(tree(3, [tree(2)]))'''


'''def fact(s):
    if s == 0:
        return 1
    else:
        return s * fact(s - 1)
    

def fact_times(s, k):
    if s == 0:
        return k
    else:
        return fact_times(s - 1, k * s)'''


'''def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)'''


'''def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s'''


'''class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance'''


'''class Kangaroo:
    def __init__(self):
        self.pouch_content = []
    
    def put_in_pouch(self, s):
        for i in range(len(self.pouch_content)):
            if self.pouch_content[i] == s:
                print("already in pounch")
                return 
        self.pouch_content.append(s)
    
    def __str__(self):
        if not self.pouch_content:
            return "The kangaroo's pouch is empty"
        else:
            return "The kangaroo pouch contains: " + \
                    str(self.pouch_content)

    
k = Kangaroo()
print(k)
k.put_in_pouch("ball")
print(k)
k.put_in_pouch("hammer")
print(k)
k.put_in_pouch("ball")
print(k)'''


'''def add(s, v):
    assert s is not List.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v
        add(s.rest, v)
    return s'''


'''class Tree:
    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\s'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches    

def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves
    
def height(t):
    if t.is_leaf():
        return 0
    else:
            return 1 + max([height(b) for b in t.branches])

def fib_tree(s):
    if s == 0 or s == 1:
        return Tree(s)
    else:
        left = fib_tree(s - 2)
        right = fib_tree(s - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

def prune(t, s):
    t.branches = [b for b in t.branches if b.label != s]
    for b in t.branches:
        prune(b, s)'''


'''def permutations(s):
    if not s:
        yield ''
    else:
        first = s[0]
        rest = s[1:]
        for rest_permutations in permutations(rest):
            for i in range(len(s)):
                yield rest_permutations[:i] + first + rest_permutations[i:]'''


'''num = int(1234)
str_num = str(num)
print(str_num[1])'''


'''def count(f):
    def counted(s):
        counted.call_count += 1
        return f(s)
    counted.call_count = 0
    return counted'''


'''def exp(b, s):
    if s == 0:
        return 1
    else:
        return b * exp(b, s-1)'''


'''def similar(self, k, similarity):
    others = list(Restaurant.all)
    others.remove(self)
    return sorted(others, key=lambda r: -similarity(self, r))[:k]'''


'''def fast_overlab(s, t):
    i, j, count = 0, 0, 0
    while i <= len(s) and j <= len(t):
        if s[i] == t[j]:
            count, i, j = count+1, i+1, j+1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count'''


'''class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', i work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam' '''


'''def min_abs_indices(s):
    min_abs = min(map(abs, s))
    return (i for i in range(len(s)) if abs(s[i]) == min_abs)'''


'''def largest_adj_sum(s):
    return max(s[i] + s[i+1] for i in range(len(s) - 1))'''


'''def all_have_an_equal(s):
    return min([s.count(x) for x in s]) > 1

print(all_have_an_equal([1, 2, 3, 4, 5, 5]))
print(all_have_an_equal([1, 2, 3, 4, 5, 1]))
print(all_have_an_equal([1, 1, 2, 2, 3, 3, 4, 4]))'''


'''def ordered(s, key=lambda x: x):
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)'''


'''def compose(f, g):
    return lambda x: f(g(x))

def add(x):
    return x + x

def square(x):
    return x * x

def repeat_rec(f, s):
    if s == 0:
        return lambda x: x
    else:
        return compose(f, repeat_rec(f, s - 1))

def repeat_itr(f, s):
    result = lambda x: x
    for _ in range(s):
        result = compose(f, result)
    return result'''


'''def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)'''


'''def pow_lin(x, y):
    if y == 0:
        return 1
    else:
        return x * pow(x, y - 1)


def pow_log(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return pow(x, y // 2) ** 2
    else:
        return x * pow(x, y - 1)'''


'''def reduce(f, s, initial):
    'iterative'
    for x in s:
        initial = f(initial, x)
    return initial

def reduce(f, s, initial):
    'recursive'
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))'''


'''r = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, r)
print(result)'''


'''def ascending(s):
    i = 0
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return False

def ascending_rec(s):
    if len(s) <= 1:
        return True
    elif s[0] <= s[1]:
        return ascending_rec(s[1:])
    else:
        return False'''


'''def filter(pred, s):
    if not s:
        return []
    elif pred(s[0]):
        return [s[0]] + filter(pred, s[1:])
    else:
        return filter(pred, s[1:])

def is_positive(s):
    return s > 0

print(filter(is_positive, [-1, 2, 3]))'''


'''def interleave(lst1, lst2):
    i, j = 0, 0
    lst  =[]
    if not lst1:
        lst.extend(lst2)
    if not lst2:
        lst.extend(lst1)
    while i < len(lst1) and j < len(lst2):
        lst.append(lst1[i])
        lst.append(lst2[j])
        i += 1
        j += 1
    if i < len(lst1):
        lst.extend(lst1[i:])
    if j < len(lst2):
        lst.extend(lst2[j:])
    return lst

def interleave_rec(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    else:
        return [lst1[0], lst2[0]] + interleave_rec(lst1[1:], lst2[1:])

a = [1, 2, 3]
b = [4, 5]
print(interleave(a, b))
print(interleave_rec(a, b))'''


'''def no_repeats(s):
    lst = []
    for i in s:
        if not i in lst:
            lst.append(i)
    return lst

def no_repeats_rec(s):
    if not s:
        return s
    else:
        first = s[0]
        rest = list(filter(lambda x: x != first, s[1:]))
        return [first] + no_repeats_rec(rest)

print(no_repeats([1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]))
print(no_repeats_rec([1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]))
print(no_repeats_rec([1, 2, 3, 1, 1]))'''


'''def enumerate(s, i=0):
    if not s:
        return []
    else:
        return [i, s[0]] + enumerate(s[1:], i + 1)
    
print(enumerate([1, 2, 3]))
print(enumerate(['k', 'p']))'''


'''def merge(order, lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    elif order(lst1[0], lst2[0]):
        return [lst1[0]] + merge(order, lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(order, lst1, lst2[1:])

def bigger(a, b):
    return a > b

def smaller(a, b):
    return a < b

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
print(merge(bigger, a[::-1], b[::-1]))
print(merge(smaller, a, b))'''


'''def trace(fn):
    def traced(n):
        print(f'{fn.__name__}({n})')
        return fn(n)
    return traced

@trace
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(5))'''


