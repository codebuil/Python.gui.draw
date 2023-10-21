import tkinter as tk
from tkinter import filedialog

class DrawingApp:
    def __init__(self, root):
        self.root = root
        root.title("Drawing App")

        self.canvas_visible = True

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.textbox = tk.Text(root)
        self.textbox.pack(fill=tk.BOTH, expand=True)
        self.textbox.insert(tk.END, "Text will appear here")

        self.button_open = tk.Button(root, text="Abrir Ficheiro", command=self.open_file)
        self.button_save = tk.Button(root, text="Guardar", command=self.save_text)
        self.button_toggle = tk.Button(root, text="Recolher/Mostrar", command=self.toggle_canvas)
        self.button_draw = tk.Button(root, text="Redesenhar Canvas", command=self.redraw_canvas)

        self.button_open.pack()
        self.button_save.pack()
        self.button_toggle.pack()
        self.button_draw.pack()

        self.start_x = 0
        self.start_y = 0
        self.rect = None

        self.canvas_hidden = False

    def on_mouse_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_release(self, event):
        end_x = event.x
        end_y = event.y
        width = end_x - self.start_x
        height = end_y - self.start_y
        if width > 0 and height > 0:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline="black")

            text = f"boxs({self.start_x},{self.start_y},{width},{height});\n"
            self.textbox.insert(tk.END, text)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, content)

    def save_text(self):
        text = self.textbox.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)

    def toggle_canvas(self):
        if self.canvas_hidden:
            self.canvas.pack(fill=tk.BOTH, expand=True)
        else:
            self.canvas.pack_forget()
        self.canvas_hidden = not self.canvas_hidden

    def redraw_canvas(self):
        if self.rect:
            self.canvas.delete(self.rect)
            self.textbox.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

