######## World's Largest Hello world program ########

######## Execute output of this code ########

for x in range(0,1000):
    print("\t"*(x)+"def "+"_"*(x+1)+"():")
print("\t"*1000+"print('Hello world')")
for x in range(1000-1,0,-1):
    print("\t"*(x)+"return "+"_"*(x+1))
print("_"+"()"*1000)
