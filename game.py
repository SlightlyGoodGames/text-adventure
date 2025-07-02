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
            if cdict[cans][1] != "":
                print("\nYou received: " + cdict[cans][1] + " (but not really since the inventory doesn't exist yet)")#append cdict[cans][1] item to their inventory
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
        print("\n")
class Item:
    def __init__(self,name,desc,shown):
        self.name = name
        self.desc = desc
        self.shown = shown

croom = "TEST" #current room
wmap = {"TEST":Scene("TEST ROOM","You are in the test room. This room is used to test work-in-progress features.",{"OM":Actor("Old Man","It is an old man.",{"INIT":["Hello. Would you like a cup of tea?","",{"Yes":"YES","No":"NO"}],"YES":["YOU PASSED THE TEST","Tea",{}],"NO":["YOU FAILED","",{"Goodbye":"BYE","I want to try again":"INIT"}]},True)},{"RolPap":Item("Rolled-up Newspaper","It is a rolled-up Sunday Times.",True),"Tea":Item("Tea","A lukewarm cup of tea.",False,)},{"N":["disgust","NOT EXISTENT"]})}
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
        wtw = int(input("> ")) #who to talk with
        print()
        rd.actors[quickdict[wtw]].converse()
