import dataclasses


@dataclasses.dataclass(frozen=True)
class Valve:
    id: str
    flow_rate: int
    children: frozenset
