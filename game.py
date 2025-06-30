class Scene:
    def __init__(self,name,desc,actors,items,dirs):
        self.name = name
        self.desc = desc
        self.actors = actors
        self.items = items
        self.dirs = dirs
class Actor:
    def __init__(self,name,desc,con):
        self.name = name
        self.desc = desc
        self.con = con
class Item:
    def __init__(self,name,desc,cpu):
        self.name = name
        self.desc = desc
        self.cpu = cpu #can pick up
wmap = {"TEST":Scene("TEST ROOM","You are in the test room. If you somehow got here, your game is broken!",{"OM":Actor("Old Man","It is an old man.",{"INIT":["Hello. Would you like a cup of tea?","",{"Yes":["YOU PASSED THE TEST","Tea",{}],"No":["YOU FAILED","",{}]}]})},{"RolPap":Item("Rolled-up Newspaper","It is a rolled-up Sunday Times.",True),"Tea":Item("Tea","A lukewarm cup of tea.",False)},{"N":["disgust","NOT EXISTENT"]})}
