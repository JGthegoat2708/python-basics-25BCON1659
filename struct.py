from dataclasses import dataclass

# Define the struct-like class
@dataclass
class Student:
    name: str
    roll: int
    marks: float

# Create an instance of Student
s1 = Student(name="Rahul", roll=101, marks=87.5)

# Print the values
print(f"Name: {s1.name}")
print(f"Roll number: {s1.roll}")
print(f"Marks: {s1.marks:.1f}")