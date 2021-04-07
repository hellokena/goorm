a = int(input())
for i in range(1, a+1):
	if a%i==0:
		print(i, end=' ')
    
array = ''
a = int(input())
for i in range(1, a+1):
	if a%i==0:
		array += str(i) + ' '
print(array)
