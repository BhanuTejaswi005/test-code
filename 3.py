valid_dig=[0,1,2,5,6,8,9]
def valid(k):
    k=str(k)
    for i in k:
        if int(i) not in valid_dig:
            return False
    return True

n = int(input())
if n < len(valid_dig):
    print(valid_dig[n])
else:
    count=len(valid_dig)
    k=valid_dig[-1]
    while(count<=n):
        k+=1
        if valid(k):
            count+=1
    print(k)
