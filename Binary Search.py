def binarySearch(l,val):
    left=0
    right=len(l)-1
    while left<=right:
        mid= int(left + (right - left)/2)
        if val<l[mid]:
            right=mid-1
        elif val>l[mid]:
            left=mid+1
        else:
            return mid
   
    return "Not Exist"

binarySearch([10,20,30,40,50],55)

