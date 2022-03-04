class Rectangle:
    def __init__(self, wid, ht):
        self.width = wid
        self.height = ht

    def __str__(self):
        return ("Rectangle(width={0}, height={1})".format(self.width, self.height))

    def set_width(self, wid):
        self.width = wid
        return self.width
    
    def set_height(self, ht):
        self.height = ht
        return self.height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height **2) **0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return ("Too big for picture.")
        else:
            picture = ""
            for i in range (self.height):
                picture += "*"*self.width + "\n"
            return (picture)

    def get_amount_inside(self, shape):
        outer_width = self.width
        outer_height = self.height
        inner_width = shape.width
        inner_height = shape.height
        w_counter = 0
        h_counter = 0
        while outer_width >= inner_width:
            outer_width -= inner_width
            w_counter += 1

        while outer_height >= inner_height:
            outer_height -= inner_height
            h_counter += 1

        return (w_counter * h_counter)




#For a child class, pass the parent class as a parameter to inherit the methods in parent class
class Square (Rectangle):
    
    def __init__(self, len):
        self.width = len
        self.height = len

    def __str__(self):
        return ("Square(side={0})".format(self.width))

    def set_side(self, side):
        self.width = side
        self.height = side
    


#test1
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

#test 2
# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))
# rect = Rectangle(5, 10)
# print(rect.get_area())
# rect.set_width(3)
# print(rect.get_perimeter())
# print(rect)

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)