def solve(cubes) -> int:
    x_z_faces = get_x_z_faces(cubes)
    x_y_faces = get_x_y_faces(cubes)
    y_z_faces = get_y_z_faces(cubes)
    return len(x_z_faces) + len(x_y_faces) + len(y_z_faces)


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
