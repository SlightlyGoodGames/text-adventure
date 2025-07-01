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
class Item:
    def __init__(self,name,desc,shown):
        self.name = name
        self.desc = desc
        self.shown = shown

croom = "TEST" #current room
wmap = {"TEST":Scene("TEST ROOM","You are in the test room. This room is used to test work-in-progress features.",{"OM":Actor("Old Man","It is an old man.",{"INIT":["Hello. Would you like a cup of tea?","",{"Yes":["YOU PASSED THE TEST","Tea",{}],"No":["YOU FAILED","",{}]}]},True)},{"RolPap":Item("Rolled-up Newspaper","It is a rolled-up Sunday Times.",True),"Tea":Item("Tea","A lukewarm cup of tea.",False,)},{"N":["disgust","NOT EXISTENT"]})}
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
