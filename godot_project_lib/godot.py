import os
from enum import Enum

class Nodes(Enum):
    Node2D = 0
    Sprite = 1

class Godot:
    def __init__(self, is2 = False, width = 480, height = 360):
        self.project_name = "default"
        self.res_id = 1
        self.project_content = ''''''
        self.is2 = is2
        self.width = width
        self.height = height
    
    def create_project(self, name, driver = "GLES2"):
        if not os.path.isdir(f'./{name}'):
            os.mkdir(f'./{name}') #create dir
        
        self.project_name = name
        
        # 
        if not self.is2:
            self.project_content += '''
                    config_version=4\n
                    [application]\n

                    config/name="'''+name+'''"\n

                    [gui]\n

                    common/drop_mouse_on_gui_input_disabled=true\n

                    [physics]\n

                    common/enable_pause_aware_picking=true\n

                    [rendering]\n

                    quality/driver/driver_name="'''+driver+'''"\n
                    vram_compression/import_etc=true\n
                    vram_compression/import_etc2=false\n
                    environment/default_environment="res://default_env.tres"\n''' #write simple project.godot
        
            with open(f'./{name}/project.godot','w') as f:
                f.write(self.project_content)
                f.close()
        else:
            self.project_content += '''
                \n[application]\n
                
                name="'''+name+'''"\n
                icon="res://icon.png"\n
                
                [display]\n
                width='''+self.width+'''\n
                height='''+self.height+'''\n
            
                [physics_2d]\n

                motion_fix_enabled=true\n
            '''
            with open(f'./{name}/engine.cfg','w') as f:
                    f.write(self.project_content)
                    f.close()
    
        if not self.is2:
            with open(f'./{name}/default_env.tres','w') as f:
                f.write('''\n
                [gd_resource type="Environment" load_steps=2 format=2]\n

                [sub_resource type="ProceduralSky" id=1]\n

                [resource]\n
                background_mode = 2\n
                background_sky = SubResource( 1 )\n''') #write standard default_env
                
                f.close()

    def create_scene(self, name):
        with open(f'./{self.project_name}/{name}.tscn','w') as f:
            if self.is2:
                f.write('''[gd_scene load_steps=2 format=1]\n''')
            else:
                f.write('''[gd_scene load_steps=2 format=2]\n
                ''') #write an empty node2d scene
            
            f.close()
            self.scene_name = name
    
    def set_scene_name(self, name):
        self.scene_name = name
        
    def add_resource(self, path, typ = "Texture"):
        with open(f'./{self.project_name}/{self.scene_name}.tscn','a') as f:
            f.write('''\n[ext_resource path="res://'''+path+'''" type="'''+typ+'''" id='''+str(self.res_id)+''']\n
            ''')
            
            self.res_id += 1
            
            f.close()
            
            return self.res_id - 1
            
    def add_node(self, name, res_id, posX, posY, typ = 0):
        with open(f'./{self.project_name}/{self.scene_name}.tscn','a') as f:
            if typ == Nodes.Sprite:
                if self.is2:
                    f.write('''\n[node name="'''+name+'''" type="Sprite" parent="."]\ntransform/pos = Vector2( '''+str(posX)+''', '''+str(posY)+''' )\ntexture = ExtResource( '''+str(res_id)+''' )\n''')
                else:
                    f.write('''\n[node name="'''+name+'''" type="Sprite" parent="."]\nposition = Vector2( '''+str(posX)+''', '''+str(posY)+''' )\ntexture = ExtResource( '''+str(res_id)+''' )\n''')
                self.res_id += 1
            if typ == Nodes.Node2D:
                f.write('''\n[node name="Node2D" type="Node2D"]\n
                ''')
                
            f.close()

