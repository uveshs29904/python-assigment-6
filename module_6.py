#Task 1
students={
    'Alice':85,
    'Bob':90,
    'Charlie':70,
    'David':45,
    'Eve':96,
}
input=input("Enter the Student's  Name:")

if input in students:
    print(input,'s ','Marks: ',students[input])
else:
    print("Student not found.")

#Task 2: Demonstrate List Slicing
list=[1,2,3,4,5,6,7,8,9,10]
print("Orignal List: ",list)
extracted_list=list[:5]
print("Extracted First Five Elemnts: ",extracted_list)
extracted_list.reverse()
print("Reversed Extrected Elements",extracted_list)
