from collections import Counter

from main.day15.Sensor import Sensor


def solve(sensors_beacons, y_to_scan) -> int:
    sensors = map(create_sensor, sensors_beacons)
    occupied = set()
    for sensor in sensors:
        circumference_range = find_circumference_range(sensor, y_to_scan)
        if circumference_range:
            occupied.update(circumference_range)

    beacons_on_line = set(
        [sb[1][0] for sb in sensors_beacons if sb[1][1] == y_to_scan])
    return len(occupied) - len(beacons_on_line)


def solve_p2(sensors_beacons, rows_to_scan) -> int:
    sensors = map(create_sensor, sensors_beacons)
    coords = Counter()
    for sensor in sensors:
        manhattan_distance = calc_manhattan_distance(sensor.sensor_x,
                                                     sensor.beacon_x,
                                                     sensor.sensor_y,
                                                     sensor.beacon_y)
        # draw left to top
        x = sensor.sensor_x - manhattan_distance
        y = sensor.sensor_y
        while x <= sensor.sensor_x:
            coords[(x, y)] += 1
            x += 1
            y -= 1

        # draw top to right
        x = sensor.sensor_x
        y = sensor.sensor_y - manhattan_distance
        while y <= sensor.sensor_y:
            coords[(x, y)] += 1
            x += 1
            y += 1

        # draw right to bottom
        x = sensor.sensor_x + manhattan_distance
        y = sensor.sensor_y
        while x >= sensor.sensor_x:
            coords[(x, y)] += 1
            x -= 1
            y += 1

        # draw bottom to left
        x = sensor.sensor_x
        y = sensor.sensor_y + manhattan_distance
        while y >= sensor.sensor_y:
            coords[(x, y)] += 1
            x -= 1
            y -= 1
    intersection_points = {coord: count for coord, count in coords.items() if
                           count >= 2 and 0 <= coord[0] <= rows_to_scan and 0 <= coord[1] <= rows_to_scan}
    central = list(find_central_points(intersection_points))[0]
    return (central[0] * 4000000) + central[1]


def find_central_points(intersection_points):
    centrals = set()
    for intersection_point in intersection_points:
        if is_surrounded((intersection_point[0] - 1, intersection_point[1]), intersection_points):
            centrals.add((intersection_point[0] - 1, intersection_point[1]))
        elif is_surrounded((intersection_point[0] + 1, intersection_point[1]), intersection_points):
            centrals.add((intersection_point[0] + 1, intersection_point[1]))
        elif is_surrounded((intersection_point[0], intersection_point[1] - 1), intersection_points):
            centrals.add((intersection_point[0], intersection_point[1] - 1))
        elif is_surrounded((intersection_point[0], intersection_point[1] + 1), intersection_points):
            centrals.add((intersection_point[0], intersection_point[1] + 1))
    return centrals


def is_surrounded(coord, intersection_points):
    return (coord[0] + 1, coord[1]) in intersection_points and (coord[0] - 1, coord[1]) in intersection_points and (
        coord[0], coord[1] - 1) in intersection_points and (coord[0], coord[1] + 1) in intersection_points


def find_circumference_range(sensor, y_to_scan):
    manhattan_distance = calc_manhattan_distance(sensor.sensor_x,
                                                 sensor.beacon_x,
                                                 sensor.sensor_y,
                                                 sensor.beacon_y)
    lower_x = -((manhattan_distance - abs(
        sensor.sensor_y - y_to_scan)) - sensor.sensor_x)
    retry = calc_manhattan_distance(sensor.sensor_x, lower_x,
                                    sensor.sensor_y, y_to_scan)
    if retry != manhattan_distance:
        lower_x = None
    upper_x = (manhattan_distance - abs(
        sensor.sensor_y - y_to_scan)) + sensor.sensor_x
    retry = calc_manhattan_distance(sensor.sensor_x, upper_x, sensor.sensor_y,
                                    y_to_scan)
    if retry != manhattan_distance:
        upper_x = None
    if lower_x is None or upper_x is None:
        return None
    else:
        return set(range(lower_x, upper_x + 1))


def calc_manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def create_sensor(sensor_beacon):
    sensor, beacon = sensor_beacon[0], sensor_beacon[1]
    return Sensor(sensor[0], sensor[1], beacon[0], beacon[1])
