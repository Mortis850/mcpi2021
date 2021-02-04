from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randrange(1,5)
    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = x + 4
    elif r == 1:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x - 4
    elif r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = z + 4
    elif r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = z - 4
        
        
for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x + i
    
    for j in range(10):
        r = random.randrange(0,16)
        z = z + 1
        mc.setBlock(x,y,z,35,r)
        
        time.sleep(1)
        
        
myID = mc.getplayerEntityId('APE 37')
mc.postToTile(myID, 'hello')


list2d = [[1,0,1,1,1,1,1],
          [1,0,0,0,0,0,1],
          [1,0,1,1,1,0,1],
          [1,0,0,0,0,1,1],
          [1,0,1,1,0,0,1],
          [1,0,0,0,1,0,1],
          [1,1,1,1,1,0,1]]

x,y,z = mc.player.getTilePos()
startX = x
startZ = z

for j in range(4):
    for list1d in list2d:
        
        for i in list2d:
            
            for i in list1d:
                mc.setBlock(x,y,z,i)
                x = x + 1
                
            x = startX
            z = z+1
            
        z = startZ
        y = y+1