#Q2 Solution

departments =  {
        "IT" : {"Head": "Amit", "Employees": 25},        "HR" : {"Head": "Neha", "Employees": 12}
}

for dept, details in departments.items():
	if dept=="IT":
		print("The head is:",details["Head"])
		print("The no. of employees:",details["Employees"])

