from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

while True:
    x,y,z = mc.player.getTilePos()
    x = x + random.randrange(-10,10)
    z = z + random.randrange(-10,10)
    y = y + 30
    
    mc.spawnEntity(x,y,z,92)
    time.sleep(0.2)
    
while True:
    hits = mc.events.pollProjectileHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.createExplosion(x,y,z)
        
        
def buildpyramid(x,y,z):
    base = 20
    height = (base//2) + 1
    
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        z2 = z + base - i
        mc.setBlocks(x1, y1, z1, x2, y2, z2, 46)
        
        
x,y,z = mc.player.getTilePos()
buildPyramid(x,y,z)


line1 = []
line2 = []
line3 = []

for i in range(1,4):
    line1.append(1*i)
    
for i in range(1,4):
    line2.append(2*i)
    
for i in range(1,4):
    line3.append(3*i)
    
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))


x,y,z = mc.player.getTilePos()

number = 1

for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)