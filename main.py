from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass

class Child(Person):
    def __init__(self, name, age, sponsor=None):
        super().__init__(name, age)
        self.sponsor = sponsor

    def display_info(self):
        if self.sponsor:
            print(f"Child: {self.name}, Age: {self.age}, Sponsored by: {self.sponsor}")
        else:
            print(f"Child: {self.name}, Age: {self.age}")

class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def display_info(self):
        print(f"Staff: {self.name}, Age: {self.age}, Position: {self.position}")

class Volunteer(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def display_info(self):
        print(f"Volunteer: {self.name}, Age: {self.age}, Role: {self.role}")

class PersonFactory:
    @staticmethod
    def create_person(person_type, name, age, **kwargs):
        if person_type == "child":
            return Child(name, age, kwargs.get("sponsor"))
        elif person_type == "staff":
            return Staff(name, age, kwargs.get("position"))
        elif person_type == "volunteer":
            return Volunteer(name, age, kwargs.get("role"))
        else:
            raise ValueError("Invalid person type")
            
class Orphanage:
    def __init__(self):
        self.children = []
        self.staffs = []

    def admit_child(self, child):
        self.children.append(child)

    def hire_staff(self, staff):
        self.staffs.append(staff)

    def display_orphanage_info(self):
        print("Orphanage Information:")
        print("Children:")
        for child in self.children:
            child.display_info()
        print("Staffs:")
        for staff in self.staffs:
            staff.display_info()

def create_person_menu():
    print("Choose a person to create:")
    print("1. Child")
    print("2. Staff")
    print("3. Volunteer")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter name for the Child: ")
        age = int(input("Enter age for the Child: "))
        sponsor = input("Enter sponsor for the Child (leave blank if none): ")
        return Child(name, age, sponsor)
    elif choice == "2":
        name = input("Enter name for the Staff: ")
        age = int(input("Enter age for the Staff: "))
        position = input("Enter position for the Staff: ")
        return Staff(name, age, position)
    elif choice == "3":
        name = input("Enter name for the Volunteer: ")
        age = int(input("Enter age for the Volunteer: "))
        role = input("Enter role for the Volunteer: ")
        return Volunteer(name, age, role)
    else:
        print("Invalid choice!")
        return None

if __name__ == "__main__":
    orphanage = Orphanage()

    while True:
        person = create_person_menu()
        if person:
            orphanage.admit_person(person)
        
        another = input("Do you want to create another person? (yes/no): ")
        if another.lower() != "yes":
            break

    orphanage.display_orphanage_info()
