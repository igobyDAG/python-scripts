class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width={0.width!s}, height={0.height!s})'.format(self)

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        shape_area = shape.get_area()
        return self.get_area() // shape_area


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(width=side, height=side)

    def __str__(self):
        return 'Square(side={0.side!s})'.format(self)

    def set_side(self, side):
        self.side = side
        return self.side

    def set_height(self, height):
        return self.set_side(height)

    def set_width(self, width):
        return self.set_side(width)


rectangle = Rectangle(10, 5)
print(str(rectangle))
