from dataclasses import dataclass

# creating a class called "Rectangle" that has 2 attributes: the width and height which are integer values
@dataclass
class Rectangle:
    width: int = 0
    height: int = 0

    # in a while loop, the class's height attribute is assigned from the user input. If the input is not int or if it is less then or equal ot 0, an error message prints
    # otherwise, it will return the height
    def get_height(self):
        '''
        :return: height of the rectangle
        '''
        while True:
            try:
                self.height = int(input("Height: "))
                if self.height <= 0:
                    print("Height must be less then or equal to zero")
                else:
                    return self.height
            except:
                print("Must be a positive integer")

    # Same thing with the width attribute
    def get_width(self):
        '''
        :return: the width of the rectangle
        '''
        while True:
            try:
                self.width = int(input("Width: "))
                if self.width <= 0:
                    print("Width must be greater then zero.")
                else:
                    return self.width
            except:
                print("Must be a positive integer")

    # NOTE: Area is not an attribute. it is calculated by multiplying height and width and returned.
    def get_area(self, width, height):
        '''
        :param width: width of the rectangle
        :param height: height of the rectangle
        :return: the area of the rectangle
        '''
        area = width * height
        return area

    # NOTE: perimeter is also not an attribute. the width and height and multiplied together and that result is multiplied by 2 and returned
    def get_perimeter(self, width, height):
        '''
        :param width: width of the rectangle
        :param height: height of the triangle
        :return: the perimeter of the triangle
        '''
        perimeter = 2 * (width + height)
        return perimeter

    # format manages the sides of the rectangle. a blank line is multiplied by width - 2. that is * 2 and subtracted by 1 so it lines up neatly.
    # "* " * width is for the tops and bottom of the rectangle
    # in a loop, the sides of the triangle is printed using the format mentioned. it starts at 2 as we already have the sides from the tops nad bottom.
    def print_rectangle(self):
        '''
        :return: nothing
        '''
        format = " " * (((self.width - 2) * 2) - 1)
        print("* " * self.width)
        for x in range(2, self.height):
            print('*', format, '*')
        print("* " * self.width)


# Instanciating the class
rectangle = Rectangle()


# go variable controls the while loop, as long as the player says "y' when asked if they want to continue, the loop will repeat. if the user does not enter a string value, it will
# print an error message.
def main():
    '''
    :return: nothing
    '''
    go = "y"
    while go == "y":
        height = rectangle.get_height()
        width = rectangle.get_width()
        area = rectangle.get_area(width, height)
        perimeter = rectangle.get_perimeter(width, height)
        print(f"Height: {height}")
        print(f"Width: {width}")
        print(f"Perimeter: {perimeter}")
        print(f"Area: {area}")
        rectangle.print_rectangle()
        try:
            go = input("Continue? (y/n): ")
        except:
            print("Invalid input")


# executes the main function, and shows "Bye" for when the player exits the loop.
if __name__ == "__main__":
    main()
    print("Bye!")
