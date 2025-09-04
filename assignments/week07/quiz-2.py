class Student:
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    # Method to add a grade
    def add_grade(self, grade):
        self.grades.append(grade)
        

    # Method to get the average grade
    def get_average_grade(self):
        average_grade = 0
        sum = 0
        for grade in self.grades:
            score = grade ['grade']
            sum += score
        average_grade = sum/len(self.grades)
        return average_grade
    # Method to get the grade report
    def get_grade_report(self):
        report= " "
        for grade in self.grades:
            subject = grade["subject"]
            score = grade["grade"]
            report += f"subject: {subject} Grade: {score}\n"
        return report


student = Student("John", 20, "S123")
student.add_grade(
    {
        "subject": "Math", 
        "grade": 85
    }
)
student.add_grade(
    {
        "subject": "Science",
        "grade": 92
    }
)
print(student.get_average_grade())  # Should print 88.5
print(student.get_grade_report())   # Should show all grades