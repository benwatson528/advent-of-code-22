class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def __str__(self):
        if self.parent:
            return f"""
                    Name: {self.name}. Parent: {self.parent.name}.
                    Size: {self.size}. Num children: {len(self.children)}
                    """
        else:
            return f"""
                    Name: {self.name}. Parent: (none, root).
                    Size: {self.size}. Num children: {len(self.children)}
                    """
