class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return (f"Rectangle(width={self.width}, height={self.height})")

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    print(self.width * self.height)
    return self.width * self.height

  def get_perimeter(self):
    print(2 * self.width + 2 * self.height)
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    print((self.width**2 + self.height**2)**.5)
    return (self.width**2 + self.height**2)**.5

  def get_picture(self):
    if self.width <= 50 and self.height <= 50:
      shape = ""
      for i in range(self.height):
        for i in range(self.width):
          shape = shape + "*"
        shape = shape + "\n"
      print(shape)
      return shape

    else:
      print("Too big for picture.")

  def get_amount_inside (self, other_shape):
    first_shape = self.get_area()
    second_shape = other_shape.get_area()

    number_of_fit = first_shape//second_shape
    print(number_of_fit)
    return number_of_fit


class Square(Rectangle):
  def __init__ (self, length):
    self.width = length
    self.height = length

  def __str__(self):
    return (f"Square(side={self.width})")

  def set_side (self, new_side):
    self.width = new_side
    self.height = new_side
