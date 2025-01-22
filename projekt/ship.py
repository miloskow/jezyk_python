class Ship:
    def __init__(self, x, y, size, direction):
        self.x = x  
        self.y = y
        self.size = size
        self.direction = direction  
        self.hits = [False] * size 

    def check_hit(self, col, row):
        for i in range(self.size):
            ship_x = self.x + (i if self.direction == "H" else 0)
            ship_y = self.y + (i if self.direction == "V" else 0)
            if ship_x == col and ship_y == row:
                self.hits[i] = True
                return True
        return False

    def is_sunk(self):
        return all(self.hits)