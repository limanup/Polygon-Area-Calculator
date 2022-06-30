class Rectangle:

    # initialize with width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # set width
    def set_width(self, width):
        self.width = width
    
    # set height
    def set_height(self, height):
        self.height = height
    
    # returns the area of the rectangle
    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    # returns perimeter of the rectangle
    def get_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
    
    # returns the diagonal of the rectangle
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return self.diagonal
    
    # returns a string that represents the shape using '*'
    def get_picture(self):
        strpicture = str()
        strpicture = strpicture + '*' * self.width + '\n'
        strpicture = strpicture * self.height
        
        # if width or height > 50, replace strpicture with message
        if self.width > 50 or self.height > 50: 
            strpicture = 'Too big for picture.'

        return strpicture

    # takes another shape (square or rectangle) as an argument
    # returns the # of times the passed in shape could fit 
    # inside the shape (with no rotations)
    def get_amount_inside(self, shape):
        # # no need to check.. will just let it return 0 
        # ## check passed in shape is bigger than rectangle
        # if shape.width > self.width or shape.height > self.height:
        #     return (shape.__class__.__name__, 'is too big')
        # else:
        w_x_times = self.width // shape.width
        h_x_times = self.height // shape.height
        amount_inside = w_x_times * h_x_times
        return amount_inside

    # if an object of class Rectangle is represented as a string (print())
    def __str__(self):
        strclass_name = self.__class__.__name__
        strwidth = 'width=' + str(self.width)
        strheight = 'height=' + str(self.height)
        print_result = strclass_name + '(' + strwidth + ', ' + strheight + ')'
        return print_result


class Square(Rectangle):

    # initialize side for square
    def __init__(self, side):
        # can use super/child function to call Rectangle's init method
        super().__init__(side, side)

    # set side of square
    def set_side(self, side):
        self.width = side
        self.height = side
    
    # set_width and set_height for square should set both w and h
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height

    # if an object of class Square is represented as a string (print())
    def __str__(self):
        strclass_name = self.__class__.__name__
        strside = 'side=' + str(self.width)
        print_result = strclass_name + '(' + strside + ')'
        return print_result


# # test cases
# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))

# sq1 = Square(10)
# print(sq1.get_perimeter())
# print(sq1.get_picture())

# rect1 = Rectangle(2,2)
# rect1.set_width(3)
# rect1.set_height(4)
# print(rect1.get_diagonal())
# print(rect1.get_picture())

# print(sq1.get_amount_inside(rect1))

# sq2 = Square(5)
# print(sq2.get_picture())
# sq2.set_height(3)
# print(sq2.get_picture())
