def factorial_iterative(n):
    """

    :param n: Integer
    :return: n * n-1 * n-2 *.....1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
        return fac
def factorial_recursive(n):
   """
   :param n: Integer
   :return: n * n-1 8 N-2 8 n-3.......1
   """
   if n==1 :
       return 1
   else:
       return n * factorial_recursive(n-1)
numbers = int(input("Enter the number"))
print("Factorial using iterative method", factorial_iterative(numbers))
print("Factorial using recursive method", factorial_recursive(numbers))
# n! = n * n-1 * n-2 * n-3.....1
# n! = n* n-1!