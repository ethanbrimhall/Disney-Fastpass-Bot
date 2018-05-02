from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import smtplib
import pymysql

akRides = ["Avatar Flight of Passage", "Na'vi River Journey", "DINOSAUR", "Expedition Everest - Legend of the Forbidden Mountain", "Festival of the Lion King", "Finding Nemo - The Musical", "It's Tough to be a Bug!", "Kali River Rapids", "Kilimanjaro Safaris", "Meet Favorite Disney Pals", "Primeval Whirl", "Rivers of Light"]
mkRides = ["The Barnstormer", "Big Thunder Mountain Railroad", "Buzz Lightyear's Space Ranger Spin", "Dumbo the Flying Elephant", "Enchanted Tales with Belle", "Haunted Mansion", "it's a small world", "Jungle Cruise", "Mad Tea Party", "The Magic Carpets of Aladdin", "The Many Adventures of Winnie the Pooh", "Meet Ariel at Her Grotto", "Meet Cinderella", "Meet Mickey", "Meet Rapunzel", "Meet Tinker Bell", "Mickey's PhilharMagic", "Monsters, Inc. Laugh Floor", "Peter Pan's Flight", "Pirates of the Caribbean", "Space Mountain", "Splash Mountain", "Tomorrowland Speedway", "Journey of The Little Mermaid", "Seven Dwarfs Mine Train"]
hsRides = ["Beauty and the Beast-Live", "Fantasmic!", "Rock 'n' Roller Coaster", "Disney Junior - Live", "Frozen Sing-Along", "Epic Stunt Spectacular!", "Muppet*Vision 3D", "Star Tours", "The Twilight Zone Tower", "Voyage of The Little Mermaid", "Toy Story Mania!"]
eRides = ["Frozen Ever After", "IllumiNations", "Soarin'", "Test Track", "Short Film Festival", "Journey Into Imagination", "Living with the Land", "Meet Disney Pals", "Mission: SPACE", "Nemo & Friends", "Spaceship Earth", "Turtle Talk With Crush"]

parkRides = [mkRides, eRides, hsRides, akRides]

x = False

print("Magic Kingdom: 1 | Epcot: 2 | Hollywood Studios: 3 | Animal Kingdom: 4")
print("")
park = input("What park are you going to: ")
while park != "1" and park != "2" and park != "3" and park != "4":
    park = input("Invalid Choice... What park are you going to: ")

print("\n")
if park == "1":
    print("The Barnstormer: 1 | Big Thunder Mountain Railroad: 2 | Buzz Lightyear's Space Ranger Spin: 3 | Dumbo the Flying Elephant: 4 | Enchanted Tales with Belle: 5 | Haunted Mansion: 6 | it's a small world: 7 | Jungle Cruise: 8 | Mad Tea Party: 9 | The Magic Carpets of Aladdin: 10 | The Many Adventures of Winnie the Pooh: 11 | Meet Ariel at Her Grotto: 12 | Meet Cinderella: 13 | Meet Mickey: 14 | Meet Rapunzel: 15 | Meet Tinker Bell: 16 | Mickey's PhilharMagic: 17 | Monsters, Inc. Laugh Floor: 18 | Peter Pan's Flight:19 | Pirates of the Caribbean: 20 | Space Mountain: 21 | Splash Mountain: 22 | Tomorrowland Speedway: 23 | Journey of The Little Mermaid: 24 | Seven Dwarfs Mine Train: 25")
    ride = input("Choose a Ride: ")
    while ride not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]:
        ride = input("Choose a Ride: ")
    ride = mkRides[int(ride)-1]
elif park == "2":
    print("Frozen Ever After: 1 | IllumiNations: 2 | Soarin': 3 | Test Track: 4 | Short Film Festival: 5 | Journey Into Imagination: 6 | Living with the Land: 7 | Meet Disney Pals: 8 | Mission: SPACE: 9 | Nemo & Friends: 10 | Spaceship Earth: 11 | Turtle Talk With Crush: 12")
    ride = input("Choose a Ride: ")
    while ride not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        ride = input("Choose a Ride: ")
    ride = eRides[int(ride)-1]
elif park == "3":
    print("Beauty and the Beast-Live: 1 | Fantasmic!: 2 | Rock 'n' Roller Coaster: 3 | Disney Junior - Live: 4 | Frozen Sing-Along: 5 | Epic Stunt Spectacular!: 6 | Muppet*Vision 3D: 7 | Star Tours: 8 | The Twilight Zone Tower: 9 | Voyage of The Little Mermaid: 10 | Toy Story Mania!: 11")
    ride = input("Choose a Ride: ")
    while ride not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
        ride = input("Choose a Ride: ")
    ride = hsRides[int(ride)-1]
elif park == "4":
    print("Avatar Flight of Passage: 1 | Na'vi River Journey: 2 | DINOSAUR: 3 | Everest: 4 | Festival of the Lion King: 5 | Finding Nemo - The Musical: 6 | It's Tough to be a Bug!: 7 | Kali River Rapids: 8 | Kilimanjaro Safaris: 9 | Meet Favorite Disney Pals: 10 | Primeval Whirl: 11 | Rivers of Light: 12")
    print("")
    ride = input("Choose a Ride: ")
    while ride not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        ride = input("Choose a Ride: ")
    ride = akRides[int(ride)-1]

print("")
time = input("Select A Time: ")
timeZone = input("AM or PM: ")

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
chrome_path = r"/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.get("https://disneyworld.disney.go.com/fastpass-plus/")
while x == False:
    try:
        driver.find_element_by_xpath("""//*[@id="fastPasslandingPage"]/div[3]/div[1]/div/div/div/div""").click()
        x = True
    except:
        x = False

x = False
while x == False:
    try:
        driver.find_element_by_xpath("""//*[@id="loginPageUsername"]""").send_keys("")
        driver.find_element_by_xpath("""//*[@id="loginPagePassword"]""").send_keys("")
        driver.find_element_by_xpath("""//*[@id="loginPageSubmitButton"]/span""").click()
        x = True
    except:
        x = False
x = False
while x == False:
    try:
        driver.find_element_by_xpath("""//*[@id="guest-guestIDGoesHere-unselected"]/div""").click()
        x = True
    except:
        try:
            driver.find_element_by_xpath("""//*[@id="fastPasslandingPage"]/div[4]/div/div[1]/div/div""").click()
            x = True
        except:
            x = False

x = False
while x == False:
    try:
        driver.find_element_by_xpath("""//*[@id="guest-guestIDGoesHere-unselected"]/div""").click()
        driver.find_element_by_xpath("""//*[@id="guest-guestIDGoesHere-unselected"]/div""").click()
        driver.find_element_by_xpath("""//*[@id="guest-guestIDGoesHere-unselected"]/div""").click()
        driver.find_element_by_xpath("""//*[@id="selectPartyPage"]/div[3]/div/div[2]/div""").click()
        x = True
    except:
        x = False

print("Select A Date On Screen!")
print("")
x = False
while x == False:
    try:
        if park == "1":
            driver.find_element_by_xpath("""//*[@id="selectParkContainer"]/div[2]/div[1]/div/div[1]/img""").click()
        elif park == "2":
            driver.find_element_by_xpath("""//*[@id="selectParkContainer"]/div[2]/div[2]/div/div[1]/img""").click()
        elif park == "3":
            driver.find_element_by_xpath("""//*[@id="selectParkContainer"]/div[2]/div[3]/div/div[1]/img""").click()
        elif park == "4":
            driver.find_element_by_xpath("""//*[@id="selectParkContainer"]/div[2]/div[4]/div/div[1]/img""").click()
        x = True
    except:
        x = False

x = False
isFound = False
breakLoop = False
whichTime = 1
timesChecked = 1

while isFound == False:
    sleep(5)
    if park == "1":
        try:
            for aride in mkRides:
                num =  mkRides.index(aride) + 1
                try:
                    element = driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[2]/div[2]/div[""" + str(num) + """]""")
                    
                    if ride in element.text:
                        for x in range(1, 4):
                            timeText = driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[2]/div[2]/div[""" + str(num) + """]/div/div[2]/div/div[""" + str(x) + """]""")
                            
                            if len(timeText.text) == 7:
                                rideTime = timeText.text[:1]
                                rideTimeZone = timeText.text[5:]
                            if len(timeText.text) == 8:
                                rideTime = timeText.text[:2]
                                rideTimeZone = timeText.text[6:]
                            if time == rideTime and rideTimeZone == timeZone:
                                isFound = True
                                breakLoop = True
                                print(element.text)
                                print('Found ' + ride + ' in ' + str(timesChecked) + ' tries!')
                                driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[2]/div[2]/div[""" + str(num) + """]/div/div[2]/div/div[""" + str(x) + """]""").click()
                                sleep(3)
                                driver.find_element_by_xpath("""//*[@id="reviewConfirmButton"]/div""").click()
                        
                             
                except:
                    breakLoop = True
                if breakLoop == True:
                    break
                
            

        except:
            pass
    else:
        try:
            for aride in parkRides[int(park)-1]:
                num =  parkRides[int(park)-1].index(aride) + 1
                try:
                    element = driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[2]/div[2]/div[""" + str(num) + """]""")
                    
                    if ride in element.text:
                        for x in range(1, 4):
                            timeText = driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[2]/div[2]/div[""" + str(num) + """]/div/div[2]/div/div[""" + str(x) + """]""")
                            
                            if len(timeText.text) == 7:
                                rideTime = timeText.text[:1]
                                rideTimeZone = timeText.text[5:]
                            if len(timeText.text) == 8:
                                rideTime = timeText.text[:2]
                                rideTimeZone = timeText.text[6:]
                            if time == rideTime and rideTimeZone == timeZone:
                                isFound = True
                                breakLoop = True
                                print(element.text)
                                print('Found ' + ride + ' in ' + str(timesChecked) + ' tries!')
                                driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[2]/div[2]/div[""" + str(num) + """]/div/div[2]/div/div[""" + str(x) + """]""").click()
                                sleep(3)
                                driver.find_element_by_xpath("""//*[@id="reviewConfirmButton"]/div""").click()
                        
                             
                except:
                    breakLoop = True
                if breakLoop == True:
                    break
                
            

        except:
            pass
        try:
            breakLoop = False
            for aride in parkRides[int(park)-1]:
                num =  parkRides[int(park)-1].index(aride) + 1
                try:
                    element = driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[3]/div[2]/div[""" + str(num) + """]""")
                    
                        
                    if ride in element.text:
                        for x in range(1, 4):
                            timeText = driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[3]/div[2]/div[""" + str(num) + """]/div/div[2]/div/div[""" + str(x) + """]""")
                            if len(timeText.text) == 7:
                                rideTime = timeText.text[:1]
                                rideTimeZone = timeText.text[5:]
                            if len(timeText.text) == 8:
                                rideTime = timeText.text[:2]
                                rideTimeZone = timeText.text[6:]
                            if time == rideTime and rideTimeZone == timeZone:
                                isFound = True
                                breakLoop = True
                                print(element.text)
                                print('Found ' + ride + ' in ' + str(timesChecked) + ' tries!')
                                driver.find_element_by_xpath("""//*[@id="selectExperienceExperiencesList"]/div[3]/div[2]/div[""" + str(num) + """]/div/div[2]/div/div[""" + str(x) + """]""").click()
                                sleep(3)
                                driver.find_element_by_xpath("""//*[@id="reviewConfirmButton"]/div""").click()
                        
                except:
                    breakLoop = True
                if breakLoop == True:
                    break
                
                

        except:
            pass
    
                
            
    if isFound == False:
        breakLoop = False
        timesChecked += 1
        if whichTime == 1:
            driver.find_element_by_xpath("""//*[@id="selectExperienceTimeFilter"]/div/div[2]/div""").click()
            whichTime = 2
        elif whichTime == 2:
            driver.find_element_by_xpath("""//*[@id="selectExperienceTimeFilter"]/div/div[3]/div""").click()
            whichTime = 3
        elif whichTime == 3:
            driver.find_element_by_xpath("""//*[@id="selectExperienceTimeFilter"]/div/div[1]/div""").click()
            whichTime = 1
        
    
    

