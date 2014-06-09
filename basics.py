# strings
txt = 'Hello,'
txt += ' World! '
print txt
print txt * 2
print

# int
i = 0
i = i + 2
print i
print

# float
f = 0.5
f = f * 2
print f
print

# int and float in strings
print '%d == 2' % i
print '%s == 2' % i
print '%f == 1.000000' % f
print '%d == 1' % f
print '%s == 1.0' % f
print '%d + %d == 3' % (i, f)
print 'Welcome to %s' % 'Kyoto'
print 

# list
l = [1, 2, 3, 4]
print l[0]
l.append(5)
print l
del l[1]
print l
l.extend([6, 7])
print l
print 

# dict
d = {'a': 1, 'b': 2, 'c': 3}
print d['b']
d['d'] = 4
print d
del d['b']
print d
print 

# loop
for i in [0, 1, 2, 3]:
    print i
print range(4)
for i in range(4):
    print i
for key in {'a': 1, 'b': 2}:
    print key
