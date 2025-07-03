class Scene:
    def __init__(self,name,desc,actors,items,dirs):
        self.name = name
        self.desc = desc
        self.actors = actors
        self.items = items
        self.dirs = dirs
class Actor:
    def __init__(self,name,desc,con,shown):
        self.name = name
        self.desc = desc
        self.con = con
        self.shown = shown
    def converse(self):
        print(self.name + " says...")
        cdict = self.con #current dictionary
        cans = "INIT" #current answer (INIT by default)
        ended = False
        while not ended:
            print(cdict[cans][0])
            if cdict[cans][1] != {} and cdict[cans][1] != {"item":[],"getagain":False}:
                inv.update({cdict[cans][1]["item"][0]:cdict[cans][1]["item"][1]})
                print("\nYou received: " + cdict[cans][1]["item"][1].name)
                if not cdict[cans][1]["getagain"]:
                    cdict[cans][1]["item"] = []
            if cdict[cans][2] == {}:
                ended = True
            else:
                print()
                count = 1
                quickdict = {}
                for i in cdict[cans][2]:
                    print(str(count) + ") " + i)
                    quickdict.update({count:i})
                    count += 1
                conpath = int(input("> ")) #conversation path
                cans = cdict[cans][2][quickdict[conpath]]
                if cans == "BYE":
                    ended = True
class Item:
    def __init__(self,name,desc,shown):
        self.name = name
        self.desc = desc
        self.shown = shown

croom = "TEST" #current room
wmap = {"TEST":Scene("TEST ROOM","You are in the test room. This room is used to test work-in-progress features.",{"OM":Actor("Old Man","It is an old man.",{"INIT":["Hello. Would you like a cup of tea?",{},{"Yes":"YES","No":"NO"}],"YES":["YOU PASSED THE TEST",{"item":["Tea",Item("Tea","A nice hot cup of tea. You see something scribbled on it: \"for emergencies ONLY\"",True)],"getagain":False},{}],"NO":["YOU FAILED",{},{"Goodbye":"BYE","I want to try again":"INIT"}]},True)},{"RolPap":Item("Rolled-up Newspaper","It is a rolled-up Sunday Times.",True),"Tea":Item("Tea","A lukewarm cup of tea.",False,)},{"N":["disgust","NOT EXISTENT"]})}

print("=== TEXT-ADVENTURE BY SLIGHTLYGOODGAMES ON GITHUB - COMMIT 5 ===\n")

inv = {"NPic":Item("Picture of Home","A picture of your homeland far, far away. It's in pristine condition.",True)}

while True:
    rd = wmap[croom] #room data
    print(rd.desc + "\n\nYou see:")
    for i in rd.actors:
        obj = rd.actors[i]
        if obj.shown:
            print(obj.name)
    for i in rd.items:
        obj = rd.items[i]
        if obj.shown:
            print(obj.name)
    com = input("\n> ").lower() #command
    print()
    if com == "talk":
        print("Who to talk with?")
        quickdict = {}
        count = 1
        for i in rd.actors:
            obj = rd.actors[i]
            if obj.shown:
                print(str(count) + ") " + obj.name)
                quickdict.update({count:i})
        giveint = False
        while not giveint:
            try:
                wtw = int(input("> "))
            except:
                print("Please enter an integer.")
            else:
                giveint = True
        print()
        rd.actors[quickdict[wtw]].converse()
    elif com == "inv":
        print("Your inventory contains:")
        for i in inv:
            print(inv[i].name + " - " + inv[i].desc)
    input("\nPress return to continue...")
    print("\n")
