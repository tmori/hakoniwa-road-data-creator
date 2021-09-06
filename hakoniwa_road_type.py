import json

class RoadEntry:
    prefab_name = 'null'
    rotation = 0.0
    connect_direction = None
    name = None
    repeat_num = None
    scale = None


    def __init__(self, prefab, rot, dir):
        self.prefab_name = prefab
        self.rotation = rot
        self.connect_direction = dir
        
    def encode(self):
        json_data = dict()
        json_data['prefab_name'] = self.prefab_name
        json_data['rotation'] = self.rotation
        if self.connect_direction != None:
            json_data['connect_direction'] = self.connect_direction
        if self.name != None:
            json_data['name'] = self.name
        if self.repeat_num != None:
            json_data['repeat_num'] = self.repeat_num
        if self.scale != None:
            json_data['scale'] = self.scale
        
        return json_data

class RoadRoot:
    root = dict()
    def __init__(self):
        self.root['entries'] = list()
    
    def add(self, entry):
        self.root['entries'].append(entry.encode())
    
    def dump(self, filepath):
        with open(filepath, mode='wt', encoding='utf-8') as file:
            json.dump(self.root, file, ensure_ascii=False, indent=2)
