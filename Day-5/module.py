## Type-1
def func1():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))

    var3 = var1 + var2
    print(f"{var1} + {var2} = {var3}")

## Type-2
def func2(var1,var2):
    var3 = pow(var1,var2)
    print(f"{var1}^{var2} = {var3}")

## Type-3
def func3():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))

    var3 = var1 * var2
    return var3

## Type-4
def func4(num1, num2):
    num3 = num1/num2
    return num3