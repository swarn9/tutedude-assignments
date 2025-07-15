#______________________________Task-1___________________________________________________#

Student_details= {'raj':20, 'singh':30, 'swarn':60,'alice':55, 'rajniesh':77}
name = (input("Enter the student's name :"))
if name in Student_details:
    print(f"{name}'s marks : {Student_details[name]}")
    
else:
    print("student not found")
    
    
#______________________________Task-2___________________________________________________#

current_list =list(range(1,11))
extracted_list=(current_list[0:5])
reverse_list= (extracted_list[::-1])
print(current_list)
print(extracted_list)
print(reverse_list)
