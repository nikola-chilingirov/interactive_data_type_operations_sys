# interactive_data_type_operations_sys
Dynamic script where the user gets to choose a data type and perform related operations

Prompt the user with a menu to select from five options:

1. Strings
2. Numbers
3. Booleans
4. Additional Data Types (List, Tuple, Dictionary)
5. End program
6. 
Example

![image](https://github.com/user-attachments/assets/64b03367-93f9-41f3-acc8-e0957579f9db)

**Operations Based on User Choice:**

- **Strings:**

   - Declare a string variable (sentence = "Learning Python is fun!").
   - Extract a substring (e.g., "Python") using string slicing and display it.
   - Convert the string to uppercase and print it.
   - Replace a word in the string (e.g., replace "fun" with "awesome") and print the result.

- **Numbers:**

   - Prompt the user to input two numbers (num1 and num2).
   - Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
   - Handle the case where the second number is zero to avoid division by zero errors.
   - Calculate the power of one number raised to another and print the result.

- **Booleans:**

   - Declare two boolean variables (is_python_fun = True and is_sunny = False).
   - Perform logical operations (AND, OR, NOT) on these variables and display the results.
   - Perform comparison operations (e.g., 10 > 5, 5 == 5) and print the outcomes.

- **Additional Data Types:**

   - **List**: Create a list with mixed data types ([1, 3.14, "Python"]).
      - Append an item to the list and print the updated list.
      - Access and print the 4th element in the list.
        
   - **Tuple**: Create a tuple with a few items (e.g., fruits: ("apple", "banana", "cherry")).
      - Print the length of the tuple.
      - Modify an element (and handle the resulting TypeError).
  
   - **Dictionary**: Create a dictionary with key-value pairs (e.g., {"name": "Nick", "age": 30, "city": "Sofia"}).
      - Access and print the value for the key "age".
      - Add a new key-value pair (e.g., "home town": "Smolian") and print the updated dictionary.
