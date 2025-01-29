def spy_game(nums):
    num=''
    for i in nums:
        if i==0 or i==7:
            num+=str(i)
    if '007' in num:
        print('True')
        return
    else:
        print('False')
        return
