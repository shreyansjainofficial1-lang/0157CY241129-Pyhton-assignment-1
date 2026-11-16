class Teacher:
    def teach(self):
        print("Professor teaches students.")

class Researcher:
    def research(self):
        print("Professor conducts research.")

class Professor(Teacher, Researcher):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Professor:", self.name)

professor = Professor(input("Enter professor name: "))
professor.introduce()
professor.teach()
professor.research()
