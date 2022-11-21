str1 = input()
str2=input()
last_chr=str2[-1]
count = 0
for i in str1:
	if i == last_chr:
		count = count + 1
print (count)
