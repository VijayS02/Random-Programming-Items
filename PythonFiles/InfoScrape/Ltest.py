
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://lionel.kgv.edu.hk/kgv-additions/Register3/RoomReport.php")
driver.find_element_by_xpath("//INPUT[@id='username']").send_keys("18sambamurthyv2")
driver.find_element_by_xpath("//INPUT[@id='password']").send_keys("What&password")
driver.find_element_by_xpath("//INPUT[@type='submit']").click()
print("Ok 0")
info = driver.find_elements_by_xpath("(//TD[@align='center'])")
#print(text.get_attribute("text"))
print("Ok 1")
titles = driver.find_elements_by_xpath("//TH")
print("Ok 2")
rooms = []
pt = False
for elem in titles:
    if(elem.get_attribute("innerHTML")=="AS1"):
        pt = True
    if(pt == True):
        rooms.append([elem.get_attribute("innerHTML"),[]])
count = 0;
room = count;
for elem in info:
    room = count//60;
    print(elem.get_attribute("innerHTML"))
    if(elem.get_attribute("innerHTML").replace("<small>","").replace("</small>","") != ""):
        rooms[room][1].append(elem.get_attribute("innerHTML").replace("<small>","").replace("</small>",""))
    else:
        rooms[room][1].append("Empty")

    count += 1


for e in range(0,len(rooms)):
    rooms[e][1] = ','.join(rooms[e][1])
    rooms[e] = '|'.join(rooms[e])
rooms = '\n'.join(rooms)
print(rooms)
driver.close()
safeFile = open("info1.txt",'w')
safeFile.write(rooms)
safeFile.close()
print("Update complete.")