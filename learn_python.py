a,b = 0,1
while b < 10:
    print b
    a,b = b, a+b    #Multiple assignment

print "+" * 50

a,b = 0,1
while b < 1000:
    print b,
    a,b = b, a+b
print ""

print "+" * 50

x = int(raw_input("Please enter an integer: "))
print x

print "+" * 50

words = ['hello', 'world', 'in', 'python']
print words

for w in words[:]:           #make a copy of the list for iteration
    if len(w) > 5:
        words.insert(0, w)
print words


# range(start, end, step)


# LOOP STATEMENTS can have an ELSE clause

for n in range(2,10):
    print "------{}-----".format(n)
    for x in range(2, n):
        print n, x
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        print n, 'is a prime number'

print '+' * 50



