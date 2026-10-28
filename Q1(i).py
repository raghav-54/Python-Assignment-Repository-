#Q1 from Python Mid Term

products= [
["Laptop", 55000], ["Mobile", 25000], 
["Tablet", 18000]
]
for data in products:
	if data[0]=="Mobile":
		print("The product is:",products[1][0])
		print("The price is:",products[1][1])