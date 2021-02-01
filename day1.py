from mcpi.minecraft import Minecraft
mc = Minecraft.create()


while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat('X:'+ str(x) + 'Y:' + str(y) + 'z:' + str(z))
    
    
x,y,z = mc.player.getTitlePos()
mc.setBlock(x,y,z,46)
mc.setBlock(x,y+1,z,46)
mc.setBlock(x,y+2,z,46)
mc.setBlock(x,y+3,z,46)
mc.setBlock(x,y+4,z,46)
mc.setBlock(x,y+5,z,46)
mc.setBlock(x,y+6,z,46)






x,y,z = mc.player.getTitlePos()
mc.setBlock(x+1,y,z,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x,y,z+1,46)
mc.setBlock(x,y,z-1,46)
mc.setBlock(x+1,y,z+1,46)
mc.setBlock(x-1,y,z+1,46)
mc.setBlock(x-1,y,z-1,46)
mc.setBlock(x+1,y,z-1,46)














import random
import time 
x,y,z = mc.player.getTilePos()

while True:
    r = random.randrange(0,16)
    mc.setBlocks(x+5,y,z+5,x+5,y,z-5,35,r)
    time.sleep(0.5)