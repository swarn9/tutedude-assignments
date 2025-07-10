#_____________________________Task_1____________________________________________#
try:
    file_1 = open(r'E:\Py_Assignment\Sample.txt', 'r')
    content = file_1.read()
    print("Reading file content:")
    print(content)
    file_1.close()
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")
#_____________________________Task_1_ B ____________________________________________#
try:
    print("Reading file content:")
    with open(r'E:\Py_Assignment\Sample.txt', 'r') as file_1:
        for i, line in enumerate(file_1, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found.")


#_____________________________Task_2____________________________________________#
text = input("Enter text to write to the file : ")
with open("output.txt", "w") as file:
    file.write(text + '\n')
    print("Data sucessfully written to output.txt.")
add_text= input("Enter additional text to append: ")
with open("output.txt","a") as file:
    file.write(add_text + '\n')
    print("Data sucessfully append")
print("Final content of the 'output.txt':")
with open("output.txt","r") as file:
    print(file.read())