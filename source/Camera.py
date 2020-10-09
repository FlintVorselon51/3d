import math


class Camera:
    def __init__(self, coordinates, horizontal_viewing_angle, vertical_viewing_angle, horizontal_rotation):
        self.__coordinates = coordinates
        self.__horizontal_viewing_angle = horizontal_viewing_angle
        self.__vertical_viewing_angle = vertical_viewing_angle
        self.__horizontal_rotation = horizontal_rotation
        self.__vertical_rotation = 0

        # X
        self.__x1 = math.sin(math.radians(90 + self.__horizontal_viewing_angle / 2 - self.__horizontal_rotation))
        self.__x2 = math.sin(math.radians(90 - self.__horizontal_viewing_angle / 2 - self.__horizontal_rotation))

        # Y
        self.__y1 = math.sin(math.radians(self.__vertical_viewing_angle / 2 + self.__vertical_rotation))
        self.__y2 = math.sin(math.radians(-self.__vertical_viewing_angle / 2 + self.__vertical_rotation))

        # Z
        self.__z1 = math.cos(math.radians(90 + self.__horizontal_viewing_angle / 2 - self.__horizontal_rotation))
        self.__z2 = math.cos(math.radians(90 - self.__horizontal_viewing_angle / 2 - self.__horizontal_rotation))

        self.__delta_x = self.__x2 - self.__x1
        self.__delta_y = self.__y2 - self.__y1
        self.__delta_z = self.__z2 - self.__z1

    def get_coordinates(self):
        return self.__coordinates

    def get_delta(self):
        return self.__delta_x, self.__delta_y, self.__delta_z

    def get_start_values(self):
        return self.__x1, self.__y1, self.__z1

    def __str__(self):
        return str(f'1: ({round(self.__x1, 3)}, {round(self.__y1, 3)}, {round(self.__z1, 3)})\n'
                   f'2: ({round(self.__x1, 3)}, {round(self.__y2, 3)}, {round(self.__z1, 3)})\n'
                   f'3: ({round(self.__x2, 3)}, {round(self.__y1, 3)}, {round(self.__z2, 3)})\n'
                   f'4: ({round(self.__x2, 3)}, {round(self.__y2, 3)}, {round(self.__z2, 3)})\n')
