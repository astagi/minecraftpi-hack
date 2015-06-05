from PIL import Image
from mcpi import minecraft, block

mc = minecraft.Minecraft.create()
mc.postToChat('Nephila logo demo')

player_pos = mc.player.getPos()

im = Image.open('nephilalogo.png')
pixels = im.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixel = pixels[i,j]
        if pixel[0] > 100:
            type = block.STONE
        else:
            type = block.GLASS
        mc.setBlock(player_pos.x + 2 , player_pos.y - j, player_pos.z + i, type)        
        print (pixel)
