import random
import string
print("""
*****   Welcome to the password Genrator *****
""")
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation
password=[]
pass_length=int(input("Enter the password length:    "))
l_l=int(input("Enter the number of letters:\t"))
s_l=int(input("Enter the number of symbols:\t"))
n_l=int(input("Enter the number of numbers:\t"))
while pass_length!=l_l+s_l+n_l:
    print("invalid input... the sum of letters, numbers and symbols doesn't match the password length")
    pass_length=int(input("Enter the password length:\t"))
    letters=int(input("Enter the number of letters:\t"))
    symbols=int(input("Enter the number of symbols:\t"))
    numbers=int(input("Enter the number of numbers:\t"))
l_x=random.choices(letters, k=l_l)
n_x=random.choices(numbers, k=n_l)
s_x=random.choices(symbols, k=s_l)
password=l_x+n_x+s_x
random.shuffle(password)
print(f"Generated Password:\n{''.join(password)}")
