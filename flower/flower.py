from mcpi import minecraft

mc = minecraft.Minecraft.create()

while True:
    pos_player = mc.player.getPos()
    mc.setBlock(pos_player.x, pos_player.y, pos_player.z, 38)
