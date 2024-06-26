import unittest

class Orphanage:
    def __init__(self):
        self.people = []

    def admit_person(self, person):
        self.people.append(person)

    @staticmethod
    def decoratorMethod(func):
        def wrapper(*args, **kwargs):
            print("|||| Welcome to the Orphanage management system: ||||")
            func(*args, **kwargs)
            print("~ Operation Executed! ~")

        return wrapper

    @decoratorMethod
    def display_orphanage_info(self):
        print("Orphanage Information:")
        for person in self.people:
            person.display_info()


class Child:
    def __init__(self, name, age, sponsor=None):
        self.name = name
        self.age = age
        self.sponsor = sponsor

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Sponsor: {self.sponsor}")


class Staff:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")


class Volunteer:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Role: {self.role}")


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


def write_to_file(orphanage, filename):
    with open(filename, "w") as file:
        for person in orphanage.people:
            if isinstance(person, Child):
                file.write(f"Child,{person.name},{person.age},{person.sponsor}\n")
            elif isinstance(person, Staff):
                file.write(f"Staff,{person.name},{person.age},{person.position}\n")
            elif isinstance(person, Volunteer):
                file.write(f"Volunteer,{person.name},{person.age},{person.role}\n")
            else:
                print(f"Unknown person type: {type(person)}")


def read_from_file(filename):
    orphanage = Orphanage()
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == "Child":
                orphanage.admit_person(
                    Child(data[1], int(data[2]), data[3] if len(data) > 3 else None)
                )
            elif data[0] == "Staff":
                orphanage.admit_person(Staff(data[1], int(data[2]), data[3]))
            elif data[0] == "Volunteer":
                orphanage.admit_person(Volunteer(data[1], int(data[2]), data[3]))
            else:
                print(f"Unknown person type: {data[0]}")
    return orphanage


class TestOrphanage(unittest.TestCase):
    def test_child_creation(self):
        child = Child("John", 10, "ABC Foundation")
        self.assertEqual(child.name, "John")
        self.assertEqual(child.age, 10)
        self.assertEqual(child.sponsor, "ABC Foundation")

    def test_staff_creation(self):
        staff = Staff("Jane", 30, "Manager")
        self.assertEqual(staff.name, "Jane")
        self.assertEqual(staff.age, 30)
        self.assertEqual(staff.position, "Manager")

    def test_volunteer_creation(self):
        volunteer = Volunteer("Alice", 25, "Tutor")
        self.assertEqual(volunteer.name, "Alice")
        self.assertEqual(volunteer.age, 25)
        self.assertEqual(volunteer.role, "Tutor")


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

    filename = input("Please enter the filename here: ")
    write_to_file(orphanage, filename)
    print("Data written to", filename, ".txt file successfully")

    orphanage_from_file = read_from_file(filename)
    orphanage_from_file.display_orphanage_info()

    unittest.main()
