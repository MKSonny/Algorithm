str1 = list(input())
str2 = list(input())

if len(str1)>len(str2):
    str1, str2 = str1, str2

total = 0
for i in str1:
    if i in str2:
        str2.remove(i)
        total += 1
print(len(str1)-total + len(str2))