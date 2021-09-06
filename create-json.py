from hakoniwa_road_type import RoadEntry
from hakoniwa_road_type import RoadRoot

filepath = 'road_map.json'
        
root = RoadRoot()

root.add(RoadEntry('road2', 0.0,    None))
root.add(RoadEntry('road1', 0.0,    '+z'))
root.add(RoadEntry('road2', 180.0,  '+z'))
root.add(RoadEntry('road1', 90.0,   '+x'))
root.add(RoadEntry('road2', 270.0,  '+x'))

root.dump(filepath)
