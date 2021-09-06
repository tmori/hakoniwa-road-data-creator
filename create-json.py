from hakoniwa_road_type import RoadEntry
from hakoniwa_road_type import RoadRoot

filepath = 'road_map.json'
        
root = RoadRoot()

entry = RoadEntry('road2', 0.0, None)
root.add(entry)

entry = RoadEntry('road1', 0.0, '+z')
root.add(entry)

entry = RoadEntry('road2', 180.0, '+z')
root.add(entry)

entry = RoadEntry('road1', 90.0, '+x')
root.add(entry)

entry = RoadEntry('road2', 270.0, '+x')
root.add(entry)

root.dump(filepath)
