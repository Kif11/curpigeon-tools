from random import randint

upNum = 1
for i in range(0, 105):
    rnd = randint(0,360) #Inclusive
    print rnd
    
    cmds.select( 'oak_tree_GEO_' + str (upNum) )
    cmds.rotate( 0, rnd, 0, r=True )
    upNum = upNum+ 1

