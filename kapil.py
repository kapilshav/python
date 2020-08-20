import os       
import pyttsx3
x="0"
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............S U P R A B H A A T.........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print()
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~W h a t   You want me to do  For  You~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")       
print()
print()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print()
print()    
pyttsx3.speak("Suprabhaat")
while True:
     print("")
     pyttsx3.speak("What  you want me to do for you")
     print()
     print("N O T E :- If You Want To Terminate The program Type exit")
     print()
     print("Type Your Requirement ",end=":")
     x=input()
     pyttsx3.speak(x)
     if(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and (("notepad++" in x) or ("texteditor" in x)):
        os.system("notepad++")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and (("zoomapp" in x) or ("zoom" in x)):
        os.system("zoom")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x))and (("chrome" in x)or("browser" in x)):
        print("which site you want to open in chrome browser",end=":")
        site=input()
        os.system("chrome www."+site+".com")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("notepad" in x):
        os.system("notepad")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("vlc" in x):
        os.system("vlc")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("jupyter notebook" in x):
        os.system("jupyter notebook")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("msedge" in x):
        print("which site you want to open in microsoft edge browser",end=":")
        site=input()
        os.system("msedge www."+site+".com")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("teamviewer" in x):
        os.system("teamviewer")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("steam" in x):
        os.system("steam")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("wmplayer" in x):
        os.system("wmplayer")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("safeexambrowser" in x):
        os.system("safeexambrowser")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("powerpnt" in x):
        os.system("powerpnt")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("excel" in x):
        os.system("excel")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("msaccess" in x):
        os.system("msaccess")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("outlook" in x):
        os.system("outlook")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("rainmeter" in x):
        os.system("rainmeter")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("control" in x):
        os.system("control")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("winword" in x):
        os.system("winword")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("startexplorer" in x):
        os.system("start explorer")
     elif (("make"in x) or ("create" in x) or ("mkdir"in x)) and (("directory"in x) or ("dir"in x) or ("mkdir" in x) or ("make the directory" in x) or ("make the folder" in x)):
        print("Name The Folder You Want To Make",end=":")
        fname=input()
        os.system("mkdir "+fname)
     elif (("open"in x) or ("run" in x) or ("perform"in x)) and (("calc"in x) or ("calculator"in x)):
        os.system("calc")
     elif (("exit" in x) or ("quit" in x) or ("close" in x) or ("terminate" in x) or ("band" in x) or ("bandkaro" in x)):
        break
     else:
        print("The System Cannot Find The File Specified->"+x) 
