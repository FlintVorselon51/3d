class Circle:
    def __init__(self, coordinates, radius, color):
        self.__coordinates = coordinates
        self.__radius = radius
        self.__color = color

    def get_distance(self, coordinates):
        return pow((coordinates[0] - self.__coordinates[0]) ** 2 +
                   (coordinates[1] - self.__coordinates[1]) ** 2 +
                   (coordinates[2] - self.__coordinates[2]) ** 2, 0.5) - self.__radius

    def get_coordinates(self):
        return self.__coordinates

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color
