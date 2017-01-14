rcon_notes.rst


Works well using the code below


        f = open('T:\\user\\AIKIF\\pers_data\\credentials\\minecraft_server.cred')
        pwd = f.read()
        f.close()
        
        import mcrcon
        rcon = mcrcon.MCRcon()
        rcon.connect('192.168.1.9', 25575)
        rcon.login(pwd)
        say_hi = rcon.command('/say hi from rcon')
        rcon.command('/tp craftandstore 4 102 4')
        import time
        time.sleep(1) 
        rcon.command('/fill 0 100 0 2 101 2 minecraft:air') # clear area first
        res2 = rcon.command('/fill 0 100 0 2 101 2 minecraft:glass 0')
        rcon.disconnect()
        self.assertEqual(res2, '18 blocks filled')
        print('say_hi = ', say_hi)
        print('res2 [setblock] = ', res2)
        


But, during large builds (multilevel_castle.py) it crashes the server

     ---- Minecraft Crash Report ----
     Time: 1/14/17 6:08 PM
     Description: Exception ticking world

     
From the server latest.log file

         
    java.util.ConcurrentModificationException

    [18:08:57] [RCON Client #2/INFO]: [Rcon: Block placed]
    [18:08:57] [RCON Client #2/INFO]: [Rcon: 8 blocks filled]
    [18:08:57] [Server thread/ERROR]: Encountered an unexpected exception
    f: Exception ticking world
        at net.minecraft.server.MinecraftServer.D(SourceFile:630) ~[minecraft_server.1.11.2.jar:?]
        at lh.D(SourceFile:335) ~[minecraft_server.1.11.2.jar:?]
        at net.minecraft.server.MinecraftServer.C(SourceFile:562) ~[minecraft_server.1.11.2.jar:?]
        at net.minecraft.server.MinecraftServer.run(SourceFile:466) [minecraft_server.1.11.2.jar:?]
        at java.lang.Thread.run(Unknown Source) [?:1.8.0_111]
    Caused by: java.util.ConcurrentModificationException
        at java.util.HashMap$HashIterator.nextNode(Unknown Source) ~[?:1.8.0_111]
        at java.util.HashMap$KeyIterator.next(Unknown Source) ~[?:1.8.0_111]
        at mc.c(SourceFile:114) ~[minecraft_server.1.11.2.jar:?]
        at lw.d(SourceFile:221) ~[minecraft_server.1.11.2.jar:?]
        at net.minecraft.server.MinecraftServer.D(SourceFile:626) ~[minecraft_server.1.11.2.jar:?]
        ... 4 more
    [18:08:57] [RCON Client #2/INFO]: [Rcon: 29 blocks filled]
    [18:08:57] [Server thread/ERROR]: This crash report has been saved to: T:\user\docs\fun\games\minecraft\__SERVER_1_11_2\.\crash-reports\crash-2017-01-14_18.08.57-server.txt


    
    
    