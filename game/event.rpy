init python:
    class items(object):
        def __init__(self. name, value, weight, NoOwned, ID):
            self.name = name
            self.val = val
            self.weight = weight
            self.NoOwned = NoOwned
            self.ID = ID
        def AddItem(self):
            MaxWeight = 50
            
            if CurrentWeight + self.weight > MaxWeight:
                return
            else:
                self.NoOwned += 1 
        @property
        def CurrentWeight(self):
            CurrentW = 0
            for q in Inventory:
                CurrentW += (q.weight * q.NoOwned)
            return CurrentW
    
    EVENTS = []
    Inventory = []
    t = 0

    while t < 50:
        EVENTS.append(Event(0, 0, 0, "", False))
        Inventory.append(Items("none", 0, 0, 0))
        t += 1

