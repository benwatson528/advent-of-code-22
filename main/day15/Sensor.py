import dataclasses


@dataclasses.dataclass(frozen=True)
class Sensor:
    sensor_x: int
    sensor_y: int
    beacon_x: int
    beacon_y: int
