import random
import string

def generate_password(length, complexity):
    if complexity == "1":
        characters = string.ascii_letters + string.digits
    elif complexity == "2":
        characters = string.ascii_letters + string.digits + string.punctuation.replace("'", "").replace('"', '').replace("\\", "").replace("`", "").replace("^", "")
    elif complexity == "3":
        characters = string.printable.replace("'", "").replace('"', '').replace("\\", "").replace("`", "").replace("^", "")
    else:
        raise ValueError("Invalid complexity level. Please choose from 'easy', 'medium', or 'hard'.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = input("Enter the complexity level(1/2/3) of the password \n 1.easy\n 2.medium\n 3.hard\nSelect the option :")
        
        password = generate_password(length, complexity)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

#OUTPUT

'''
Enter the desired length of the password: 5
Enter the complexity level(1/2/3) of the password
 1.easy
 2.medium
 3.hard
Select the option :1
Generated Password: gb9en
'''
