calls = 0   

def fact(n):
    global calls
    calls += 1  

    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("число: "))

result = fact(n)

print("факторіал =", result)
print("кількість викликів функції =", calls)
