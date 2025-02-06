def solve(numheads, numlegs):
    y=(numheads-2*numlegs)//2
    x=numheads-y
    retiurn x,y
numheads=35
numlegs=94
x,y=solve(numheads, numlegs)
print(f" chickens: {x},  rabbits:{y}")
