from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# Load grades from JSON file
my_grades = Grades.from_json("grades.json")

# Instantiate weights
weights = GradeWeights()

# Print grades
print(my_grades)

# Calculate current grade
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100:.2f}% is {letter_grade}')

# Calculate optimistic grade
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100:.2f}%, which is a {optimistic_letter_grade}')
