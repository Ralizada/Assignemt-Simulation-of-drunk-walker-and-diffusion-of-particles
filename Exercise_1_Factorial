# using dynamic evaluations
x = int(input())
if x < 1:
    print("Positive integers only!")
else:
    fact_string = '1'
    for i in range(1, x+1):
        fact_string = fact_string + '*' + str(i)
    print(eval(fact_string))
    
# using recursion
def fact(num):
    if num < 1:
        print("Positive integers only!")
        return None
    elif num == 1:
        return 1
    else:
        return num*fact(num-1)


print(fact(int(input())))
