from mcpi import minecraft
from nanpy import Servo, SerialManager
import time

mc = minecraft.Minecraft.create()

def get_angle(pos_player, max_alt=180):
    angle = pos_player.y * (90.0/max_alt) + 90
    return int(angle)

connection = SerialManager(
    device='/dev/ttyACM0',
    rtscts=True
)
servo = Servo(
    7,
    connection=connection
)

while True:
    pos_player = mc.player.getPos()
    angle = get_angle(pos_player)
    servo.write(angle)
