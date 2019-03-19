class Project:
    def __init__(self, filename):
        self.filename = filename
        self.dependencies = []

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)
