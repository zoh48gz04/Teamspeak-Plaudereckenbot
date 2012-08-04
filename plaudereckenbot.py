#!/usr/bin/python
import os
try:
    import PyTS3
except:
    print "PyTS3 not found. Aborting"
    os._exit(7)


class pBot:
    def __init__(self, ip, port, username, password, displayname, sid, channellist, cpid):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.sid = sid
        self.channellist = channellist
        self.cpid = cpid
        self.connect(ip, port, username, password, displayname, sid)

    def connect(self, ip, port, username, password, displayname, sid):
        self.teamspeak = PyTS3.ServerQuery(ip, port)
        if self.teamspeak.connect() == False:
            print "Could not connect"
            os._exit(7)
        self.teamspeak.command("login " + username + " " + password)
        self.teamspeak.command("use " + str(sid))
        self.teamspeak.command("clientupdate client_nickname=" + self.teamspeak.string2escaping(displayname))

    def getUserInfo(self):
        self.userInfo = self.teamspeak.command("clientlist")
        self.userInfoArray = list()
        for i in range(len(self.userInfo)):
            if(self.userInfo[i]['cid'] == 152):
                self.userInfoArray.append(self.userInfo[i]['clid'])

    def getChannelUsers(self, cid):
        x = self.teamspeak.command("channellist")
        for i in range(len(x)):
            if(x[i]['cid'] in self.channellist):
                if(x[i]['cid'] == cid):
                    return x[i]['total_clients']

    def addChannel(self):
        #print str(self.channellist[len(self.channellist) - 1])
        y = str("channelcreate channel_name=Plauderecke\s"
                + str(len(self.channellist) + 1) + " channel_order="
                + str(self.channellist[len(self.channellist) - 1]) + "")
        print y
        x = self.teamspeak.command("channelcreate channel_name=Plauderecke\s"
                                   + str(len(self.channellist) + 1) + " channel_order="
                                   + str(self.channellist[len(self.channellist) - 1]) +
                                   " cpid=" + str(self.cpid) + " channel_flag_semi_permanent=1 CHANNEL CODEC")
        print x
        if isinstance(x['cid'], int):
            self.channellist.append(x['cid'])
        print self.channellist
        #print x  # dbg

    def delChannel(self, cid):
        print "deleteChannel: " + str(cid) + " "
        x = self.teamspeak.command("channeldelete cid=" + str(cid) + " force=1")
        self.channellist.remove(cid)
        print x
        #  nothing
