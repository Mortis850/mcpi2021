from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+19,y+19,z+19,46)
mc.setBlocks(x+1,y+1,z+1,x+18,y+18,z+18,0)


import time

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.5)
    
    
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(0.5)
    
    
while True:
    x,y,z = mc.player.getTilePos()
    a = mc.setBlock(x+1,y-1,z,19)
    b = mc.setBlock(x-1,y-1,z,19)
    c = mc.setBlock(x,y-1,z+1,19)
    d = mc.setBlock(x,y-1,z-1,19)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,20)
        
        
x,y,z = mc.player.getTilePos()
a = int(input('Which block do you want to put?'))
mc.setBlock(x,y,z,a)




x,y,z = mc.player,getTilePos()
mc.setSign(x,y,z,63,0)


 x,y,z = mc.player.getTilePos()
 mc.spawnEntity(x,y,z,95)