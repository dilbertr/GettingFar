import gd
import time
import pynput
from pynput.keyboard import Key, Controller
memory=gd.memory.get_memory()
percent=memory.get_percent()
lastpercent=memory.get_percent()
keyboard=Controller()
print("Made by LDubbs")
print("To use, set your deafen key in discord to ctrl + ~")
print("If you self deafen, the bot will still think you're undeafened, and thus will undeafen you when you get far.")
far=int(input("Far percent: "))
levelid=int(input("Level id: "))
print("Feel free to start playing...")
def Deafen():
    global keyboard
    keyboard.press(Key.ctrl_l)
    keyboard.press('`')
    keyboard.release('`')
    keyboard.release(Key.ctrl_l)
def isfar(percent):
    global far
    if percent >= far:
        return True
    else:
        return False
while True:
    time.sleep(0.2)
    percent=memory.get_percent()
    if isfar(percent)!=isfar(lastpercent):
        if memory.get_level_id_fast() == levelid:
            if memory.is_practice_mode()==False:
                print("Toggled deafen")
                Deafen()
            else:
                print("Player is in practice")
        else:
            print("Not playing specified level")
    lastpercent=percent
