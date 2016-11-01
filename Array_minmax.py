min = None
max = None

while True:
    imp = raw_input ('Enter a Number: ')
    if imp == 'done':
        break
    try:
        num = float (imp)
    except:
        print 'invalid input'
        continue

    if min is None or num < min:
        min = num

    if max is None or num > max:
        max = num

print "Maximum Number: ", int(max)
print "Minimum Number: ", int(min)