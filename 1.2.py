def my_str(num: int) -> str:
    digits = ["0","1","2","3","4","5","6","7","8","9"]

    neg = False
    if num == 0:
        return "0"

    if num < 0:
        neg = True
        num = -num

    res = ""
    n = num

    while n > 0:
        last = n % 10
        res = digits[last] + res
        n //= 10

    if neg:
        res = "-" + res

    return res


print(my_str(12))
print(my_str(-55))
print(my_str(0))
