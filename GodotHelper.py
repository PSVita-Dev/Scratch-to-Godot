from godot_project_lib import godot

class GodotWriter:
    def __init__(self, project_name):
        self.handler = godot.Godot(True) #True for godot 2.1.x, False for godot 3.x
        handler.create_project(project_name)
