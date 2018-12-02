from todo import Todo
import mlab

mlab.connect()
command = ["New Todo", "View all Todos", "Mark a Todo COMPLETED", "Delete a Todo", "Exit"]

while True:
    for idx, val in enumerate(command):
        print(str(idx + 1) + '. ' + val)
    
    todos_list = Todo.objects()
    
    choice = int(input('Enter your command:  '))
    while choice not in [1, 2, 3, 4, 5]:
        choice = int(input('Please type 1, 2, 3, 4, or 5:  '))

    if choice == 1:
        name = input('Name: ')
        des = input('Description: ')
        new_todo = Todo(name=name, des=des)
        new_todo.save()

    elif choice == 2:
        print('= = = = = = = = = = = = = = = = = = = =')
        if todos_list.first() == None:
            print('EMPTY')
        else:
            for idx, todo in enumerate(todos_list):
                print(str(idx + 1) + '. Name: ' + todo.name)
                print('Description: ' + todo.des)
                print('Completed: ' + todo.available)
                print()
        print('= = = = = = = = = = = = = = = = = = = =')

    elif choice == 3:
        update_position = int(input('Which one: '))
        todos_list[update_position - 1].update(set__available='Yes')
        print('Updated')

    elif choice == 4:
        delete_position = int(input('Which one: '))
        todos_list[delete_position - 1].delete()
        print('Deleted')

    input('Press Enter to continue ...')

    if choice == 5:
        break
