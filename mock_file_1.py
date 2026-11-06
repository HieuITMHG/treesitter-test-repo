class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def get_somethings(self):
        return f"hello {self.name} at {self.age} years old"

    def return_some_structure(self) -> list:
        return [1,2,3,4,5]
        
