import course_data
def calculate_student_grade(student_name):
    data = course_data.actual_data
    if student_name not in data['roster']:
        print("Student not found.")
        return
    total_score = 0.0
    total_weight = 0.0
    for assignment, details in data['assignments'].items():
        weight = details['weight']
        submissions = details['submissions']
        score = submissions.get(student_name, 0)
        print(f"{assignment}: {score}%")
        total_score += score * (weight / 100)
        total_weight += weight
    print(f"Total score: {total_grade:.1f}%")

if __name__ == '__main__':
    student_name = input("Enter the student's name: ")
    calculate_student_grade(student_name)
