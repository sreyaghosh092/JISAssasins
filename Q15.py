digits=input("Enter a number x, enter two numbers to raise the previous number by the sum of these number: ")
digits=list(digits.split(" "))
result=int(digits[0])**(int(digits[1])+int(digits[2]))
print(result)
