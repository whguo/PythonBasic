def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    print (sum)
    return sum

nums = range(1,20)
calc(*nums)
