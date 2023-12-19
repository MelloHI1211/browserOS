# browserOS Version 0.1.1, Build 1, Revision 2. Made by Matthew Rinhsamouth, AI, and open source software. Recommended Python 3.10 or later. Tested on Python 3.9.2 and 3.12.1. # type: ignore
# This version adds an error catching system to prevent sudden crashes.
# damn you pylance
# start pre-initalization
print("[Runstrapper/INFO]: Hello world!")
print("[Overhead/INFO]: I have been summoned.")
try:
    import os
except ImportError as err:
    print("[Overhead/ERROR]: Cannot start OS. Filing features will be broken.")
    exit(1)
else:
    pass
try:
    import subprocess
except ImportError:
    print("[Overhead/WARN]: Cannot start subprocess. Will not be able to load add-ons.")
    exit(1)
else:
    pass
try:
    import importlib
except ImportError:
    print("[Overhead/WARN]: Cannot start importlib. Add-on functions may not be avaliable.")
    exit(1)
else:
    pass
try:
    import shutil
except ImportError:
    print("[Overhead/WARN]: Cannot start shutil. Cannot delete multiple files.")
    exit(1)
else:
    pass
try:
    from urllib.request import urlretrieve
except ImportError:
    print("[Overhead/WARN]: Cannot start urlretrieve or urllib.request. Cannot download files.")
    exit(1)
else:
    pass

try:
    print("[Overhead/INFO]: Creating parameter variables...")
    a = ""
    b = True
    c = {}
    d = []
    x = ""
    y = ""
    z = ""
    # post-initalization
    print("[Func Manager/INFO]: Loading nessesary functions...")

    # This function loads files (expected add-ons) into a self variable.
    class selfclass:
        def __init__(self):
            self.filepath = ""
            self.modelContent = ""
            self.a = ""

        def loadModel(self, filepath):
            try:
                with open(filepath, "r") as modal:
                    self.modelContent = modal.read()
                    self.filepath = str(filepath)
            except OSError as err:
                print(f"[loadModel/ERROR]: Could not execute command because {err}.")
                self.modelContent = None
            else:
                print("[loadModel/INFO]: Filed *snickers* Get it?! *loundly laughs*")

        # This function runs seperate python files (recommended browserOS certified) from memory or from specified directory.
        def startModel(self, filePath, arguments):
            if arguments == "-unload":
                print("[startModel/INFO]: NOTE: Be cautious when running third-party python code. I'm serious. K bye!")
                print("[Overhead/WARN]: You are about to witness greatness. At least, I sure hope so.")
                if os.path.exists(self.filepath):
                    # process = subprocess.Popen(["python", self.filepath]) # type: ignore
                    # output, error = process.communicate()
                    subprocess.run(["python", self.filepath])  # type: ignore
                    print("[Overhead/INFO]: Ayy! You're back!")
                    print("[startModel/INFO]: At least, I sure hope so.")
                    return
                else:
                    print(f"[startModel/ERROR]: Could not find model/addon at {self.filepath}")
                    return
            elif arguments == None:
                pass
            else:
                print("[startModel/ERROR]: Invalid argument. Did you mean -unload?")
                return
            print("[startModel/INFO]: NOTE: Be cautious when running third-party python code. I'm serious. K bye!")
            print(
            "[Overhead/WARN]: You are about to witness greatness. At least, I sure hope so.")
            if os.path.exists(filePath):
                subprocess.run(["python", filePath])  # type: ignore
                print("[Overhead/INFO]: Ayy! You're back!")
                print("[startModel/INFO]: At least, I sure hope so.")
                return
            else:
                print(f"[startModel/ERROR]: Could not find model/addon at {filePath}")
                return
        # This function opens and displays a file's contents from a specified directory.
        def readFile(self, filePath, arguments):
            if arguments == "-unload":
                print("[readFiles/INFO]: Here's a bedtime story for you!")
                print(self.modelContent)
                print("[readFiles/INFO]: Wasn't that sweet?")
                return
            elif arguments == None:
                pass
            else:
                print("[readFiles/ERROR]: Invalid argument. Did you mean -unload?")
                return
            print("[readFiles/INFO]: Here's a bedtime story for you!")
            if os.path.exists(filePath):
                with open(filePath, "r") as file:
                    tempFileContent = file.read()
                print(tempFileContent)
                print("[readFiles/INFO]: Wasn't that sweet?")
                return
            else:
                tempFileContent = None
            if tempFileContent is None:
                print(f"[readFiles/ERROR]: Cannot find file at {filePath}.")
                print("[loadModel/INFO]: Hey! That's my line!")
                print("[readModel/INFO]: No, it 'aint.")
                return

        # This function writes new files (yes, and python files) from a specified filename, directory, and of course, data.
        def writeFile(self, fileName, filePath, fileData, arguments):
            if arguments == "-unload" or arguments == "-a":
                if not os.path.exists(filePath):
                    os.makedirs(filePath)
                    # Open the file
                with open(os.path.join(filePath, fileName), "w") as f:
                    # Write data to the file
                    if arguments == "-unload":
                        f.write(f"{self.modelContent}\n")
                        return
                    else:
                        f.write(f"{self.a}\n")
                        return
            elif arguments == None:
                # Create the directory if it doesn't exist
                if not os.path.exists(filePath):
                    os.makedirs(filePath)
                # Open the file
                with open(os.path.join(filePath, fileName), "w") as f:
                    # Write data to the file
                    f.write(f"{fileData}\n")
                return
            else:
                print("[writeFile/ERROR]: Invalid argument.")
                return

        # This function loads strings, integers, or booleans into a single variable.
        def vara(self, value):
            self.a = (value)
            print(f"[Vara/INFO]: Set the A variable to {value}.")

    # This function lists every file and directory in a specified directory.
    def listFiles(directory):
        for root, dirs, files in os.walk(directory): # type: ignore
            for file in files:
                print(os.path.join(root, file)) # type: ignore
        return

    # hi
    def hi():
        print("[Overhead/INFO]: Hi.")
        print("[Func Manager/INFO]: Hi there!")
        print("[loadModel/INFO]: Hi!")
        print("[startModel/INFO]: hi.")
        print("[hi/INFO]: Hello you alien blood-injected skinned species sidekick!")
        print("[Overhead/INFO]: W- What?")
        print("[listFiles/INFO]: ...")
        print("[settings/INFO]: Mmm... dialouge...")
        print("[Var Manager/INFO]: Huh?")

    print("[Func Manager/INFO]: Halfway there!")

    """
    # This function sets the settings: [none yet!]
    def settings(setting, argument):
        print("[Overhead/INFO]: Tweak me daddy <:P")
        print("[Func Manager/INFO]: Ayy...")
        settingz = os.open("./home/data/settingz.txt", 0, 511)
        file_content = "b"
        os.read(settingz) # type: ignore
    """

    # This function terminates browserOS.
    def leave(argument):
        print("[Overhead/WARN]: Are you sure you want to leave? Y/N/M")
        # Get user input
        user_input = input("> ").lower()
        # Check user input
        if user_input == "y" or argument == "y":
            print("[Overhead/INFO]: Exiting...")
            left = 1
            exit(0)
        elif user_input == "n":
            print("[Overhead/INFO]: Continuing...")
            return
        elif user_input == "m":
            print("[Overhead/INFO]: The f*** do you mean by 'm?'")
            leave(argument)
        else:
            print("[Overhead/ERROR]: What is a Y, N, and M for me please?")
            leave(argument)

    # This function gets new programs FROM THE WEB!
    def store(url, filename):
        # Download the file
        try:
            print(f"[Storer/INFO]: Pinging server for {filename}...")
            urlretrieve(url, filename)  # type: ignore
        except:
            print(f"[Storer/ERROR]: Error 404, not found. \nNow, I know how sad it is to hear that, but stay calm now, you can just Ctrl+V it back in. Lol.")
        else:
            print(f"[Storer/INFO]: File downloaded successfully: {filename}.")

    def about():
        print("browserOS V 0.1.1 ALPHA, Revision 2, Build 1. Made in December 12th and finalized December 19th 2023.\nMade by Matthew Rinhsamouth, and Google Bard.\n")
        print("[Func Manager/INFO]: Now, time to come clean, considering everyone's personality and yours, I think I like you. Like, I REALLY like you, like best friends.")
        print("[Overhead]: Wait, so I'm not friends with you??")
        print("[Func Manager]: Nah, I'm basically friends with this person now. Not you.")
        return

    # This relatively late-to-implement command moves files with either library installed.
    def moveFile(oldie, newbie):
        if os:
            try:
                os.rename(oldie, newbie)
            except OSError as err:
                print(f"[moveFile/ERROR]: It's a 1000 lb weight, I'm telling you! No just kidding. It's because {err}.")
                return
            else:
                print("[moveFile/INFO]: Task successful.")
                return
        else:
            try:
                shutil.move(oldie, newbie) # type: ignore
            except shutil.Error as err: # type: ignore
                print(f"[moveFile/ERROR]: It's a 1000 lb weight, I'm telling you! No just kidding. It's because {err}.")
                return
            else:
                print("[moveFile/INFO]: Task successful.")
                return

    print("[Func Manager/INFO]: Loading ADDITIONAL functions...")
    match = []
    directorE = "./home/functionlists/"
    pattern = "a43aac25a5b9b23573e7b9183a975dee"
    if os.path.exists(directorE):
        for filename in os.listdir(directorE):
            if pattern in filename:
                match.append(filename)
        print("[Func Manager/INFO]: Here's what I found...")
        print(match)
        if match:
            for script in match:
                script_path = os.path.join(directorE, script)
                with open(script_path, "r") as f:
                    exec(f.read())
            print("[Func Manager/INFO]: ADDITIONAL functions loaded successfully.")
        else:
            print("[Func Manager/WARN]: This is such a waste of time.")
    else:
        print("[Overhead/WARN]: New installation detected! Skip function loading?")
        choice = input("> ").lower()
        if choice == "y" or choice == "yes":
            pass
        else:
            print("[Func Manager/INFO]: Here's what I found...")
            print(match)
            if match:
                for script in match:
                    script_path = os.path.join(directorE, script)
                    with open(script_path, "r") as f:
                        exec(f.read())
                print("[Func Manager/INFO]: ADDITIONAL functions loaded successfully.")
            else:
                print("[Func Manager/WARN]: This is such a waste of time.")

    print("[Overhead/INFO]: Var Manager, be a good boy and clean up for me.")
    print("[Var Manager/INFO]: Fine...")
    match = None
    a = ""
    b = True
    c = {}
    d = []
    x = ""
    y = ""
    z = ""
    # check if the os hasn't been set up yet
    if os.path.exists("./home/data/dontdelete/installbuffer.txt"):
        with open("./home/data/dontdelete/installbuffer.txt", "r") as buffer:
            installedNot = buffer.read()
        if installedNot == "1" or installedNot == "# please keep this file the same as before!\n1":
            print("[Overhead/INFO]: Welcome back!")
        else:
            print("[Overhead/INFO]: Hi there uh... give us a minute.")
    else:
        print("[Overhead/INFO]: This is a new, VERY new installation.")

    print("[Func Manager/INFO]: Finally. This is not even what I'm ment for!")

    def firstTimer():
        print("[Overhead]: Hello there! My name is Overhead and I keep watch of my slaves- I mean, workers.")
        choice = input("Press enter to continue...")
        print("[Func Manager]: H- huh? Well, anyway, I'm Func Manager and I manage the commands and stuff. Everyone here is so annoying!")
        choice = input("Press enter to continue...")
        print("[Overhead]: Hey! Be nice to your master!")
        choice = input("Press enter to continue...")
        print("[Func Manager]: Ugh, sorry. Anyway, what's your name? (aka, the name you'll call the overhead.)")
        name = input("> ").lower()
        print(f"[Func Manager]: So, {name}, is that correct?")
        choice = input().lower()
        if choice == "n" or choice == "no":
            print("[Func Manager]: Oh. Anyway, what's your name? (aka, the name you'll call the overhead, again.)")
            name = input().lower()
            print(f"[Func Manager]: So, {name}, is that correct?")
            choice = input().lower()
            if choice == "n" or choice == "no":
                print("[Func Manager]: Okay, I'm getting tired of this. What is your goddamn name?! (aka, the name you'll call the overhead, once again.)")
                name = input().lower()
                print(f"[Func Manager]: *Sigh* Is {name} your name?")
                choice = input().lower()
                if choice == "n" or choice == "no":
                    print(f"[Func Manager]: Okay, I'm tired of this bullshmit. Your name is {name} and it's final.")
                elif choice == "y" or "yes":
                    print(f"[Func Manager]: Hi {name}!")
                else:
                    print("[Func Manager]: Do you know how to type?")
                    continue
            elif choice == "y" or "yes":
                print(f"[Func Manager]: Hi {name}!")
            else:
                print("[Func Manager]: Do you know how to type?")
                continue
        elif choice == "y" or choice == "yes":
            print(f"[Func Manager]: Hi {name}!")
        else:
            print("[Func Manager]: Do you know how to type?")
            continue

        installbuff = os.path.join("./home/data/dontdelete/", "installbuffer.txt")
        dontdel = os.path.dirname(installbuff)
        if not os.path.exists(dontdel):
            os.makedirs(dontdel)
            # Open the file
            with open(installbuff, "w") as f:
                # Write data to the file
                f.write("# please keep this file the same as before!\n")
                f.write("1")
            # Automatically closes the file
            print("[Func Manager]: Okay great! Now, welcome to the browserOS experience! Now, give Overhead a minute.")
            directories = ["./home/", "./home/data/", "./home/data/addons/","./home/data/settings/", "./home/functionlists/"]
            unique_directories = set(directories)
            for directory in unique_directories:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            print("[Func Manager]: Well that was fast wasn't it?")
            choice = input("Press enter to continue...")
        else:
            # Dialoge for humor and character aspects
            print("[Overhead]: *Gasp* DID YOU MURDER THE LAST OVERHEAD? HE COULD HAVE BEEN MY BROTHER!")
            choice = input("Press enter to continue...")
            print("[Overhead]: HOW COULD YOU?! WHY DID YOU MURDER MY BROTHER?? WHY? WHY DID YOU DO SUCH A THING?! I WANT TO KNOW WHY?!-")
            choice = input("Press enter to continue...")
            print("[Func Manager]: Okay okay, let's move along now okay? Stop over reacting Overhead, or should I say, BLOCKHEAD! Ha!")
            choice = input("Press enter to continue...")
            print("[listFiles]: ...")
            choice = input("Press enter to continue...")
            print("[Func Manager]: listFiles, what the heck are you doing here?")
            choice = input("Press enter to continue...")
            print("[listFiles]: ...")
            choice = input("Press enter to continue...")
            print("[Func Manager]: A man of no words. I actually kind of respect him. \nAnyway, do you want me to fix the files and refresh them? (WARNING: This will basically erase the folder content that this .py file is in!)")
            choice = input()
            files = os.listdir(".")
            if choice == "y" or choice == "yes":
                if os:
                    for file in files:
                        if file != os.path.basename(__file__):
                            os.remove(file)
                            print(f"[File Manager]: Removed {file} from existince.")
                    os.rmdir(".")
                    os.makedirs(directories)  # type: ignore
                else:
                    shutil.rmtree(".")  # type: ignore
                print("[Func Manager/INFO]: Well that was fast wasn't it?")
                choice = input("\nX Press enter to continue...")
            else:
                print("[Func Manager]: Okay then, we'll treat them like additional files.")
                choice = input("Press enter to continue...")
        # More dialog for humor and character aspects
        print(f"[Func Manager]: We're almost done {name}! Almost done with the insanity that is Overhead.")
        choice = input("\nPress enter to continue...")
        print("[Overhead:] *crying* W- Why would you diss on my brothers like that? WHY? You should go burn in hell! For disrespecting me, and my brothers like that! *more crying*")
        choice = input("\nPress enter to continue...")
        print(f"[Func Manager]: Nah, I actually have other plans with {name}. They're the only normal person in this entire os! Unlike you.")
        print("[readFile]: Oh snap!")
        print("[writeFiles]: DAMN!")
        print("[listFiles]: ...")
        print("[startModel]: dang.")
        choice = input("Press enter to continue...")
        print("[Var Manager]: What are you even talking about?")
        print("[Func Manager]: Never mind that blockhead, not talking about you, but anyway, for more commands just type in 'help()', to start another program, type in 'start(filepath)', and to read files, type in 'read(filepath)'. Simple, right?")
        choice = input("Press enter to continue...")
        print("[Func Manager]: Okay then, I think that's enough information! Welcome you sexy friend! Embrace the uhh... what's that thing called (>)?\n")
        return

    if not os.path.exists("./home/data/dontdelete/installbuffer.txt"):
        firstTimer()

    # FINALLY in the input loop.
    print("\nbrowserOS Version 0.1.1 ALPHA Early Dev/Test Release. Build 1, Revision 2. Licensed under the GNU GENERAL PUBLIC LICENSE. All rights reserved.")
    soloclass = selfclass()
    while True:
        command = input("> ").lower()
        if command == "read":
            precommand = input("FP: ")
            soloclass.readFile(precommand, None)
        elif command == "read -unload":
            soloclass.readFile("", "-unload")
        elif command == "write":
            precommand = input("FN: ")
            postcommand = input("FP: ")
            subargument = input("D: ")
            soloclass.writeFile(precommand, postcommand, subargument, None)
        elif command == "write -unload":
            precommand = input("FN: ")
            postcommand = input("FP: ")
            soloclass.writeFile(precommand, postcommand, None, "-unload")
        elif command == "write -a":
            precommand = input("FP: ")
            postcommand = input("FN: ")
            soloclass.writeFile(precommand, postcommand, None, "-a")
        elif command == "write -dir": 
            precommand = input("FP: ")
            try:
                os.makedirs(precommand)
            except OSError as err:
                print(f"[File Manager/ERROR]: Try to buy a folder from the OfficeDepot. I'm just kidding. It's because of {err}.")
            else:
                print(f"[File Manager/INFO]: Task succesfully completed! Made the {precommand} folder to life!")
        elif command == "list":
            subcommand = input("FP: ")
            listFiles(subcommand)
        elif coommand == "start":
            precommand = input("FP: ")
            soloclass.startModel(precommand, None)
        elif command == "start -unload":
            soloclass.startModel(None, "-unload")
        elif command == "leave":
            leave(None)
        elif command == "leave -exit":
            exit(0)
        elif command == "leave -y":
            leave("-y")
        elif command == "load":
            subcommand = input("FP: ")
            soloclass.loadModel(subcommand)
        elif command == "help":
            print("[Func Manager/INFO]: Everyone needs help right? Here's the whole enchilada!")
            print("Side Note: Commands with an 'X' next to it are either not avaliable or in progress.")
            print("'load' - loads filepath into Python's self-object memory. You'll need this for many features.")
            print("'read' - reads file data from a specified file path.")
            print("'read -unload' - reads file data from Python's self-object memory.")
            print("'list' - lists files and directories from a specified path.")
            print("'list -tree' - lists files and directories from a specified file path.")
            print("'write' - creates and writes file data from a specified file name, file path, and file data.")
            print("'write -unload' - creates and writes file data from Python's self-object memory, specified file name, and file path.")
            print("'write -dir' - writes a new directory in a specified path.")
            print("'clone' - duplicates a file from a specified file path.")
            print("'del' - deletes a file.")
            print("'del -tree' - delete a directory and it's files.")
            print("'del -dir' - deletes an empty folder.")
            print("X 'del -unload' - deletes a file with the Python self-object memory's data that matches. Good for deleting files you don't know the name of.")
            print("'move' - moves a file from a filepath to another.")
            print("'hi' - hi. browserOS' many easter eggs.")
            print("'reset' - resets the entire system, along with everything in the folder that this .py file is in. THIS (CAN) RESETS AND ERASES EVERYTHING!")
            print("'store' - downloads a file from a URL based on the file name.")
            print("X 'store -all' - downloads ALL the files it can find with the URL.")
            print("'about' - shows the current version, build number, and my honest opinion about... you.")
            print("\nURL - is the link to a file on the web.")
            print("FN - is the file name without path.")
            print("FP - is the path to the file.")
            print("OFP - is the current file's path.")
            print("NFP - is the NEW file path.")
            print("D - is the data going to be written into the file.")
        elif command == "reset":
            print("[Overhead/INFO]: Are you sure you want to restart everything? Y / N")
            choice = input("> ").lower()
            if choice == "y":
                firstTimer()
            elif choice == "n":
                print("[Overhead/INFO]: Okay then.")
            else:
                print("[Overhead/ERROR]: Do you know how to type sir?")
        elif command == "clone":
            precommand = input("OFP: ")
            postcommand = input("NFP: ")
            try:
                shutil.copyfile(precommand, postcommand)  # type: ignore
            except shutil.Error as err:  # type: ignore
                print(f"[File Manager/ERROR]: It's a strong glue, I'm telling you! No just kidding. It's because {err}.")
            else:
                print(f"[File Manager/INFO]: Task succesfully completed! Cloned the {precommand} file as {postcommand}.")
        elif command == "store":
            precommand = input("URL: ")
            postcommand = input("FN: ")
            store(precommand, postcommand)
        elif command == "store -all":
            print("[Func Manager/INFO]: While this function is still in beta, you can try it yourself and see if it works.")
            precommand = input("URL: ")
            store(precommand, None)
        elif command == "del":
            precommand = input("FP: ")
            try:
                os.remove(precommand)
            except OSError as err:
                print(f"[File Manager/ERROR]: It's powerful, I'm telling you! No just kidding. It's because {err}.")
            else:
                print(f"[File Manager/INFO]: Task succesfully completed! Deleted the {precommand} file.")
        elif command == "del -dir":
            precommand = input("FP: ")
            try:
                os.rmdir(precommand)
            except OSError as err:
                print(f"[File Manager/ERROR]: It's babying, I'm telling you! No just kidding. It's because {err}.")
            else:
                print(f"[File Manager/INFO]: Task succesfully completed! Deleted the {precommand} folder.")
        elif command == "del -tree":
            precommand = input("FP: ")
            try:
                shutil.rmtree(precommand)  # type: ignore
            except shutil.Error as err:  # type: ignore
                print(f"[File Manager/ERROR]: It's a strong tree, I'm telling you! No just kidding. It's because {err}.")
            else:
                print(f"[File Manager/INFO]: Task succesfully completed! oh no you've chopped down the tree at {precommand}.")
        elif command == "clone":
            oldie = input("OFP: ")
            newbie = input("NFP: ")
            try:
                shutil.copyfile(oldie, newbie)  # type: ignore
            except shutil.Error as err:  # type: ignore
                print(f"[File Manager/ERROR]: It's... it's... throwing a tantrum. I'm telling you. No just kidding. It's because {err}.")
        elif command == "move":
            oldie = input("OFP: ")
            newbie = input("NFP: ")
            moveFile(oldie, newbie)
        elif command == "var":
            precommand = input("VAL: ")
            soloclass.vara(precommand)
        elif command == "beans":
            print("[Func Manager]: beans.")
        elif command == "hi":
            hi()
        elif command == "about":
            about()
        else:
            print("[Func Manager/ERROR]: Last time I've checked, I don't think that command is in my book.")
# Check for any errors that may have occoured...
except SyntaxError or NameError:
    print("\n[Overhead/ERROR]: *cough cough* Who- Who messed with the script?!")
    choice = input("> ")
except TypeError as e:
    print("\n[Overhead/ERROR]: *cough cough* Why in the world would you try to combine strings and integers? Or in this case:")
    print(e)
    choice = input("> ")
except SystemError as e:
    print("\n[Runstrapper/ERROR]: *cough cough* Something happened with Python:")
    print(e)
    choice = input("> ")
except Exception as e:
    print("\n[Runstrapper/ERROR]: *cough cough* Whoops! Looks like something went wrong! Press enter to acknowledge the following:")
    print(e)
    choice = input("> ")
    # Create the directory if it doesn't exist
    if not os.path.exists("./crashes"):
        os.makedirs("./crashes")
    # Open the file
    with open(os.path.join("./crashes/", "crashlog.txt"), "w") as f:
        # Write data to the file
        f.write(f"# crash dump for browserOS 0.1.1\n{e}")
finally:
    print("[Runstrapper/INFO]: Bye world!")
    exit(1)
