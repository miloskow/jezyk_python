import random
class Iterator01:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        x = self.a 
        if x == 0:
            self.a = 1
            return x
        else: 
            self.a = 0
            return x
        
class IteratorDirections:
    def __iter__(self):
        self.directions = ("N", "E", "S", "W")
        return self
    def __next__(self):
        return random.choice(self.directions)
        
class IteratorDays:
    def __iter__(self):
        self.day = 0
        return self
    def __next__(self):
        result = self.day
        self.day = (self.day + 1) % 7 
        return result
        

print("Iterator01:")
new01 = iter(Iterator01())
for _ in range(10):  
    print(next(new01))

print("\nIteratorDirections:")
newDir = iter(IteratorDirections())
for _ in range(10):  
    print(next(newDir))

print("\nIteratorDays:")
newDays = iter(IteratorDays())
for _ in range(10):  
    print(next(newDays))