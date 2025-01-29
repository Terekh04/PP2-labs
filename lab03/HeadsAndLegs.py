def solve(numheads, numlegs):
    if numlegs%4==0:
        rabbit=numlegs/4
        chicken=0
    else:
        rabbit=(numlegs-2)/4
        chicken=1
    if rabbit+chicken==numheads:
        pass
    else:
        while rabbit+chicken!=numheads:
            rabbit-=1
            chicken+=2
    ans=[int(rabbit), chicken]
    return ans
#first element is a number of rabbits, second element is a number of chickens