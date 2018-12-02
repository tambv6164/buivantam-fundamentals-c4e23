from pymongo import MongoClient

uri = "mongodb://admin:admin1@ds251747.mlab.com:51747/movie"
client = MongoClient(uri)
db = client.get_database()
todos = db["todos"]

command = ["New Todo", "View all Todos", "Mark a Todo COMPLETED", "Delete a Todo", "Exit"]

def show_command():
    for idx, val in enumerate(command):
        print(str(idx + 1) + '. ' + val)

def wait_enter():
    input('Press Enter to continue ...')


while True:
    show_command()
    choice = int(input('Enter your command:  '))

    if choice == 1:
        name = input('Name: ')
        des = input('Description: ')
        new_todo = {'Name': name, 'Description': des}
        todos.insert_one(new_todo)
        wait_enter()
        
    elif choice == 2:
        print('= = = = = = = = = = = = = = = = = = = =')
        todos_list = todos.find()
        # if todos_list != None:
        #     print('EMPTY')
        print(type(todos_list))
        # else:
        #     for todo in todos_list:
        #         for k, v in todo.items():
        #             print(k, ': ', v)
        #             print()
        print('= = = = = = = = = = = = = = = = = = = =')
        wait_enter()

    elif choice == 3:
        update_position = input('Which one: ')
        
        #############

        print('Updated')
        wait_enter()

    elif choice == 4:
        delete_position = input('Which one: ')

        #############

        print('Deleted')
        wait_enter

    elif choice == 5:
        wait_enter()
        break

client.close()