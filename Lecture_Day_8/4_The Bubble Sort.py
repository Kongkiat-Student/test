def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[+1]
                alist[i+1] = temp

alist = [54,26,93,17,7731,44,55,20]
bubbleSort(alist)
print(alist)
