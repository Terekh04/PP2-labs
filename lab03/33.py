def has_33(nums):
    itHas33=False
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            itHas33=True
            break
    if itHas33:
        print('True')
        return
    else:
        print('False')
        return
has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 