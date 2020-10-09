import numpy as np


def raymarch(camera, outside_point, distance, objects):
    start_point = camera.get_coordinates()
    end_point = outside_point
    for _ in range(50):
        transform_point = transform_vector(start_point, end_point, distance)
        distance_with_color = get_distance(objects, transform_point)
        distance = distance_with_color[0]
        if distance < 0.001:
            return distance_with_color[1]
        elif distance > 100:
            return np.array((0, 0, 0))
        start_point = end_point
        end_point = transform_vector(end_point, end_point + outside_point, distance)
    return np.array((0, 0, 0))


def send_rays(camera, screen, objects):
    start_x = camera.get_start_values()[0] + camera.get_coordinates()[0]
    now_y = camera.get_start_values()[1] + camera.get_coordinates()[1]
    start_z = camera.get_start_values()[2] + camera.get_coordinates()[2]
    step_x = camera.get_delta()[0] / screen.get_width()
    step_y = camera.get_delta()[1] / screen.get_height()
    step_z = camera.get_delta()[2] / screen.get_width()
    distance = get_distance(objects, camera.get_coordinates())[0]
    for i in range(screen.get_height()):
        now_x = start_x
        now_z = start_z
        for j in range(screen.get_width()):
            outside_point = np.array((now_x, now_y, now_z))
            color = raymarch(camera, outside_point, distance, objects)
            screen.set_at((j, i), color)
            now_x += step_x
            now_z += step_z
        now_y += step_y


def get_distance(objects, point):
    distances = {}
    for obj in objects:
        distances[obj.get_distance(point)] = obj.get_color()
    distance = min(distances)
    return distance, distances[distance]


def get_module_of_vector(point_1, point_2):
    return pow((point_1[0] - point_2[0]) ** 2 +
               (point_1[1] - point_2[1]) ** 2 +
               (point_1[2] - point_2[2]) ** 2, 0.5)


def transform_vector(main_point, minor_point, required_distance):
    if get_module_of_vector(main_point, minor_point) == 0:
        return 0
    coff = required_distance / get_module_of_vector(main_point, minor_point)
    return main_point[0] - (main_point[0] - minor_point[0]) * coff, \
           main_point[1] - (main_point[1] - minor_point[1]) * coff, \
           main_point[2] - (main_point[2] - minor_point[2]) * coff
