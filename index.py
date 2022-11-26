import tkinter as tk
import customtkinter as ctk

from buttons import alphabet


def main():
    ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")  # set_default_color_theme("blue")  # Themes: "blue" (standard),
    # "green", "dark-blue"

    root = tk.Tk()
    root.title("Words Guessing Game")
    root.geometry("900x500")
    root.minsize(width=1080, height=720)
    root.maxsize(width=1080, height=720)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    main_frame = ctk.CTkFrame(root)

    main_frame.grid(row=0, column=0, sticky="nsew")

    alphabet(main_frame)

    root.mainloop()


if __name__ == "__main__":
    main()
