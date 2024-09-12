class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def __str__(self):
        return f"length = {self.length}, width = {self.width}"

rectangle = Rectangle(4, 5)
print(rectangle)