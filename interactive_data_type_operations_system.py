# Prompt the user to choose a data type to perform operations on

# Get the user's choice and store it in a variable
while True:
    print("Choose a data type to perform operations on:")
    print("1. Strings")
    print("2. Numbers")
    print("3. Booleans")
    print("4. Additional Data Types (List, Tuple, Dictionary)")
    print("5. End program")
    choice = input("Enter the number of your choice (1-5): ")
    if choice == '5':
        break
    if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
        print('Wrong number, please try again.')
        continue
        #choice = input("Enter the number of your choice (1-4): ")
    # If the user chooses Strings (choice == '1'):

    if choice == '1':
    # Declare a string variable, e.g., sentence = "Learning Python is fun!"
        sentence = "Learning Python is fun!"
        print(sentence)
        flag = True
        while flag:
    # Extract and print a substring, such as the word "Python" from the sentence.
            word = input("Chose word to extract: ") #print(sentence[9:16])
            if word in sentence:
                new_sentence = sentence.replace(word, '')
                new_sentence = ' '.join(new_sentence.split())
                sentence = new_sentence
                print(word)
                print(f"The new sentence is: {new_sentence}")
                flag = False
            else:
                print("The word is not in the sentence.")
    # Convert the entire sentence to uppercase and print it.
        print("Now we will convert sentence to uppercase.")
        sentence = sentence.upper()
        print(sentence)
    # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
        print("Now we will replace word in the sentence.")
        flag = True
        while flag:
            word_to_rep = input("Chose word to replace: ")  # print(sentence[9:16])
            if word_to_rep in sentence:
                new_word = input(f"Chose word with which we will replace {word_to_rep}: ")
                new_sentence = sentence.replace(word_to_rep, new_word)
                print(f"The new sentence is: {new_sentence}")
                flag = False
            else:
                print("The word is not in the sentence.")
    # If the user chooses Numbers (choice == '2'):
    elif choice == '2':
    # Prompt the user to input two numbers, e.g., num1 and num2.
        print("You chose Numbers!")
        num_1 = float(input("Enter the first number:" ))
        num_2 = float(input("Enter the second number:" ))
    # Perform and print the results of addition, subtraction, multiplication, and division.
        print(f'Addition: {num_1 + num_2}')
        print(f'Subtraction: {num_1 - num_2}')
        print(f'Multiplication: {num_1 * num_2}')
        print(f"{num_1} raised to the power of {num_2} is: {(num_1 ** num_2):.3f}")
        if num_2 == 0:
            print("Division: error, please enter number different from 0")
        else:
            print(f'Division: {num_1 / num_2}')

    # Handle division by zero (e.g., print an error message if num2 is zero).

    # Perform a power operation, raising num1 to the power of num2, and print the result.

    # If the user chooses Booleans (choice == '3'):
    elif choice == '3':
        flag = True
        while flag:
            print("Chose 'Yes' or 'No'.")
            is_python_fun = input("Is learning Python fun? : ")
            if is_python_fun == 'Yes':
                is_python_fun = True
            else:
                is_python_fun = False
            is_sunny = input("Is weather sunny?: ")
            if is_sunny == 'Yes':
                is_sunny = True
            else:
                is_sunny = False
            if is_sunny and is_python_fun:
                print("Let continue learning Python outside.")

            elif is_python_fun and not is_sunny:
                print("Let continue learning Python at home.")
            elif not is_python_fun or not is_sunny:
                print("Let continue learning Python and we will see what`s next.")
            print("If you want to try again insert Yes or No.")
            answer = input()
            if answer == 'Yes':
                flag = True
            else:
                flag = False
        print("Let`s see the result of comparison operations")
        print('Enter two numbers.')
        num_1 = input('Enter number one: ')
        num_2 = input('Enter number two: ')
        if num_1 > num_2:
            print(f'{num_1} > {num_2}')
        elif num_1 < num_2:
            print(f'{num_1} < {num_2}')
        else:
            print(f'{num_1} = {num_2}')

    # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.

    # Perform and print the results of logical operations: AND, OR, NOT.

    # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).

    # If the user chooses Additional Data Types (choice == '4'):
    elif choice == '4':
    # ### List Operations ###
        print('List Operations')
    # Create a list with mixed data types (e.g., numbers, strings, booleans).
        print('Now we will create a list with mixed data type.')
        mixed_list = []
        txt = 'Please input integer, float and string'
        print(txt)
        while True:
            integer = input('Input integer: ')
            if ord(integer[0]) == 45 and integer[1:].isdigit():
                mixed_list.append(int(integer))
                break
            elif integer.isdigit():
                mixed_list.append(int(integer))
                break
            else:
                print('Wrong input, please try again.')
                continue
        while True:
            float_data = input('Input float: ')
            if ord(float_data[0]) == 45 and '.' in float_data:
                float_data_temp = float_data.replace('-', '', 1).replace('.', '', 1)
                if len(float_data_temp) == (len(float_data) - 2):
                    mixed_list.append(float(float_data))
                break
            elif 48 <= ord(float_data[0]) <= 57 and '.' in float_data:
                float_data_temp = float_data.replace('.', '', 1)
                if len(float_data_temp) == (len(float_data) - 1):
                    mixed_list.append(float(float_data))
                break
            else:
                print('Wrong input, please try again.')
                continue
        string_data = input('Input string: ')
        mixed_list.append(string_data)
        print(f"Your list is {mixed_list}")
        print('Now we will check types ot the elements of the list')
        for i in mixed_list:
            print(type(i))
    # Append a new element to the list and print the updated list.
        print('Now we will append a new element to the list.')
        new_element = input('Input new element - integer, float or string: ')
        flag = True
        for x in range(1):
            try:
                int(new_element)
                new_element = int(new_element)
            except ValueError:
                flag = False
            if flag:
                mixed_list.append(int(new_element))
                break
            try:
                flag = True
                float(new_element)
                new_element = float(new_element)
            except ValueError:
                flag = False
            if flag:
                mixed_list.append(float(new_element))
                break
            else:
                mixed_list.append(new_element)
                break
        print(f"The new list is {mixed_list}")
        print('The elements of the new list are: ')
        for i in mixed_list:
            print(type(i))
    # Access and print the 4th element in the list.
        print("Chose number of list`s element that you want to access.")
        element = int(input("Number of element: "))
        print(f"You choose: {mixed_list[element - 1]}")
    # ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits).
        print()
        print('Tuple Operations')
        print('Input your three favourite fruits:')
        lst = []
        for f in range(3):
            fruit = input()
            lst.append(fruit)
        tuple_fruit = tuple(lst)
        print(f"This is tuple with your favourite fruits: {tuple_fruit}")
    # Print the length of the tuple.
        print(f"Now we will check the length of the tuple: {len(tuple_fruit)}")
        print()
    # Try to modify one element in the tuple and handle the resulting TypeError.
        print('Once a tuple is created, you cannot change its values. Tuples are immutable.')
        print('But you can convert the tuple into a list, change the list, and convert the list back into a tuple.')
        print("Let`s do it.")
        lst_fruit = list(tuple_fruit)
        print(f"First we convert our tuple {tuple_fruit} in list {lst_fruit}.")
        print("Let`s change any fruit in our tuple.")
        old_fruit = input('Chose fruit to change: ')
        new_fruit = input('Chose new fruit: ')
        a = lst_fruit.index(old_fruit)
        lst_fruit[a] = new_fruit
        new_tuple = tuple(lst_fruit)
        print(f"Your new tuple is: {new_tuple}")
        print()
    # ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city).
        print('Dictionary Operations')
        new_dict = {'name': '', 'age': '', 'city': ''}
        name = input('Input your name: ')
        age = input('Input your age: ')
        city = input('Input your city: ')
        new_dict['name'] = name
        new_dict['age'] = age
        new_dict['city'] = city
        print(f"This is your Dictionary: {new_dict}")
    # Access and print the value for one of the keys (e.g., "age").
        key = input(f"Chose one of the key from your dictionary to print its value: ")
        b = new_dict[key]
        print(f"This is value {b} of key {key}")
        print()
    # Add a new key-value pair to the dictionary and print the updated dictionary.
        print('We add new key-value to our dictionary')
        new_key = input(f"Input your home town: ")
        new_dict.update({'home town': new_key})
        print(f"This is update dictionary: {new_dict}")
    # If the user enters an invalid choice:

