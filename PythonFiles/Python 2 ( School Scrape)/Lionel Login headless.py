paswd = "What&password"









import cookielib, urllib, urllib2, getpass, StringIO
from lxml import etree,html  
cookieJar = cookielib.LWPCookieJar()
opener = urllib2.build_opener(
    urllib2.HTTPCookieProcessor(cookieJar),
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0))

opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")]

forms = {"username":"18sambamurthyv2" ,
         "password": paswd
         }
urllib2.install_opener(opener)
print("Logging in")
data = urllib.urlencode(forms)
req = urllib2.Request('https://lionel2.kgv.edu.hk/login/index.php',data)

res = opener.open(req)
parser = etree.HTMLParser()
print("Logged in.")




"""
dataz = []
dataz.append("SID Name Email TimeTable Homework")


for i in [9082]:
   try:
    req1 = urllib2.urlopen("https://lionel2.kgv.edu.hk/local/mis/students/summary.php?sid="+str(i))   
    login_html = req1.read)(
    tree   = etree.parse(StringIO.StringIO(login_html), parser)
    root = tree.getroot()
    node =tree.xpath('//span[@id=\'box2\']')[0]
    tt = tree.xpath('//input[@id=\'gcal\']')[0]
    hw = tree.xpath('//input[@id=\'gcal2\']')[0]
    data =  ''.join(etree.tostring(e) for e in node)
    dataz.append(str(i) + " " + data[data.index("</h4>")+5:data.index("<br/>")] + " " + data[data.index("<br/>") + 5:data.index("<a")] + " " + str(tt.get('value')) + " " + str(hw.get('value')))
    print(str(i) + " " + data[data.index("</h4>")+5:data.index("<br/>")] + " " + data[data.index("<br/>") + 5:data.index("<a")])
   except:
       print(str(i) + " not connected. OR ERROR!")
#findat = '\n'.join(dataz)
#saveFile = open('data.txt', 'w')
#saveFile.write(str(findat))
#saveFile.close()
"""


