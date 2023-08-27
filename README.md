# Chaos-Mod-Twitch-Integration
Twitch Integration For [Teardown Chaos Mod](https://github.com/NLferdiNL/Teardown-Chaos-Mod)

Exe files created using auto-py-to-exe, but source also included.

To get started download the repo using [this link](https://github.com/NLferdiNL/Chaos-Mod-Twitch-Integration/archive/refs/heads/main.zip) or the download button on the code dropdown.

You can unzip this where ever you want. You can even delete the .py files if you don't want them, they are merely there as source files and not required.
To get setup you want to run options.exe first, this is a one time setup to get started on the mod.
You'll need to enter:
  - Your twitch channel username
  - Your twitch oauth (used to pull your chat only) You can create one here: [https://twitchapps.com/tmi/](https://twitchapps.com/tmi/)
  - The chaos mod folder in your teardown mods either a local copy or in steamapps\workshop\content\1167630\2433702881 (depending on where you installed Teardown) This is where the program creates an xml file for the game to read the vote data through.
  - Your Teardown savegame.xml (found in C:\Users\user\AppData\Local\Teardown\) this is used for the twitch chat program to receive reset calls from the mod and is only ever read. NO WRITES. (Always a good idea to make backups though.)

When this is done it should have created a file called twitchchatsettings.txt. 
DO NOT send this file to ANYONE. This file contains that oauth key and is very dangerous. 
If you accidently leaked this key go to your (Twitch App Connections)[https://www.twitch.tv/settings/connections] and remove Twitch Chat OAuth Token Generator. 
You can generate a new one if need be.

Now run GetTwitchChat.exe, start up your game. (Make sure to enable twitch integration ingame in the options menu, from your mod list) Then once ingame you could start seeing the votes appear.

# Credits
A massive shout out to [MutatedOnion](https://steamcommunity.com/profiles/76561199083584422) for doing most of the work on this. I only did the finishing touches.
