from day07.Dir import Dir


def solve_smallest(commands) -> int:
    root_fs = traverse_commands(commands)
    sum_nested_files(root_fs)
    return sum_small_nodes(root_fs)


def solve_biggest(commands) -> int:
    root_fs = traverse_commands(commands)
    sum_nested_files(root_fs)
    space_to_clear = 30000000 - (70000000 - root_fs.size)
    return sum_big_nodes(root_fs, space_to_clear)


def sum_nested_files(node):
    for child in node.children:
        node.size += sum_nested_files(child)
    return node.size


def sum_small_nodes(node):
    total = 0
    if node.size < 100000:
        total += node.size
    for child in node.children:
        total += sum_small_nodes(child)
    return total


def sum_big_nodes(node, space_to_clear):
    current_biggest = 70000000
    if space_to_clear <= node.size < current_biggest:
        current_biggest = node.size
    for child in node.children:
        current_biggest = min(sum_big_nodes(child, space_to_clear),
                              current_biggest)
    return current_biggest


def traverse_commands(commands):
    root = Dir("/", None)
    current_dir = root
    for command in commands:
        if command.startswith("cd"):
            current_dir = move(command, current_dir, root)
        if command.startswith("ls"):
            current_dir.size = get_dir_contents_size(command)
    return root


def move(command, current_dir, root):
    movement = command.split(" ")[1]
    if movement == "..":
        return current_dir.parent
    elif movement == "/":
        return root
    else:
        child_dir = Dir(movement, current_dir)
        current_dir.children.append(child_dir)
        return child_dir


def get_dir_contents_size(command):
    sizes = 0
    for item in command.split("\n")[1:]:
        if not item.startswith("dir"):
            sizes += int(item.split(" ")[0])
    return sizes
