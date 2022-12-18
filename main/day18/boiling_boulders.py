def solve_all_surface_area(cubes) -> int:
    return len(get_x_z_faces(cubes)) + len(get_x_y_faces(cubes)) + len(get_y_z_faces(cubes))


# This is quite inefficient. It would be better to flood fill the outside and then count the flooded boundaries.
def solve_outer_surface_area(cubes) -> int:
    bounds = (min(x for (x, y, z) in cubes), max(x for (x, y, z) in cubes),
              min(y for (x, y, z) in cubes), max(y for (x, y, z) in cubes),
              min(z for (x, y, z) in cubes), max(z for (x, y, z) in cubes))
    surface_area = 0
    for cube in cubes:
        for neighbour in get_neighbours(cube):
            if neighbour not in cubes and dfs(neighbour, cubes, bounds):
                surface_area += 1
    return surface_area


def dfs(cube, cubes, bounds):
    visited = set()
    to_visit = [cube]
    while to_visit:
        current = to_visit.pop()
        if current not in cubes and current not in visited:
            visited.add(current)
            if has_escaped(current, bounds):
                return True
            to_visit.extend(get_neighbours(current))
    return False


def get_neighbours(cube):
    return [(cube[0] - 1, cube[1], cube[2]), (cube[0] + 1, cube[1], cube[2]),
            (cube[0], cube[1] - 1, cube[2]), (cube[0], cube[1] + 1, cube[2]),
            (cube[0], cube[1], cube[2] - 1), (cube[0], cube[1], cube[2] + 1)]


def has_escaped(cube, bounds):
    return cube[0] < bounds[0] or cube[0] > bounds[1] or \
        cube[1] < bounds[2] or cube[1] > bounds[3] or \
        cube[2] < bounds[4] or cube[2] > bounds[5]


def get_x_z_faces(cubes):
    x_z_faces = set()
    for cube in cubes:
        update_faces((cube[0], cube[2], cube[1]), x_z_faces)
        update_faces((cube[0], cube[2], cube[1] + 1), x_z_faces)
    return x_z_faces


def get_x_y_faces(cubes):
    x_y_faces = set()
    for cube in cubes:
        update_faces((cube[0], cube[1], cube[2]), x_y_faces)
        update_faces((cube[0], cube[1], cube[2] + 1), x_y_faces)
    return x_y_faces


def get_y_z_faces(cubes):
    y_z_faces = set()
    for cube in cubes:
        update_faces((cube[1], cube[2], cube[0]), y_z_faces)
        update_faces((cube[1], cube[2], cube[0] + 1), y_z_faces)
    return y_z_faces


def update_faces(face, faces):
    faces.remove(face) if face in faces else faces.add(face)
