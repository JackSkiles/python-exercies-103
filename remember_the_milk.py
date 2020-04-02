
count = 0
groceries = ''

# Iterates three times to add three user inputs for a grocery list.
while count < 3:
    # Each loop will had groceries to groceries new total
    groceries = groceries + input('What do you need from the store today? ')
    groceries = groceries + '\n' # Adds a line break after each item
    count += 1
print(f'Here is your grocery list:\n{groceries}')