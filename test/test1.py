class Person:
    __age = 10


person = Person()
print(person._Person__age, 1)
print(person.age, 2)
print(Person.age, 3)
print(person.__age, 4)
