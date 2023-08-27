import sys
from PyQt5 import QtCore

app = QtCore.QCoreApplication(sys.argv)

def file_changed(path):
    word = '<chaosmodtwitchreset value="1"/>'
    with open(settingsContent[3].rstrip() + "/savegame.xml", 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find(word) != -1:
                print("AHH")
                

settingsFile = open("twitchchatsettings.txt", 'r')
settingsContent = settingsFile.readlines()

fs_watcher = QtCore.QFileSystemWatcher()

fs_watcher_result = fs_watcher.addPath(settingsContent[3].rstrip() + "/savegame.xml")

print(fs_watcher_result)

fs_watcher.fileChanged.connect(file_changed)

#fs_watcher.connect(fs_watcher, QtCore.SIGNAL('directoryChanged(QString)'), directory_changed)
#fs_watcher.connect(fs_watcher, QtCore.SIGNAL('fileChanged(QString)'), file_changed)

sys.exit(app.exec_())
