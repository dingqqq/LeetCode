def fib(n):
    if n == 1:
        return 1

    if n == 2:
        return 1

    prev1 = 1
    prev2 = 1

    cur = 0
    for i in xrange(3, n + 1):
        cur = prev2 + prev1
        prev2 = prev1
        prev1 = cur

    return cur

for n in xrange(100):
    print "fib(%d) = %d" % (n, fib(n))
