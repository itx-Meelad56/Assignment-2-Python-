#  Assignment 2

# Take an integer from the user and check whether it is even or odd. 

num = int(input('give number'))

if num % 2 == 0 :
    print(f'Even Number {num}')
else : 
    print(f'Odd Number {num}')


#  Take a number and check whether it is positive or negative.

if num > 0 :
    print(f'Positive Number {num}')
elif num < 0 : 
    print(f'Negative Number {num}')
else :
    print(f'Zero {num}')


#  Take a person's age and check whether they are eligible to vote. Assume the minimum voting age is 18.

age = int(input('what is your age'))

if age >= 18 :
    print(f'eligible for this age {age}')
else :
    print(f'not eligible for this age {age}')


# Take two numbers from the user and print the greater number. If both numbers are equal, display an appropriate message.

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

if num1 > num2 :
    print('first number greater than second number')
elif num2 > num1 :
    print('second number greater than first number')
else : 
    print('both number are equal')


# Take a password from the user and check whether it matches a predefined password.

password = 'python123'
userPassword = input('Enter Password')

if password == userPassword :
    print('password correct')
else : 
    print('incorrect password')


# Take a student's marks and check whether the student has passed or failed. Assume 50 marks are required to pass.


marks = int(input('enter your marks'))

if marks >= 50 :
    print('Pass')
else : 
    print('Fail')


# Take a student's marks out of 100 and assign a grade according to the following criteria:
### 90–100: A+
### 80–89: A
### 70–79: B
### 60–69: C
### 50–59: D
### Below 50: Fail

if marks >= 80 : 
    print('Your Grade A')
elif marks >= 70 : 
    print('Your Grade B')
elif marks >= 60 :
    print('Your Grade C')
elif marks >= 50 : 
    print('Your Grade D')
else :
    print ('You Fail')


# Create a simple calculator that takes two numbers and an operator (+, -, *, /). Perform the selected operation and display an appropriate message if the operator is invalid.

operator = input('give operator')

if operator == '+' :
    solution = num1 + num2
elif operator == '-' :
    solution = num1 - num2
elif operator == '/' :
    solution = num1 / num2
elif operator == '*' :
    solution = num1 * num2
else :
   print('this operator not allowed')
print(solution)


# Take the temperature in input and display the following messages:
### Above 35: Very Hot
### 25–35: Hot
### 15–24: Moderate
### 5–14: Cold
### Below 5: Very Cold

temperature = int(input('enter temperature'))

if temperature > 35 :
    print('Very Hot')
elif temperature >= 25 :
    print('Hot')
elif temperature >= 15 :
    print('Moderate')
elif temperature >= 5 :
    print('Cold')
else :
    print('Very Cold')


# Create a simple ticket-pricing program based on age:
### Below 5: Free
### 5–12: Child Ticket
### 13–17: Teen Ticket
### 18–59: Adult Ticket
### 60 and above: Senior Citizen Ticket

if age < 5 :
    print('Ticket Free')
elif age >= 5 and age <= 12:
    print('Child Ticket')
elif age >= 13 and age <= 17 :
    print('Teen Ticket')
elif age >= 18 and age <= 59 :
    print('Adult Ticket') 
else :
    print('Senior Citizen Ticket')



# Create an electricity bill calculator using the following units:
### 0 to 100 units: Rs. 10 per unit
### 101–200 units: Rs. 15 per unit
### Above 200 units: Rs. 20 per unit
### Take the consumed units as input and calculate the bill according to the applicable rate.


units = int(input('give your electric bill units'))

if units >= 0 and units <= 100 :
    print('10 per unit')
elif units > 100 and units <= 200 :
    print('15 per unit')
else :
    print('Rs. 20 per unit')


# Take a user's age and monthly income. Determine whether they are eligible for a fictional loan using these conditions: age must be at least 21 and monthly income must be at least Rs. 50,000.

monthly_income = int(input('enter your monthly income'))

if age == 21 and monthly_income >= 50000 :
    print('Eligible')
else :
    print('Not Eligible')


# Take the total shopping amount and calculate the discount category:
### Below Rs. 2,000: No Discount
### Rs. 2,000–4,999: 5% Discount
### Rs. 5,000–9,999: 10% Discount
### Rs. 10,000 and above: 20% Discount

shopping_amount = int(input("enter your shopping ammount"))

if shopping_amount < 2000 :
    discount = 'No Discount'
elif shopping_amount >= 2000 and shopping_amount < 5000 :
    discount = '5% Discount'
elif shopping_amount >= 5000 and shopping_amount < 10000 :
    discount = '10% Discount'
else : 
    discount = '20% Discount'
print(discount)


# Take the number of GB used by a customer and display the usage category:
### Below 5 GB: Low Usage
### 5–20 GB: Normal Usage
### 21–50 GB: High Usage
### Above 50 GB: Very High Usage

gb = int(input('enter your GB'))

if gb < 5 :
    print('Low Usage')
elif gb >= 5 and gb < 21 :
    print('Normal Usage')
elif gb >= 21 and gb < 51 :
    print('High Usage')
else :
    print('Very High Usage')



# Take an employee's years of experience and monthly salary. Determine their bonus category based on these conditions:
### Experience below 1 year: No Bonus
### Experience of 1–3 years: 5% bonus
### Experience above 3 years and salary below Rs. 100,000: 10% bonus
### Experience above 3 years and salary of Rs. 100,000 or more: 15% bonus

experience = float(input("Enter your years of experience: "))
salary = float(input("Enter your monthly salary: "))

if experience < 1:
    bonus_percent = 0

elif experience <= 3:
    bonus_percent = 5

elif experience > 3 and salary < 100000:
    bonus_percent = 10

else:
    bonus_percent = 15

bonus_amount = salary * bonus_percent / 100

print(f"Monthly Salary: Rs. {salary:.2f}")
print(f"Bonus Percentage: {bonus_percent}%")
print(f"Bonus Amount: Rs. {bonus_amount:.2f}")



# Ask the user to enter a username and password.
### First, check whether the username is correct.
### If the username is correct, check the password.
### Display an appropriate message for successful or unsuccessful login.


correct_username = "meelad"
correct_password = "12345"

username = input("Enter username: ")

if username == correct_username:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password!")
else:
    print("Incorrect username!")



# Take the account balance and withdrawal amount as input.
### First, check whether the withdrawal amount is greater than zero.
### If valid, check whether the account has sufficient balance.
### If sufficient balance is available, process the withdrawal and display the remaining balance.



balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw > 0:
    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")
else:
    print("Withdrawal amount must be greater than zero!")



# Take the user's age and monthly income as input.
### First, check whether the user is at least 21 years old.
### If eligible by age, check whether the monthly income is at least Rs. 50,000.
### Display whether the user meets the basic loan eligibility criteria



age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))

if age >= 21:
    if income >= 50000:
        print("You are eligible for the loan!")
    else:
        print("Your income is too low.")
else:
    print("You must be at least 21 years old.")



# Complete Assignment 



