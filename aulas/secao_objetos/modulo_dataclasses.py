from dataclasses import dataclass, asdict


@dataclass
class Point:
    x: int
    y: int

p1 = Point(10, 20)


print(p1)
print(p1.x)
print(asdict(p1))