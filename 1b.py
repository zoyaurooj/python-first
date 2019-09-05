def fib(n):
 if n in [0,1]:
  return 1
 else:
  return(fib(n-1)+fib(n-2))
number=int(input("enter the number"))
if number<0:
 print("enter a possitive no")
else:
 for i in range(number):
  print(fib(i))
