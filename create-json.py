from hakoniwa_road_type import RoadEntry
from hakoniwa_road_type import RoadRoot

filepath = 'road_map.json'
        
root = RoadRoot()

entry = RoadEntry()
entry.prefab_name = 'road2'
entry.rotation = 0.0
root.add(entry)

entry = RoadEntry()
entry.prefab_name = 'road1'
entry.rotation = 0.0
entry.connect_direction = "+z"
root.add(entry)

entry = RoadEntry()
entry.prefab_name = 'road2'
entry.rotation = 180.0
entry.connect_direction = "+z"
root.add(entry)

entry = RoadEntry()
entry.prefab_name = 'road1'
entry.rotation = 90.0
entry.connect_direction = "+x"
root.add(entry)

entry = RoadEntry()
entry.prefab_name = 'road2'
entry.rotation = 270.0
entry.connect_direction = "+x"
root.add(entry)

root.dump(filepath)
