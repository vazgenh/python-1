count = 0
str = input()

for i in str:
    if i == '(' :
        count += 1
    elif i == ')':
        count -= 1
        
if count == 0:
    print('Good')
else:
    print("Bad")        
