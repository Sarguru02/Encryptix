import tkinter as tk
from tkinter import messagebox
from todo import addTodo, deleteTodo, getTodos, toggleTodo, updateTodo
from comp import TodoComp

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todolist")

        self.input_label = tk.Label(master, text="Enter Item:")
        self.input_label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.add_button = tk.Button(master, text="Add", command=self.add_item)
        self.add_button.pack()

        self.display_frame = tk.Frame(master)
        self.display_frame.pack()

        self.display_items()

    def add_item(self):
        item_text = self.input_entry.get()
        if item_text:
            addTodo(item_text)
            self.input_entry.delete(0, 'end')
            self.display_items()

    def delete_item(self, id):
        deleteTodo(id)
        self.display_items()

    def edit_item(self, id):
        new_text = messagebox.askokcancel("Edit Item", "Enter new text for the item:")
        if new_text:
            updateTodo(id, new_text)
            self.display_items()

    def toggle_completion(self, id):
        toggleTodo(id)
        self.display_items()

    def display_items(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        for id, todo, completed in getTodos():
            var = tk.BooleanVar(value=completed)
            comp = TodoComp(self.display_frame, todo, "Edit", "Delete",button1_command=lambda: self.edit_item(id), button2_command=lambda: self.delete_item(id), completed=completed, checkbox_command=lambda: self.toggle_completion(id))
            comp.pack()





def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
