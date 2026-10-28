#Q7 Solution

students = {
          101: {"name": "Amit", "marks": 82, "course": "Python"},
          102: {"name": "Neha", "marks": 76, "course": "Java"},
          103: {"name": "Rahul", "marks": 91, "course": "Python"}
}
          
for id, details in students.items():
	if details["marks"]>=80:
		print("Student's Name: ",details["name"])
		print("Student's Course: ",details["course"],"\n")