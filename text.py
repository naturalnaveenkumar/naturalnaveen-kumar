n = int(input(" "))
arr  = list(map(int,input(" ").split()))
di = {}
idx = -1
for i in range(0,n):
    if arr[i] not in di:
        di[arr[i]] = i 
    else:
        idx = i 
        break
    if idx == -1:
        newarr = sorted(arr,rev = True)
        for i in newarr:
            print(i,end=" ")
    else:
        print('Duplicate founf at index1',idx)
