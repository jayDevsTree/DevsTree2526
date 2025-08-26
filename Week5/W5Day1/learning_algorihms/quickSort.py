def quickSort(l1,st,end):
    if st<end:
        pivot = partiton(l1,st,end)
        quickSort(l1,st,pivot-1)
        quickSort(l1,pivot+1,end)
        
def partiton(l1,st,end):
    pivot = l1[end]
    idx = st-1
    for j in range (st,end):
        if l1[j]<= pivot:
            idx+=1
            l1[j],l1[idx] = l1[idx],l1[j]
    idx+=1
    l1[idx],l1[end] = l1[end],l1[idx]
    return idx

l1 = [99,4,32,1,56,32,52]

print("Before:",l1)
quickSort(l1,0,len(l1)-1)
print("After:",l1)
print(l1)
print("Time Complexity (Avg)= O(nlogn)")
print("Time Complexity (Worst)= O(n^2)") 

print("Space Complexity = O(1)")