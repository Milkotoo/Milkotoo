import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Зміна напису")

        self.label_text = "Початковий напис"
        self.label = tk.Label(root, text=self.label_text)
        self.label.pack(pady=20)

        self.button_count = 0
        self.button = tk.Button(root, text="Змінити напис", command=self.change_text)
        self.button.pack()

        self.label_count = tk.Label(root, text="Кількість клацань: 0")
        self.label_count.pack(pady=10)

    def change_text(self):
        self.button_count += 1
        self.label_count.config(text=f"Кількість клацань: {self.button_count}")

        if self.button_count % 2 == 1:
            self.label_text = "Новий напис"
        else:
            self.label_text = "Початковий напис"

        self.label.config(text=self.label_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
