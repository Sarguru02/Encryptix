import pickle

counter =0
try:
    with open('todos.dat', 'rb') as f:
        todos = pickle.load(f)
        print(todos)
        counter = len(todos)
except: 
    todos = []



def addTodo(todo):
    global counter
    todos.append((counter, todo, False))
    counter+=1
    saveTodos()

def deleteTodo(id):
    for i in range(len(todos)):
        if todos[i][0] == id:
            del todos[i]
    saveTodos()


def updateTodo(id, todo):
    for i in range(len(todos)):
        if todos[i][0] == id:
            todos[i] = (id, todo, todos[i][2])
            saveTodos()

def getTodos():
    return todos

def saveTodos():
    f = open('todos.dat', 'wb')
    pickle.dump(todos, f)
    f.close()

def toggleTodo(id):
    for i in range(len(todos)):
        if todos[i][0] == id:
            todos[i] = (todos[i][0], todos[i][1], not todos[i][2])
            saveTodos()
