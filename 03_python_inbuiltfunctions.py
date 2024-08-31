# Name =Ayesha Shahid
# RollNo = PIAIC245513

# 1. Simple Message
msg : str ="Hello, I am learning Python programming language."
print(msg)
#2. Simple Messages
msg1 : str ="Hi"
print(msg1)
msg1 : str ="Bye"
print(msg1)
#3. Personal Message
name : str ="Ayesha"
print(f"Hello {name} , would you like to learn python with me?")
#4. Name Cases
name : str = "Ayesha shahid"
print(name.title())
print(name.upper())
print(name.lower())
#5. Famous Quote
quote :str ="A plan backed by action makes your dreams come true."
print(f"Greg Reid once said,{quote}")
#6. Famous Quote 2
quote:str = "A plan backed by action makes your dreams come true."
famous_person :str ="Greg Reid"
print(f"{famous_person} once said, {quote}")
#7. Stripping Names
greeting : str = "\t\tHello,\n Ayesha \t Shahid!\t\t"
print(greeting)
print(greeting.lstrip())
print(greeting.rstrip())
print(greeting.strip())
#8. Variable Sum
x : int =5
y :int =10
z :int=15
i :int = x+y+z
print(i)
#9. Variable Swap
a :int =10
b :int =20
print(f"Before swapping a={a} and b={b}")
temp :int
temp = a
a=b
b=temp
print(f"After swapping a={a} and b={b}")
#10. Favorite Color
fav_clr :str ="black"
print(f"My favorite color is {fav_clr}")
clr :str = fav_clr
print(f"My favorite color is {clr}")
#11. Changing Pet Name
pet_name:str ="Buddy"
pet_name:str ="Max"
print(f"My pet name is {pet_name}")
#12. Observing Name Error
sunshine :str = "Sunshine"
# print(sunsine ) ---->NameError: name 'sunsine' is not defined. Did you mean: 'sunshine'?
# 13. Reassigning Score
score :int = 100
print(score)
score = 200
print(score)
#14. City Name
city_name :str= "Lahore"
print(f"I live in {city_name}")
# 15. Title Case Text
text :str ="Python programming"
print(text.title())
# 16. Lowercase Conversion
mixed :str ="PYthoN PrograMmiNg"
print(mixed.lower())
# 17. Uppercase Conversion
mixed1:str ="PYthoN PrograMmiNg"
print(mixed1.upper())
# 18. Current Temperature
temp :  float = 25
print(f"The current temperature is {temp}  degree celsius")
# 19. Printing a Poem
poem :str = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""

print (poem)
