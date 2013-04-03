import curses

key = curses.getkey()
print("hej")
print(key)

# class TestScreen:
#     def __init__(self, scr):
#         self.scr = scr
#         self.scr.move(10, 5)
#         self.scr.addstr('Press q to QUIT', curses.A_BOLD)
#     def loop(self):
#         k = None
#         while k != 'q':
#             k = self.scr.getkey()
#             try:
#                 o = ord(k)
#             except:
#                 o = '????'
#                 #Error.elog('test:', k, o)
#     
# def test_keys(scr):
#     screen = TestScreen(scr)
#     screen.loop()
# 
# if __name__ == '__main__':
#     curses.wrapper(test_keys)
