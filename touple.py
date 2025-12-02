# -----------------------------
# Complex Tuple Example
# -----------------------------

# A tuple of student records (each record is also a tuple)
students = (
    ("Kaiser", 23, 3.75),
    ("Ayesha", 21, 3.90),
    ("Rahim", 22, 3.40),
    ("Tania", 24, 3.85)
)

# Function returning multiple values as a tuple
def find_top_student(student_tuple):
    # Sort by CGPA (3rd element of each tuple)
    sorted_students = tuple(sorted(student_tuple, key=lambda x: x[2], reverse=True))
    top_student = sorted_students[0]

    # return name, age, cgpa as a tuple
    return top_student, sorted_students


# Unpacking the returned tuple
(top_name, top_age, top_cgpa), sorted_list = find_top_student(students)

print("Top Student:")
print("Name:", top_name)
print("Age:", top_age)
print("CGPA:", top_cgpa)

print("\nAll Students Sorted by CGPA:")
for s in sorted_list:
    print(s)
