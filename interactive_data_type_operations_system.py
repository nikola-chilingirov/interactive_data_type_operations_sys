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
        sentence = input("Please input string variables, e.g., Learning Python is fun!: ")
        print(sentence)
        flag = True
        while flag:
    # Extract and print a substring, such as the word "Python" from the sentence.
            word = input("Chose word for your input to extract: ") #print(sentence[9:16])
            if word in sentence:
                new_sentence = sentence.replace(word, '')
                new_sentence = ' '.join(new_sentence.split())
                sentence = new_sentence
                print(f"You choose '{word}' to extract.")
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
        print("You choose Numbers!")
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
    # Perform and print the results of addition, subtraction, multiplication, and division.
        print("Choose number of operation:")
        print(f'1 - Addition')
        print(f'2 - Subtraction')
        print(f'3 - Multiplication')
        print(f"4 - Raising first number to the power of second number")
        print(f'5 - Division')
        choice_op = int(input("Enter the number of operation: "))
        if choice_op == 1:
            print(f'Addition: {num_1} + {num_2} = {num_1 + num_2}')
        elif choice_op == 2:
            print(f'Subtraction: {num_1} - {num_2} = {num_1 - num_2} ')
        elif choice_op == 3:
            print(f'Multiplication: {num_1} * {num_2} = {num_1 * num_2}')
        elif choice_op == 4:
            print(f"{num_1} raised to the power of {num_2} is: {(num_1 ** num_2):.3f}")
        elif choice_op == 5:
            if num_2 == 0:
                print("Division: error, please enter number different from 0")
            else:
                print(f'Division: {num_1} / {num_2} = {num_1 / num_2}')

    # Handle division by zero (e.g., print an error message if num2 is zero).

    # Perform a power operation, raising num1 to the power of num2, and print the result.

    # If the user chooses Booleans (choice == '3'):
    elif choice == '3':
        flag = True
        while flag:
            print("Chose 'Yes' or 'No'.")
            is_python_fun = input("Is learning Python fun?: ")
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
        print('Choose what Additional Data Type want to create.')
        print('1 - List')
        print('2 - Tuple')
        print('3 - Dictionary')
        choice_op_data = int(input('Choose number of type: '))
        if choice_op_data == 1:
            # Create a list with mixed data types (e.g., numbers, strings, booleans).
            print('Now we will create a list with mixed data types.')
            mixed_list = []
            while True:
                data = input('Please input data and when you are ready input END: ')
                if data == "END":
                    break
                flag = True
                try:
                    int(data)
                    new_element = int(data)
                except ValueError:
                    flag = False
                if flag:
                    mixed_list.append(int(data))
                    continue
                try:
                    flag = True
                    float(data)
                    new_element = float(data)
                except ValueError:
                    flag = False
                if flag:
                    mixed_list.append(float(data))
                    continue
                if data.lower() == 'false' or data.lower() == 'true':
                    if data.capitalize() == 'True':
                        data_t = bool(data)
                        mixed_list.append(data_t)
                    else:
                        data_f = bool(not data)
                        mixed_list.append(data_f)
                else:
                    mixed_list.append(data)
                    continue
            print(f"Your list is {mixed_list}")
            print('Now we will check types ot the elements of the list')
            for i in mixed_list:
                print(type(i), end=', ')
    # Append a new element to the list and print the updated list.
            print()
            print('Now we will append a new element to the list.')
            new_element = input('Input new element - integer, float, string or boolean: ')
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
                if new_element.lower() == 'false' or new_element.lower() == 'true':
                    if new_element.capitalize() == 'True':
                        data_t = bool(new_element)
                        mixed_list.append(data_t)
                    else:
                        data_f = bool(not new_element)
                        mixed_list.append(data_f)
                else:
                    mixed_list.append(new_element)
                    break
            print(f"The new list is {mixed_list}")
            print('The elements of the new list are: ')
            for i in mixed_list:
                print(type(i), end=', ')
    # Access and print the 4th element in the list.
            print()
            print("Chose number of list`s element that you want to access.")
            element = int(input("Number of element: "))
            print(f"You choose: {mixed_list[element - 1]}")
    # ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits).
        elif choice_op_data == 2:
            print()
            print('Tuple Operations')
            lst_tuple = []
            while True:
                data = input('Please input data and when you are ready input END: ')
                if data == "END":
                    break
                flag = True
                try:
                    int(data)
                    new_element = int(data)
                except ValueError:
                    flag = False
                if flag:
                    lst_tuple.append(int(data))
                    continue
                try:
                    flag = True
                    float(data)
                    new_element = float(data)
                except ValueError:
                    flag = False
                if flag:
                    lst_tuple.append(float(data))
                    continue
                if data.lower() == 'false' or data.lower() == 'true':
                    if data.capitalize() == 'True':
                        data_t = bool(data)
                        lst_tuple.append(data_t)
                    else:
                        data_f = bool(not data)
                        lst_tuple.append(data_f)
                else:
                    lst_tuple.append(data)
                    continue
            tuple_data = tuple(lst_tuple)
            print(f"Your tuple is {lst_tuple}")
        # Print the length of the tuple.
            print(f"Now we will check the length of the tuple")
            print(f'The length of your tuple is: {len(lst_tuple)}')
            print()

    # Try to modify one element in the tuple and handle the resulting TypeError.
            print('Once a tuple is created, you can not change its values. Tuples are immutable.')
            print('But you can convert the tuple into a list, change the list, and convert the list back into a tuple.')
            print("Let`s do it.")
            tuple_data = list(tuple_data)
            print(f"First we convert our tuple {tuple_data} in list {tuple_data}.")
            print("Let`s change any element in our tuple.")
            temp_lst = []
            old_data = input('Enter data to change: ')
            temp_lst.append(old_data)
            new_data = input('Enter new data: ')
            temp_lst.append(new_data)
            temp_lst_convert = []
            for i in temp_lst:
                flag = True
                try:
                    int(i)
                    new_element = int(i)
                except ValueError:
                    flag = False
                if flag:
                    temp_lst_convert.append(int(i))
                    continue
                try:
                    flag = True
                    float(i)
                    new_element = float(i)
                except ValueError:
                    flag = False
                if flag:
                    temp_lst_convert.append(float(i))
                    continue
                if i.lower() == 'false' or i.lower() == 'true':
                    if i.capitalize() == 'True':
                        i_t = bool(i)
                        temp_lst_convert.append(i_t)
                    else:
                        i_f = bool(not i)
                        temp_lst_convert.append(i_f)
                else:
                    temp_lst_convert.append(i)
                    continue

            index_tuple_list = tuple_data.index(temp_lst_convert[0])
            tuple_data[index_tuple_list] = temp_lst_convert[1]
            new_tuple = tuple(tuple_data)
            print(f"Your new tuple is: {new_tuple}")
            print()

        elif choice_op_data == 3:
    # Create a dictionary with some key-value pairs (e.g., name, age, city).
            print('Dictionary Operations')
            new_dictionary = {}
            while True:
                key = input('Input key, when finish input END: ')
                if key == "END":
                    break
                value = input('Input value: ')
                new_dictionary[key] = value
                continue
            print(f"This is your Dictionary: {new_dictionary}")
            # Access and print the value for one of the keys (e.g., "age").
            key = input(f"Chose one of the key from your dictionary to print its value: ")
            key_print = new_dictionary[key]
            print(f"The value of {key} is {key_print}")
            print()
            # Add a new key-value pair to the dictionary and print the updated dictionary.
            print('We add new key-value to our dictionary')
            new_key = input(f"Input new key: ")
            new_value = input(f"Input new value: ")
            new_dictionary.update({new_key: new_value})
            print(f"This is update dictionary: {new_dictionary}")
            # If the user enters an invalid choice:

