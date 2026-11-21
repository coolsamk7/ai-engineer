from dataclasses import dataclass

from pydantic import BaseModel, ValidationError


def double(n: int) -> int:
    return n * 2


print(double("ab"))


@dataclass
class User:
    name: str
    age: int


u = User("Sam", "30")

print(u.age, type(u.age))


class UserModel(BaseModel):
    name: str
    age: int


m = UserModel(name="Sam", age="30")
print(m.age, type(m.age))

try:
    UserModel(name="Sam", age="thirty")
except ValidationError as e:
    print("invalid:", e.error_count())
