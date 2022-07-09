from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Person:
    name: str
    age: int


canon = Person("Canon", 22)
ada = Person("Ada", 20)

clone = Person("Canon", 22)

print(hash(canon))
print(hash(clone))

people = [canon, ada]

people.sort()

print(people)
