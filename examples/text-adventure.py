health = 100
input_value = ""
while health > 0 and input_value != 'quit':
    print("A vicious warg is chasing you.")
    print("Options:")
    print("1 - Hide in the cave.")
    print("2 - Climb a tree.")
    print("Type 'quit' to exit")
    input_value = input("Enter choice:")
    if input_value == '1':
        print('You hide in a cave.')
        print('The warg finds you and injures your leg with its claws')
        health = health - 10
    elif input_value == '2':
        print('You climb a tree.')
        print('The warg eventually looses interest and wanders off')
    print('Your health is:', health)
    input('press enter to continue...')

if health == 0:
    print('You Died!')
