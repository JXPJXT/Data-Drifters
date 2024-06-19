import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from itertools import cycle

# Predefined username and password pairs
USERNAMES = ['user1', 'user2', 'user3', 'user4', 'user5']
PASSWORDS = ['password1', 'password2', 'password3', 'password4', 'password5']

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

        self.put_placeholder()

    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)


class LoginApp:
    def __init__(self, root, bg_image_path, form_image_path):
        self.root = root
        self.root.title("FutureNse Login")
        self.root.state('zoomed')  # Make the window full screen
        self.root.resizable(True, True)

        # Create main frames for layout
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side='left', fill='both', expand=True)
        self.right_frame = tk.Frame(root, bg='white')
        self.right_frame.pack(side='left', fill='both', expand=True)  # Changed from 'right' to 'left' to divide equally

        # Load and display background image
        self.bg_image = Image.open(bg_image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.left_frame)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        
        # Resize the background image when the window is resized
        self.left_frame.bind("<Configure>", self.resize_bg_image)

        # Load and display form image
        self.form_image = Image.open(form_image_path)
        self.form_photo = ImageTk.PhotoImage(self.form_image)

        # Create login form in the right frame
        self.create_login_form()

    def resize_bg_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_bg_image = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

    def create_login_form(self):
        form_frame = tk.Frame(self.right_frame, bg='white', padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Add form image
        image_label = tk.Label(form_frame, image=self.form_photo, bg='white')
        image_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username field
        username_label = tk.Label(form_frame, text="Username", font=("Helvetica", 12), bg='white')
        username_label.grid(row=1, column=0, columnspan=2, sticky='w', pady=(20, 5))

        username_frame = tk.Frame(form_frame, bg='white')
        username_frame.grid(row=2, column=0, columnspan=2)

        # Username entry
        self.username_entry = EntryWithPlaceholder(username_frame, placeholder="Username", width=30, font=("Helvetica", 12), bd=1)
        self.username_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=5)

        # Password field
        password_label = tk.Label(form_frame, text="Password", font=("Helvetica", 12), bg='white')
        password_label.grid(row=3, column=0, columnspan=2, sticky='w', pady=(20, 5))

        password_frame = tk.Frame(form_frame, bg='white')
        password_frame.grid(row=4, column=0, columnspan=2)

        # Password entry
        self.password_entry = EntryWithPlaceholder(password_frame, placeholder="Password", width=30, font=("Helvetica", 12), show="*", bd=1)
        self.password_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=5)

        # Remember username checkbox
        remember_var = tk.IntVar()
        remember_check = tk.Checkbutton(form_frame, text="Remember username", variable=remember_var, bg='white')
        remember_check.grid(row=5, column=0, columnspan=2, pady=5)

        # Login button
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="black", foreground="black")
        login_button = ttk.Button(form_frame, text="Log in", style="TButton", command=self.check_credentials)
        login_button.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)

        # Forgotten username or password
        forgotten_label = tk.Label(form_frame, text="Forgotten your username or password?", font=("Helvetica", 10), fg="blue", bg='white')
        forgotten_label.grid(row=7, column=0, columnspan=2, pady=5)

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in USERNAMES and password == PASSWORDS[USERNAMES.index(username)]:
            messagebox.showinfo("Success", "Login Successful!")
            self.show_loading_page()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def show_loading_page(self):
        self.right_frame.destroy()

        loading_window = tk.Toplevel(self.root)
        loading_window.title("Loading")
        loading_window.state('zoomed')
        loading_window.configure(bg='white')

        loading_label = tk.Label(loading_window, text="Logging in...", font=("Helvetica", 16), bg='white')
        loading_label.pack(pady=50)

        spinner = cycle(['|', '/', '-', '\\'])
        spinner_label = tk.Label(loading_window, text="", font=("Helvetica", 24), bg='white')
        spinner_label.pack()

        def animate():
            spinner_label.config(text=next(spinner))
            loading_window.after(100, animate)

        animate()


if __name__ == "__main__":
    bg_image_path = r"C:\Users\bhati\OneDrive\Desktop\Zomato\bg.jpg"
    #form_image_path = r
    root = tk.Tk()
    app = LoginApp(root, bg_image_path, form_image_path)
    root.mainloop()
