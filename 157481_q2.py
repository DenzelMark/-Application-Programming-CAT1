# 157481_q2.py
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"{self.name}'s Grades:")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment, grade)

    def display_students_grades(self):
        print(f"Grades for {self.course_name}:")
        for student in self.students:
            student.display_grades()

if __name__ == "__main__":
    
    prof_smith = Instructor("Prof. Damba" , "Personality")
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")

    prof_smith.add_student(student1)
    prof_smith.add_student(student2)
    
    prof_smith.assign_grade("S001", "Assignment 1", 85)
    prof_smith.assign_grade("S002", "Assignment 1", 90)
    
    prof_smith.display_students_grades()