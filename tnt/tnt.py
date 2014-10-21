
from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos_player = mc.player.getPos()

for i in range(50):
    mc.setBlock(pos_player.x + i, pos_player.y, pos_player.z, 46)
    mc.setBlock(pos_player.x + i, pos_player.y - 1, pos_player.z, 1)
    block = mc.getBlockWithData(pos_player.x + 1, pos_player.y, pos_player.z)
    block.data = (block.data + 1) & 0xf
    mc.setBlock(pos_player.x + i, pos_player.y, pos_player.z, block.id, block.data)
