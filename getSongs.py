import glob
import os
import random
from mutagen.mp3 import MP3

_MIN_SONG_NUM_IN_FOLDER_ = 5
_MAX_SONG_NUM_IN_FOLDER_ = 30
_NUM_FOLDER_TO_COPY_     = 10
_MAX_LOOP_COUNT_         = 10

dirList = [
    "R:\\EnglishSongs",
    "R:\\OtherDrives\\Songs2\\EnglishSongs",
    "R:\\OtherDrives\\Songs3\\EnglishSongs"
];

def shouldICopy(dirname):
    songList = glob.glob("*.mp3")
    error = 0
    for song in songList:
        try:
            curFile = MP3(song)
        except:
            error = 1
        try:
            songtitle = curFile["TIT2"]
        except:
            error = 1
    if (error == 0):
        print dirname
    return error



count = 0
while count < _NUM_FOLDER_TO_COPY_:
    d = 0
    loopExit = 0
    dirStkDepth = 0

    baseDir = dirList[random.randint(0, len(dirList) - 1)];
    levelDir = os.path.abspath(baseDir)
    os.chdir(levelDir)
    loopCount = 0
    while (loopExit == 0):
        loopCount = loopCount + 1
        if loopCount > _MAX_LOOP_COUNT_:
            break

        levelArr = os.listdir(levelDir)
        levelLen = len(levelArr)

        tmp = os.path.join(levelDir, levelArr[random.randint(0, levelLen - 1)])
        while True:
            tmp = os.path.join(levelDir, levelArr[random.randint(0, levelLen - 1)])
            if (os.path.isdir(tmp) == False):
                levelDir = os.path.abspath(os.curdir)
            else:
                break
            loopCount = loopCount + 1
            if loopCount > _MAX_LOOP_COUNT_:
                break

        if (os.path.isdir(tmp) == False):
            continue
        levelDir = tmp
        os.chdir(levelDir)
        dirStkDepth = dirStkDepth + 1

        mp3List  = glob.glob("*.mp3")
        mp3Count = len(mp3List)

        if ((mp3Count > _MIN_SONG_NUM_IN_FOLDER_) and (mp3Count < _MAX_SONG_NUM_IN_FOLDER_)):
            retVal = shouldICopy(os.path.abspath(levelDir))
            if (0 == retVal):
                count = count + 1
            loopExit = 1

    while (dirStkDepth > 2):
        os.chdir("../")
        dirStkDepth = dirStkDepth -1




#songtitle = curFile["TIT2"]
#artist    = curFile["TPE1"]
#album     = curFile["TALB"]
#print songtitle
#print artist
#print album
