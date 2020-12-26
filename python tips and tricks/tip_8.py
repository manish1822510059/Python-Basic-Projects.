# IN TIP YOU CAN PASS ANY MORE THAN MANY PARAMETER SOME MODIFICATION IN FUNCTION


def sum(*a):
    result = 0
    for i in a:
        result = result + i
    return result

res = sum(2,3,10,4,15,100)
print(res)    