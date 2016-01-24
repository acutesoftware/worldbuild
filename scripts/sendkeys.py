#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sendkeys.py

import win32gui
import win32con
import win32api


def main():
    hwnd_server = win32gui.FindWindow(None, u"Minecraft Server")
    hwnd_client = win32gui.FindWindow(None, u"Minecraft 1.8.9")
    #hwndMain = win32gui.FindWindow(None, u"Untitled - Notepad")
    print('Minecraft windows: Server = ', hwnd_server, ', Client = ', hwnd_client)
    #hwndEdit = win32gui.FindWindowEx( hwndMain, 0, "Edit", 0 )
    #win32api.PostMessage( hwndEdit,win32con.WM_CHAR, ord('\say hello frpom python'), 0)

    send_text(hwnd_client, "/say hi to client from python\n")
    send_text(hwnd_server, "/say hi to server from python\n")
    # correctly prints the window handle but server or client wont respond
    #  Minecraft windows: Server =  985504 , Client =  526762

            
def send_text(hwnd, txt):
    for c in txt:
        if c == '\n':
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        else:
            win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(c), 0)            
            
            
main()            