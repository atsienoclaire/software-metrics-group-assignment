Refracted code
a) Improved Student.calulate_perfomance() (Lower cyclomatic complexity)

class Student(Person):

    GRADE_POINTS = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}

    def calculate_gpa(self):
        if not self.grades:
            return 0
        total_points = sum(self.GRADE_POINTS[g] for g in self.grades.values())
        return round(total_points / len(self.grades), 2)

    def calculate_attendance(self):
        if not self.attendance:
            return 0
        course_rates = []
        for records in self.attendance.values():
            attended = sum(1 for r in records if r)
            course_rates.append((attended / len(records)) * 100)
        return sum(course_rates) / len(course_rates)

    def calculate_performance(self):
        gpa = self.calculate_gpa()
        attendance = self.calculate_attendance()

        self.print_performance_feedback(gpa, attendance)
        return gpa

    def print_performance_feedback(self, gpa, attendance):
        print(f"GPA: {gpa}, Attendance: {attendance:.1f}%")
        if gpa >= 3.5 and attendance >= 90:
            print("Excellent performance!")
        elif gpa < 2.0 or attendance < 60:
            print("Warning: Poor performance")

b) Removed coupling between Registra ->Student/Course
class Course:
    def report(self):
        self.display_details()

class Lecturer(Person):
    def report(self):
        self.print_summary()

class Student(Person):
        def report(self):
            self.calculate_performance()

class Registrar:
    def full_report(self):
        print("=== Full University Report ===")
        for c in self.courses:
            c.report()
        for l in self.lecturers:
            l.report()
        for s in self.students:
            s.report()

c) Improved Cohesion in main() by extracting Setup Logic
def create_sample_data(reg):
    c1 = Course("CS101", "Intro to Programming", 3)
    c2 = Course("CS201", "Data Structures", 4)

    l1 = Lecturer("L001", "Dr. Smith", "smith@uni.com", "CS")
    s1 = Student("S001", "Alice", "alice@uni.com")
    s2 = Student("S002", "Bob", "bob@uni.com")

    reg.add_course(c1)
    reg.add_course(c2)
    reg.add_lecturer(l1)
    reg.add_student(s1)
    reg.add_student(s2)

    l1.assign_course(c1)
    c1.enroll_student(s1)
    c1.enroll_student(s2)

    l1.submit_grades([s1, s2], "CS101", "A")

    s1.attendance["CS101"] = [True, True, False, True]
    s2.attendance["CS101"] = [True, False, True, False]


def main():
    reg = Registrar()
    create_sample_data(reg)
    reg.full_report()

