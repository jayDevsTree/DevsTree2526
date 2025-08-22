l1 = [2,55,3,43,11,0,76,34]


def mergeSort(l1,st,end):
    mid = st + (end-st)//2
    if st<end:
        mergeSort(l1,st,mid)
        mergeSort(l1,mid+1,end)
        
        merge(l1,st,mid,end)
        
def merge(l1,st,mid,end):
    temp= []
    
    
    i,j = st,mid+1
    
    while i<=mid and j <=end:
        if(l1[i]<=l1[j]):
            temp.append(l1[i])
            i=i+1
        else:
            temp.append(l1[j])
            j = j+1
            
    while i<=mid:
        temp.append(l1[i])
        i+=1
        
    while j <=end:
        temp.append(l1[j])
        j+=1
        
    for idx in range(0,len(temp)):
        l1[st+idx] = temp[idx]
        

print("Merge Sort,")        
print('Before:',l1)
mergeSort(l1,0,len(l1)-1)
print('After:',l1)
print(f'Time Complexity = O(nlogn)')
print("Space Complexity = O(n)")