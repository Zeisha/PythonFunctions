def calculator():
 operation = input('choose the operation  1. Add 2. Subtract 3.Divide 4.Multiply ')

 a = int(input('type the first number for addition '))
 print(type(a))

 b = int(input('type the second number for addtion '))
 print(type(b))
 if (operation in ['Add' , '1']):
     c = a + b
     print('Sum of a and b is ' + str(c))
 elif(operation in ['Subtract' , '2']):
     c = a-b
     print('difference of a and b is ' + str(c))
 elif (operation in ['Divide' , '3']):
     c = a/b
     print('difference of a and b is ' + str(c))
 elif (operation in ['Multiply' , '4']):
     c = a*b
     print('difference of a and b is ' + str(c))
 else:
      print('Please try agin')

 return;




calculator()


