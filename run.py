#!/usr/bin/python
import plaudereckenbot
import time

# IP of the TS3 server
IP = ""

# Query port of the TS3 server
PORT = 10011

# Username for the query
USERNAME = "serveradmin"

# Password for the user specified above
PASSWORD = ""

# Displayname. Name visibible to the users
DISPLAYNAME = "Plauderecken-Bot"

# The ID of the virtual server to run on
SID = 1

# Which channels should be treated as the original channels
CHANNELLIST = [151, 152, 153]

# Channel ID of the parent channel. Created channels are children of this
CPID = 54

#########################################################################


pBot = plaudereckenbot.pBot(IP, PORT, USERNAME, PASSWORD, DISPLAYNAME,
    SID, CHANNELLIST, CPID)
while 1:
    emptyRooms = 0
    pBot.getUserInfo()
    channelUserCount = list()
    print "userInfo: " + str(pBot.userInfoArray)
    for i in range(len(pBot.channellist)):
        channelUserCount.append(pBot.getChannelUsers(pBot.channellist[i]))
    for i in range(len(channelUserCount)):
        if(channelUserCount[i] > 0):
            channelUserCount[i] = True
        else:
            emptyRooms = emptyRooms + 1
    print "ChanUserCount: " + str(channelUserCount)
    print "lenSetUserCount: " + str(len(set(channelUserCount)) == 1
    and channelUserCount[0] == True)
    if len(set(channelUserCount)) == 1 and channelUserCount[0] == True:
        pBot.addChannel()
    print "emptyRooms: " + str(emptyRooms)
    if emptyRooms > 1:
        for i in reversed(range(len(pBot.channellist))):
            if channelUserCount[i] == 0:
                if pBot.channellist[i] not in ORIGINALCHANNELS:
                    pBot.delChannel(pBot.channellist[i])
                    break
    time.sleep(5)