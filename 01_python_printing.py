#Name =Ayesha Shahid
#roll no = PIAIC245513
#1 - Basic Printing
print("Hello, World!")
first_name="Ayesha" ## first_name is a string
print(first_name)


### 2- Printing Multiple Items:
last_name= " Shahid " ## last_name is a string
print(first_name+last_name)

print("1,2 and 3")

### 3. Printing Special Characters:
print("Hello\nWorld")
print("Hello\tWorld")

### 4. Using the sep Parameter:
print("apple","banana","cherry",sep=", ") ## here separator is ,
print("1","2","3",sep="-")  ## here separator is -

### 5. Using the end Parameter:
print("Hello",end=" ")
print("World")

print(1,end="")  
print(2)

### 6. Escape Characters:

print('He said , "Hello!')

print("This is a backslash: \\")

### 7. Combining Text and Numbers:

age=18  ### age is an integer or float

print("I am",age,"years old")

print("The number is",5)


### 8. Basic Loop for Printing:
for i in range(1,6):
    print(i)