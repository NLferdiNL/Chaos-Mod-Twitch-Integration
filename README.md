# Chaos-Mod-Twitch-Integration
Twitch Integration For Teardown Chaos Mod

Exe files created using auto-py-to-exe, but source also included.

To get started download the repo using [this link](https://github.com/NLferdiNL/Chaos-Mod-Twitch-Integration/archive/refs/heads/main.zip) or the download button on the code dropdown.

You can unzip this where ever you want. You can even delete the .py files if you don't want them, they are merely there as source files and not required.
To get setup you want to run options.exe first, this is a one time setup to get started on the mod.
You'll need to enter:
  - Your twitch channel username
  - Your twitch oauth (used to pull your chat only) You can create one here: [https://twitchapps.com/tmi/](https://twitchapps.com/tmi/)
  - The chaos mod folder in your teardown mods either a local copy or in steamapps\workshop\content\1167630\2433702881 (depending on where you installed Teardown) This is where the program creates an xml file for the game to read the vote data through.
  - Your Teardown savegame.xml (found in C:\Users\user\AppData\Local\Teardown\) this is used for the twitch chat program to receive reset calls from the mod and is only ever read. NO WRITES. (Always a good idea to make backups though.)

# Credits
A massive shout out to [MutatedOnion](https://steamcommunity.com/profiles/76561199083584422) for doing most of the work on this. I only did the finishing touches.
