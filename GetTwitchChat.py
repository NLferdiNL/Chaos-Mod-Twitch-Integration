import ctypes
import irc.bot
import requests
import threading
import sys
from PyQt5 import QtCore
from pathlib import Path

def MessageBox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

if not Path("twitchchatsettings.txt").is_file():
    MessageBox("Warning", "Couldn't find the settings. Have you started the options program?", 1)
    sys.exit()

settingsFile = open("twitchchatsettings.txt", 'r')
settingsContent = settingsFile.readlines()

print("Loading Teardown Chaos Mod Twitch Integration")

# Replace these with your own Twitch credentials
USERNAME = settingsContent[0].rstrip()
TOKEN = settingsContent[1].rstrip()
PathToMod = settingsContent[2].rstrip()
PathToSave = settingsContent[3].rstrip()

CHANNEL = USERNAME # also twitch user Name if you dont have a different @ idk

VOTES = {}

TOTALVOTES = [0, 0, 0, 0]
TOTALVOTESCOMBINED = 0

RESETVOTES = False

VOTESTEP = 1

def ResetVotes():
    global VOTES
    global TOTALVOTES
    global TOTALVOTESCOMBINED
    
    VOTES = {}
    TOTALVOTES = [0, 0, 0, 0]
    TOTALVOTESCOMBINED = 0
    
    print("Vote count reset!")

    global RESETVOTES
    RESETVOTES = False  

def ResetVotesCheck():
    votestepWord1 = 'chaosmodtwitchvotestep value="1"'
    votestepWord2 = 'chaosmodtwitchvotestep value="2"'

    global VOTESTEP
    
    with open(settingsContent[3].rstrip(), 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find(votestepWord1) != -1 and VOTESTEP == 2:
                ResetVotes()
                VOTESTEP = 1
            elif line.find(votestepWord2) != -1 and VOTESTEP == 1:
                ResetVotes()
                VOTESTEP = 2

def receiveFromTeardown():
    if RESETVOTES:
        ResetVotesCheck()
        
    threading.Timer(0.5, receiveFromTeardown).start()


def sendToTeardown():
    threading.Timer(1.0, sendToTeardown).start()
    with open(PathToMod + "\\twitchchat.xml", 'w') as xml:
        xml.write(f'<prefab version="1.3.0"><group><body tags="twitch" dynamic="true" desc="{TOTALVOTES} {TOTALVOTESCOMBINED}"/></group></prefab>')
    print("Votes updated!")
    print(TOTALVOTES)

RESETVOTES = True
receiveFromTeardown()
sendToTeardown()

def file_changed(path):
    global RESETVOTES
    RESETVOTES = True 

def startFSWatch():
    app = QtCore.QCoreApplication(sys.argv)
    
    fs_watcher = QtCore.QFileSystemWatcher()

    fs_watcher_result = fs_watcher.addPath(settingsContent[3].rstrip())

    if fs_watcher_result:
        print("Save game located!")
    else:
        print("Failed to locate save game!")
        sys.exit()

    
    print("Starting file watch!")
    fs_watcher.fileChanged.connect(file_changed)
    
    app.exec_()


fsThread = threading.Thread(target=startFSWatch)
fsThread.start()

# Define a function to handle incoming chat messages
def handle_message(connection, event):
    message = event.arguments[0]
    username = event.source.split('!')[0]
    print(f'{username}: {message}')

    if VOTESTEP == 1:
        if message == "1" or message == "2" or message == "3" or message == "4":
            message = int(message) - 1
        else:
            return
    elif VOTESTEP == 2:
        if message == "5" or message == "6" or message == "7" or message == "8":
            message = int(message) - 1
            message = message - 4
        else:
            return

    if username in VOTES:
        TOTALVOTES[VOTES[username]] = TOTALVOTES[VOTES[username]] - 1
    else:
        global TOTALVOTESCOMBINED
        TOTALVOTESCOMBINED = TOTALVOTESCOMBINED + 1

    VOTES[username] = message
    TOTALVOTES[message] = TOTALVOTES[message] + 1

    print(TOTALVOTES)
    
# Create a Twitch bot
class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        self.username = username
        self.token = token
        self.channel = '#' + channel
        self.twitch_server = 'irc.chat.twitch.tv'
        self.twitch_port = 6667
        irc.bot.SingleServerIRCBot.__init__(self, [(self.twitch_server, self.twitch_port, f'oauth:{token}')], username, username)

    def on_welcome(self, connection, event):
        print("Connected to your chat!")
        connection.join(self.channel)

    def on_pubmsg(self, connection, event):
        handle_message(connection, event)

# Start the bot
bot = TwitchBot(USERNAME, TOKEN, CHANNEL)
bot.start()

