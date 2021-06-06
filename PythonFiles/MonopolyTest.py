import random


class Cards:

    def __init__(self,cardInfo):
        """
        Sets up the cards
        :param cardInfo: Array containing card information.
        """
        self.name = cardInfo[0]
        self.price = cardInfo[1]
        self.group = cardInfo[2]
        self.groupID = cardInfo[3]
        self.rent = cardInfo[4]
        self.rentWith1House = cardInfo[5]
        self.rentWith2House = cardInfo[6]
        self.rentWith3House = cardInfo[7]
        self.rentWith4House = cardInfo[8]
        self.rentWithHotel = cardInfo[9]
        self.houseCost = cardInfo[10]
        self.mortgageVal = cardInfo[11]
        self.color = colors[self.group]
        if(self.group >= 3):
            """
            FOR DEBUGGING: 
            if(self.name == 'Lamma Island'):
                self.HouseNumber = 1
            else:
            """
            self.HouseNumber = 0
            # 1 = 1 house, 2 = 2 house, 3 = 3 house, 4 = 4 house, 5 = hotel
    def cardPrinter(self):
        """
        prints the card with detail.
        :return: nothing.
        """
        if (self.group >= 3):
            print('----------------------------------')
            print('|', self.name, '                    |')
            print('| Price: $', self.price, '              |')
            print('| Color: ', colors[self.group], '           |')
            print('| ID   : ', self.groupID, '           |')
            print('| Rent: $', self.rent, '               |')
            print('| With 1 house: $', self.rentWith1House, '       |')
            print('| With 2 house: $', self.rentWith2House, '       |')
            print('| With 3 house: $',self.rentWith3House, '       |')
            print('| With 4 house: $', self.rentWith4House, '       |')
            print('| Hotel: $', self.rentWithHotel, '              |')
            print('| One house cost: $', self.houseCost, '     |')
            print('| Mortgage: $', self.mortgageVal, '          |')
        elif (self.group == 1):
            print('----------------------------------')
            print('|', self.name, '                    |')
            print('| Color: ', colors[self.group], '           |')
            print('| ID   : ', self.groupID, '           |')
            print('| With 1 owned: $', self.rentWith1House, '               |')
            print('| With 2 owned: $', self.rentWith2House, '       |')
            print('| With 3 owned: $', self.rentWith3House, '       |')
            print('| With 4 owned: $', self.rentWith4House, '       |')
            print('| Mortgage: $', self.mortgageVal, '          |')
        elif (self.group == 2):
            print('----------------------------------')
            print('|', self.name, '                    |')
            print('| Color: ', colors[self.group], '           |')
            print('| ID   : ', self.groupID, '           |')
            print('| With 1 owned:', self.rentWith1House, ' times dice roll.  |')
            print('| With 2 owned:', self.rentWith2House, ' times dice roll.  |')
            print('| Mortgage: $', self.mortgageVal, '          |')
        elif (self.group == 0):
            print('----------------------------------')
            print('|', self.name, '                    |')
            print('|', specials[self.groupID][0], '|')

class player:
    def __init__(self,name):
        """
        sets up a player object.
        :param name: The name of the player.*To be inputted*
        """
        self.name = name
        self.position = 0
        self.money = startingMoney
        self.properties = cardNoProps(board)
        """
        DEBUGGING ONLY:
        if(self.name != 'vj'):
            self.properties = cardNoProps(board)
        else:
            self.properties = ['0|0|0|0', '0|0', '0|0', '1|1|1', '0|0|0', '0|0|0', '0|0|0', '0|0|0', '0|0|0', '0|0']
        """
        self.bankrupt = False

    def addSubMoney(self,amount):
        """
        adds money to the players account.
        :param amount: Amount of money to be added/deducted.
        :return: nothing.
        """
        self.money = self.money + amount

startingMoney = 15000
addGoMoney = 2000
# format = Name,Price,Group,id in group,Rent,With 1 hs, 2 hs, 3hs , 4hs , hotel, one house cost, mortgage value
boardRaw = [['Go',0,0,0,0,0,0,0,0,0,0,0],['Community Chest',0,0,1,0,0,0,0,0,0,0,0],['Chance',0,0,2,0,0,0,0,0,0,0,0],['Stanley Jail',0,0,3,0,0,0,0,0,0,0,0],['Free parking',0,0,4,0,0,0,0,0,0,0,0],['Go to Stanley Jail',0,0,5,0,0,0,0,0,0,0,0],['Salary Tax',0,0,6,0,0,0,0,0,0,0,0],['Income tax',0,0,7,0,0,0,0,0,0,0,0],['Airport Station',2000,1,0,250,500,1000,2000,0,0,0,1000],['Tsing Yi Station',2000,1,1,250,500,1000,2000,0,0,0,1000],['Kowloon Station',2000,1,2,250,500,1000,2000,0,0,0,1000],['Hong Kong Station',2000,1,3,250,500,1000,2000,0,0,0,1000],['China Light and Power',1500,2,0,40,100,0,0,0,0,0,750],['Water works HK',1500,2,1,40,100,0,0,0,0,0,750],['Chep Lak Kok',600,3,0,20,100,300,900,1600,2500,500,300],['Lantau Island',600,3,1,40,200,600,1600,3200,4500,500,300],['Ngong Ping',1000,4,0,60,300,900,2700,4000,5500,500,500],['Cheng Chau',1000,4,1,60,300,900,2700,4000,5500,500,500],['Lamma Island',1000,4,2,60,300,900,2700,4000,5500,500,500],['Lo Wu',1400,5,0,100,500,1500,4500,6200,7500,1000,700],['Tin Shui Wai',1400,5,1,100,500,1500,4500,6250,7500,1000,700],['Sham Tseng',1600,5,2,120,600,1800,5000,7000,9000,1000,800],['Kwai Chung',1800,6,0,140,700,2000,5500,7000,9000,1000,900],['Sha Tin',1800,6,1,140,700,2000,5500,7000,9500,1000,900],['Tsueng Kwan O',2000,6,2,160,800,2200,6000,8000,10000,1000,1000],['Lei Yu Mun',2200,7,0,180,900,2500,7000,8750,10500,1500,1100],['Wong Tai Sin',2200,7,1,180,900,2500,7000,8750,10500,1500,1100],['Kowloon Tong',2400,7,2,200,1000,3000,7500,9250,11000,1500,1200],['Kwun Tong',2600,8,0,220,1100,3300,8000,9750,11500,1500,1300],['Mong Kok',2600,8,1,220,1100,3300,8000,9750,11500,1500,1300],['Tsim Sha Tsui',2800,8,2,240,1200,3600,8500,10250,12000,1500,1400],['Causeway Bay',3000,9,0,260,1300,3900,9000,11000,12750,2000,1500],['Cyberport',3000,9,1,260,1300,3900,9000,11000,12750,2000,1500],['Central',3200,9,2,280,1500,4500,10000,12000,14000,2000,1600],['Repulse Bay',3500,10,0,350,1750,5000,11000,13000,15000,2000,1750],['The Peak',4000,10,1,500,2000,6000,14000,17000,20000,2000,2000]]
colors = ['None','Stations','Utilities','Brown','Light Blue','Purple','Orange','Red','Yellow','Green','Blue']
board = []
for i in boardRaw:
    board.append(Cards(i))

# format = Description, Value added, takes card, goes to jail
specials = [['Collect $2000 every pass.','2000',0,0],['The player takes a card from the top of the respective pack and performs the instruction given on the card.',0,1,0],['The player takes a card from the top of the respective pack and performs the instruction given on the card.',0,1,0],['The player is "Just Visiting". No penalty applies.',0,0,0],['Nothing happens.',0,0,0],['The player goes to Jail.',0,0,1],['The player must pay $750.','-750',0,0],['The player must pay 10% of their total assets or $2000.','-2000/0.1',0,0]]
layout = [board[0],board[14],board[1],board[15],board[7],board[8],board[16],board[2],board[17],board[18],board[3],board[19],board[12],board[20],board[21],board[9],board[22],board[1],board[23],board[24],board[4],board[25],board[26],board[27],board[10],board[28],board[29],board[13],board[30],board[5],board[31],board[32],board[1],board[33],board[11],board[2],board[34],board[6],board[35],]


def trade(plyr,players,cards):
    temp = players
    print("Which player would you like to trade with:")
    for i in temp:
        if(i == plyr):
            temp.pop(temp.index(i))
            break
        else:
            print(i.name)
    userTradePerson = raw_input('')
    tradePerson = 0
    for i in temp:
        if(i.name == userTradePerson):
            tradePerson = i
            break
    if(raw_input('Would you like to trade properties? Yes/No').lower() == 'yes'):
        ownedProps = findOwnedProperties(plyr,cards)
        ownedPropsName = []
        print("Properties you own: ")
        for i in ownedProps:
            print(i.name)
            ownedPropsName.append(i.name)
        while True:
            cProp = raw_input("Which property would you like to trade?")
            if(cProp in ownedPropsName):
                curCard = ownedProps[ownedPropsName.index(cProp)]
                tradeHouse(plyr,tradePerson,curCard)
            if(raw_input("Trade more?")== True):
                    pass

def tradeHouse(Oplyr,Nplyr1,card):
    group = card.group
    groupID = card.groupID
    changeProp(Oplyr,group,groupID,0)
    changeProp(Oplyr, group, groupID, 1)

def changeProp(plyr,group,groupID,buyVal):
    temp = 0
    CurrentGroup = 0
    for i in plyr.properties:
        if(temp == group):
            CurrentGroup = i.split('|')
        temp += 1
    CurrentGroup[groupID] = buyVal



def getTradeItems(plyr,cards):
    pass



def findProp(cards,group,id):
    for i in cards:
        if(i.group == group and i.groupID == id):
            return i


def findOwnedProperties(plyr,cards):
    ownedProperties = []
    for i in plyr.properties:
        for x in i.split('|'):
            if(x == '1'):
                ownedProperties.append(findProp(cards,(plyr.properties).index(i) -1,(i.split('|')).index(x)))
    return ownedProperties



def Turn(plyr,board,brdlyt,players):
    """
    Does one turn for a given player.
    :param plyr: Player object.
    :param board: Board containing card objects.
    :param layout: Layout array.
    :param players: Player array with player objects.
    :return:
    """
    posCalc(roller(),plyr,brdlyt)
    currentPos = curPos(plyr,brdlyt)
    if(isOwnedByPlyr(plyr,currentPos)):
        pass
    elif(isOwned(players,currentPos)):
        plyr.addSubMoney((rentCalc(currentPos)*-1))
    else:
        buyBool = raw_input("What would you like to do? Buy or pass?")
        if buyBool.lower() == 'buy':
            buyProp(plyr,brdlyt,players)

    if (raw_input('Buy hotel?Y/N').lower() == 'Y'):
        buyHouse(plyr, board )



def rentCalc(card):
    if(card.house1 == False):
        return card.rent
    elif(card.hotel == True):
        return card.rentWithHotel
    elif(card.house4 == True):
        return card.rentWith4House
    elif(card.house3 == True):
        return card.rentWith3House
    elif(card.house2 == True):
        return card.rentWith2House
    else:
        return card.rentWith1House
#def SellProperties()

def playerSetup():
    """
    sets up the player list.
    :return: nothing.
    """
    players = []
    nPlayers = int(input("How many players? \n"))
    for i in range(0,nPlayers):
        print("Player " + str((i+1)) + " name:")
        players.append(player(raw_input("")))
    return players

def boardPrinter(lst):
    """
    Prints the layout of the board in order.
    :param lst: Layout array with board objects filled in.
    :return:
    """
    for i in layout:
        print(i.name)
boardPrinter(layout)

def checker(lst,length):
    """
    Checks by printing each card with details using the class method.
    :param lst: The board with card arrays (NOT OBJECTS).
    :param length: The length of each card object
    :return:
    """
    print("Checking board...\n")
    x = 0
    for i in lst:
        if ( len(i) != length):
            print(i)
            x = x +1
        print(i.name," card loaded.")
    print("\n\nChecking complete.",x,'card(s) had issue(s).',"\n")
checker(board,12)

def cardChecker(lst,length):
    """
    prints all the names of items in the board loaded.
    :param lst:  The list with board, filled with objects.
    :return: nothing.
    """
    print("Cards: ")
    for i in lst:
        i.cardPrinter()
    print("\nComplete. Loaded ",len(lst),'cards.')
#cardChecker(board,12)

def buyHouse(plyr,cards):
    """
    Buys a house/hotel
    :param plyr: Player object
    :param cards: Array with card objects.
    :param card: card object
    :return:
    """
    ownedSets = []
    ownedProps = []
    ownedPropsName = []
    for i in plyr.properties:
        PropGrp = i
        allOwned = True
        for x in PropGrp.split('|'):
            if x == '0':
                allOwned = False
        if(allOwned == True and plyr.properties.index(i) > 2):
            ownedSets.append(plyr.properties.index(i)+1)
    if(len(ownedSets) != 0):
        print("You can apply houses to the following properties: ")
        evenHouses = []
        for i in cards:
            if(i.group in ownedSets):
                temp = houseEvenChk(i.group,cards)
                for x in temp:
                    evenHouses.append(x)
                    ownedPropsName.append(x.name)
                    print(x.name)
                break
        buyHotelC = raw_input("Which property would you like to buy a house for?\n")
        if buyHotelC in ownedPropsName:
            selectProp = 0
            for i in evenHouses:
                if i.name == buyHotelC:
                    selectProp = i
            houseCost = selectProp.houseCost
            if(selectProp.HouseNumber < 5):
                plyr.addSubMoney((houseCost * -1))
                selectProp.HouseNumber += 1
                print("Purchase successful!")
            else:
                print("Full with a hotel already.")

        else:
            print("Incorrect name entered.")
    else:
        print("No cards can have hotels soz m8.")


def houseEvenChk(group,cards):
    groupCards = []
    groupHouseVals = []
    lessHouseCards = []
    for i in cards:
        if( i.group == group):
            groupCards.append(i)
            groupHouseVals.append(i.HouseNumber)
    x = 0
    for i in groupHouseVals:
        if(groupHouseVals[0]+1 == i):
            groupCards.pop(x)
            x -= 1
        if(groupHouseVals[0]-1 == i ):
            lessHouseCards.append(groupCards[x])
        x += 1
    if(len(lessHouseCards)==0):
        return groupCards
    else:
        return lessHouseCards


def roller():
    """
    Generates 2 numbers, like 2 dice.
    :return:  A double dice roll.
    """
    x = str(random.randrange(1,7))
    y = str(random.randrange(1,7))
    return x+" and " +y
#print("Player rolled",roller() )

def cardNoProps(brd):
    """
    Returns property ownership array.
    :param brd: Board with card objects.
    :return: Form of ['{0-not owned}|{1-owned}' e.g'0|0|0' or '0|1|0']
    """
    propperties = []
    x = ''
    for i in brd:
            if(i.groupID == 0):
               propperties.append(x)
               x = '0'
            else:
               x = x+'|0'
    propperties.append(x)
    propperties.pop(0)
    propperties.pop(0)
    return propperties

def isOwned(players,card):
    """
    checks if the selected card is owned by anyone.
    :param players: The array containing all player objects.
    :param card: The current position/card that would like to be checked.
    :return: True or False.
    """
    cardGrp = card.group
    cardGrpID = card.groupID
    for i in players:
        propLocation = i.properties[cardGrp-1]
        if(propLocation[cardGrpID] == '1'):
            print("Owned by: " + i.name)
            return True
    return False

def isOwnedByPlyr(plyr,card):
    """
    checks if owned by specific player.
    :param plyr: Input the specific player object.
    :param card: The card/position of the current player.
    :return: True or False.
    """
    cardGrp = card.group
    cardGrpID = card.groupID
    propLocation = plyr.properties[cardGrp - 1]
    if (propLocation[cardGrpID] == '1'):
        return True
    else:
        return False

def buyProp(plyr,brdlyt,players):
    """
    Buys a property if its not owned.
    :param plyr: Player object.
    :param brdlyt: Layout of board.
    :param players: Array with player objs.
    :return: Nothing.
    """
    if(isOwned(players,curPos(plyr,brdlyt))):
        print("This is already owned.")
    else:
        card = curPos(plyr,brdlyt)
        crdGrp = plyr.properties[card.group-1].split('|')
        crdGrp[card.groupID] = '1'
        '|'.join(crdGrp)
        plyr.properties[card.group - 1] = crdGrp

def curPos(plyr,brdlyt):
    """
    Finds current position of player.
    :param plyr: Player object
    :param brdlyt: Layout of board.
    :return: The card at which the player is currently at.
    """
    return brdlyt[plyr.position]

def posCalc(roll,plyr,brdlyt):
    """
    Calculates the position the player should be after a roll including the money added when passing the "Go" card.
    :param roll: The roll generated by the roller method.
    :param plyr: The player object.
    :param brdlyt: The layout of the board.
    :return: Nothing. Already altered position directly.
    """
    dieVal = roll.split(' and ')
    totalRoll = 0
    for i in dieVal:
        totalRoll = totalRoll + int(i)
    print(totalRoll)
    plyr.position = plyr.position+totalRoll
    if(plyr.position >= len(brdlyt)):
        plyr.position = plyr.position - len(brdlyt)
        plyr.addSubMoney(addGoMoney)
    print(plyr.position,plyr.position)

def declareBankruptcy (plyr):
    """
    Declares bankruptcy  for a certain player.
    :param plyr: Player object.
    :return:Nothing, alters player directly.
    """
    plyr.bankrupt = True

def checkwin(players):
    """
    Checks if a certain player has won the game.
    :param players: The array with player objects.
    :return: True or False.
    """
    totalBnkrupt = 0
    for i in players():
        if(i.bankrupt == True):
            totalBnkrupt += 1
    if(len(players) - totalBnkrupt == 1):
        for i in players():
            if(i.bankrupt == False):
                print(i.name)
        return True
    else:
        return False

