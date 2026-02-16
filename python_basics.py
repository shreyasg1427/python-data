# Prime numbers from 1–50
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers:")
for i in range(1, 51):
    if is_prime(i):
        print(i, end=" ")

# Simple OOP
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student("Shreyas", [85, 78, 92])
print("\nAverage:", s.average())