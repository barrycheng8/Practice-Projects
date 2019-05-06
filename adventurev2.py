import random
import sys

def msg(room):
    #checks if there is a room message. No room message means it has not been entered yet
    if room['msg'] == '':
        return 'You have entered the ' + room['name'] + '.'
    else:
        return room['msg']

def get_choice(room, location):
    if location.upper() == 'N':
        choice = 0
    elif location.upper() == 'S':
        choice = 1
    elif location.upper() == 'W':
        choice = 2
    elif location.upper() == 'E':
        choice = 3
    elif location.upper() == 'Q':
        sys.exit()
    else:
        return -1

    if room['location'][choice] == 0:
        return 4
    else:
        return choice

def main():
    location = (0, 0, 0, 0) #default location, (N, S, W, E)

    #available rooms
    entrance = {'name': 'Entrance', 'location': location, 'msg': ''}
    forkroom = {'name': 'Fork Road Room', 'location': location, 'msg': ''}
    westroom = {'name':  'West Hallway', 'location': location, 'msg': ''}
    westend = {'name': 'West Closet', 'location': location, 'msg': ''}
    eastroom = {'name': 'East Hallway', 'location': location, 'msg': ''}
    eastend = {'name': 'East Closet', 'location': location, 'msg': ''}

    #directions are in tuple format so they cannot be modified
    entrance['location'] = (forkroom, 0, 0, 0)
    forkroom['location'] = (0, entrance, westroom, eastroom)
    westroom['location'] = (westend, 0, 0, forkroom)
    westend['location'] = (0, westroom, 0, 0)
    eastroom['location'] = (eastend, 0, forkroom, 0)
    eastend['location'] = (0, eastroom, 0, 0)

    #randomly places the escape key in a room
    rooms = [forkroom, westroom, westend, eastend, eastroom]
    room_key = random.choice(rooms)
    key_obtained = False
    room = entrance
    print('Welcome to the Python Escape Room!')

    while True:
        if key_obtained and room['name'] == 'Entrance':
            print('You found the key and reached the entrance again! You\'ve escaped the room!')
            break
        elif not key_obtained and room['name'] == room_key['name']:
            key_obtained = True
            print(msg(room) + ' You found the key! Return to the entrance quickly before time runs out!')
            room['msg'] = ('You are back in the ' + room['name'] + '. Unless you want to take a nap here '
                                       'and run out of time, I suggest you quickly find the entrance!')
        else:
            print(msg(room))
            room['msg'] = 'You are back in the ' + room['name']

        stuck = True
        while stuck:
            location = input('Which direction would you like to go? (Options: N, S, W, E). Q to quit. ')
            choice = get_choice(room, location)
            if choice == -1:
                print('You are only allowed to enter the following directions: N, S, E, W. Type "Q" to quit.')
            elif choice == 4:
                print('There is no room in that direction!')
            else:
                room = room['location'][choice]
                stuck = False

if __name__ == '__main__':
    main()
