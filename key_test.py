import thread
import time

def print_keypresses():
    while True:
        time.sleep(1)
        f = open('keypress_count','r')
        print("\nkeypress:"+f.read())

thread.start_new_thread(print_keypresses,())

execfile("key.py")

