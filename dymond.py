n = int(input())

for i in range(1, n + 1):
    if (i <= (n + 1)/2) :
        print((n - i)*' ' + i*'* ')
    else:
        print((i - 1)* ' ' + (n - i + 1)*'* ') 
