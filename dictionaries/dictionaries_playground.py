# Key-value pairs
# Keys are unique
# Keys need to be immutable (Strings, integers, Floats)
# Unordered
#students = {"Zohreh" : 123, "Dani": 5.4}
#print(students_numbers)
#students["Donna"] = 189
#del students["Dani"]
#students_numbers["Dani"] = 999
#print(students_numbers)
school = {"asli.yoruk": [123, 111]}
student_numbers = {"Zohreh": 123, "Dani": 5.4, "Neeta": [1,2,3]}
for student_name, student_no in student_numbers.items():
    print(f"Student_name is: {student_name}")
    print(f"Student_no is: {student_no}")

for i in student_numbers.keys():
    print(i)

for i in student_numbers.values():
    print(i)   

