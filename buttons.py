import customtkinter as ctk

from design import Ft


def button_click(args):
    if args == "1":
        d1 = ctk.CTkToplevel()
        d1.minsize(height=250, width=500)
        d1.title("01.12")
        d1_label = ctk.CTkLabel(d1, text_font=Ft.txt, text="  \r\nprint(Hello World!)\r\n ")
        d1_label.pack()
    if args == "2":
        d2 = ctk.CTkToplevel()
        d2.minsize(height=250, width=500)
        d2.title("02.12")
        d2_label = ctk.CTkLabel(d2, text=" \r\n Why does Python lives on the land?\r\n \r\n Because it is above C "
                                         "level! \r\n"
                                )
        d2_label.pack()
    if args == "3":
        d3 = ctk.CTkToplevel()
        d3.minsize(height=250, width=500)
        d3.title("03.12")
        d3_label = ctk.CTkLabel(d3, text=" \r\n World shortest LoveStory\r\n \r\n He: You are the ; in my code!! \r\n "
                                         "\r\n She: Sorry! I code in Python! \r\n"
                                )
        d3_label.pack()
    if args == "4":
        d4 = ctk.CTkToplevel()
        d4.minsize(height=250, width=500)
        d4.title("04.12")
        d4_label = ctk.CTkLabel(d4, text=" \r\n 1st rule of programming - You are always in control   \r\n"
                                         "\r\n 2nd rule of programming - Programmers are lazy\r\n "
                                         "\r\n 3nd rule of programming - If it works don't touch it\r\n"
                                )
        d4_label.pack()
    if args == "5":
        d5 = ctk.CTkToplevel()
        d5.minsize(height=250, width=500)
        d5.title("05.12")
        d5_label = ctk.CTkLabel(d5, text="When computer asks: Are you a robot?,    \r\n"
                                         "maybe he just wants to find his family?\r\n "
                                )
        d5_label.pack()
    if args == "6":
        d6 = ctk.CTkToplevel()
        d6.minsize(height=250, width=500)
        d6.title("06.12")
        d6_label = ctk.CTkLabel(d6, text=" \r\nIf you put a million monkeys at a million keyboards, \r\n"
                                         "one of them will eventually write a Java program. \r\n "
                                         "The rest of them will write Python.\r\n "
                                )
        d6_label.pack()
    if args == "7":
        d7 = ctk.CTkToplevel()
        d7.minsize(height=250, width=500)
        d7.title("08.12")
        d7_label = ctk.CTkLabel(d7, text=" \r\nThere are 10 types of people in the world \r\n"
                                         " \r\n Those wo understand binary and those who don't"
                                )
        d7_label.pack()
    if args == "8":
        d8 = ctk.CTkToplevel()
        d8.minsize(height=250, width=500)
        d8.title("08.12")
        d8_label = ctk.CTkLabel(d8, text="['hip', 'hip'] (hip hip array!)")
        d8_label.pack()
    if args == "9":
        d9 = ctk.CTkToplevel()
        d9.minsize(height=250, width=500)
        d9.title("09.12")
        d9_label = ctk.CTkLabel(d9, text=" \r\n What's the object-oriented way to become wealthy? \r\n "
                                         " \r\n Inheritance. \r\n "
                                )
        d9_label.pack()
    if args == "10":
        d10 = ctk.CTkToplevel()
        d10.minsize(height=250, width=500)
        d10.title("10.12")
        d10_label = ctk.CTkLabel(d10, text=" \r\n How do you generate a random string? \r\n "
                                           " \r\n Put a first year Computer Science student in \r\n "
                                           "Vim and ask them to save and exit. \r\n")
        d10_label.pack()
    if args == "11":
        d11 = ctk.CTkToplevel()
        d11.minsize(height=250, width=500)
        d11.title("11.12")
        d11_label = ctk.CTkLabel(d11, text=" \r\n Hardware:  \r\n "
                                           " \r\n The part of a computer that you can kick. \r\n ")
        d11_label.pack()
    if args == "12":
        d12 = ctk.CTkToplevel()
        d12.minsize(height=250, width=500)
        d12.title("21.12")
        d12_label = ctk.CTkLabel(d12, text=" \r\n Schrodinger's attitude to development: \r\n "
                                           " \r\n If I don't look my code,\r\n"
                                           "then there's a chance it looks fine.. \r\n ")
        d12_label.pack()
    if args == "13":
        d13 = ctk.CTkToplevel()
        d13.minsize(height=250, width=500)
        d13.title("13.12")
        d13_label = ctk.CTkLabel(d13, text=" \r\n Why did the programmer quit his job?  \r\n "
                                           " \r\n Because he didn't get arrays. \r\n ")
        d13_label.pack()
    if args == "14":
        d14 = ctk.CTkToplevel()
        d14.minsize(height=250, width=500)
        d14.title("14.12")
        d14_label = ctk.CTkLabel(d14, text=" \r\n How many programmers does it take to change a lightbulb?  \r\n "
                                           " \r\n None, they just make darkness a standard. \r\n ")
        d14_label.pack()
    if args == "15":
        d15 = ctk.CTkToplevel()
        d15.minsize(height=250, width=500)
        d15.title("15.12")
        d15_label = ctk.CTkLabel(d15, text=" \r\n Programming is like sex. \r\n "
                                           " \r\n One mistake and \r\n"
                                           " you have to support it for the rest of your life. \r\n ")
        d15_label.pack()
    if args == "16":
        d16 = ctk.CTkToplevel()
        d16.minsize(height=250, width=500)
        d16.title("16.12")
        d16_label = ctk.CTkLabel(d16, text=" \r\n What did the router say to the doctor?  \r\n "
                                           " \r\n It hurts when IP\r\n ")
        d16_label.pack()
    if args == "17":
        d17 = ctk.CTkToplevel()
        d17.minsize(height=250, width=500)
        d17.title("17.12")
        d17_label = ctk.CTkLabel(17, text=" \r\n Why do Java programmers have to wear glasses? \r\n "
                                          " \r\n Because they don’t C# \r\n ")
        d17_label.pack()
    if args == "18":
        d18 = ctk.CTkToplevel()
        d18.minsize(height=250, width=500)
        d18.title("18.12")
        d18_label = ctk.CTkLabel(d18, text=" \r\n Chuck Norris writes code that optimizes itself.")
        d18_label.pack()
    if args == "19":
        d19 = ctk.CTkToplevel()
        d19.minsize(height=250, width=500)
        d19.title("19.12")
        d19_label = ctk.CTkLabel(d19, text=" \r\n Programmer (noun): A machine that turns coffee into code")
        d19_label.pack()
    if args == "20":
        d20 = ctk.CTkToplevel()
        d20.minsize(height=250, width=500)
        d20.title("20.12")
        d20_label = ctk.CTkLabel(d20, text=" \r\n What’s the difference between an enterprise software "
                                           " \r\nsalesperson and a used car dealer? \r\n "
                                           " \r\n The used car dealer knows when he’s lying.\r\n ")
        d20_label.pack()
    if args == "21":
        d21 = ctk.CTkToplevel()
        d21.minsize(height=250, width=500)
        d21.title("21.12")
        d21_label = ctk.CTkLabel(d21, text=" \r\n Software and cathedrals are much the same -  \r\n "
                                           " \r\n first we build them, then we pray. \r\n ")
        d21_label.pack()
    if args == "22":
        d22 = ctk.CTkToplevel()
        d22.minsize(height=250, width=500)
        d22.title("22.12")
        d22_label = ctk.CTkLabel(d22, text=" \r\n There’s no place like 127.0.0.1.")
        d22_label.pack()
    if args == "23":
        d23 = ctk.CTkToplevel()
        d23.minsize(height=250, width=500)
        d23.title("23.12")
        d23_label = ctk.CTkLabel(d23, text=" \r\n 99 little bugs in the code, \r\n "
                                           " 99 bugs in the code, \r\n "
                                           " 1 bug fixed, compile again,  \r\n "
                                           " 153 little bugs in the code")
        d23_label.pack()
    if args == "24":
        d24 = ctk.CTkToplevel()
        d24.title("24.12")
        d24_title_label = ctk.CTkLabel(
            d24,
            text_font=Ft.h2b,
            text="The Zen of Python \r\n "
        )
        d24_title_label.pack()
        d24_label = ctk.CTkLabel(
            d24,
            text_font=Ft.txt,
            text="Beautiful is better than ugly.\r\n"
                 "Explicit is better than implicit.\r\n"
                 "Simple is better than complex.\r\n"
                 "Complex is better than complicated.\r\n"
                 "Flat is better than nested. \r\n"
                 "Sparse is better than dense. \r\n"
                 "Readability counts. \r\n"
                 "Special cases aren't special enough to break the rules. \r\n"
                 "Although practicality beats purity. \r\n"
                 "Errors should never pass silently. \r\n"
                 "Unless explicitly silenced. \r\n"
                 "In the face of ambiguity, refuse the temptation to guess. \r\n"
                 "There should be one-- and preferably only one --obvious way to do it. \r\n"
                 "Although that way may not be obvious at first unless you're Dutch. \r\n"
                 "Now is better than never. \r\n"
                 "Although never is often better than *right* now. \r\n"
                 "If the implementation is hard to explain, it's a bad idea.\r\n"
                 "If the implementation is easy to explain, it may be a good idea.\r\n"
                 "Namespaces are one honking great idea -- let's do more of those! \r\n"
                 " \r\n \r\n \r\n Happy Holidays to You :)"

        )
        d24_label.pack()


def alphabet(main_frame):
    calendar = ctk.CTkFrame(
        master=main_frame,
        width=1080,
        height=720,

    )
    calendar.grid(
        row=0,
        column=0
    )

    btn_1 = ctk.CTkButton(calendar, text="1", width=180, height=180, border_width=2, command=lambda: button_click("1"))
    btn_2 = ctk.CTkButton(calendar, text="2", width=180, height=180, border_width=2, command=lambda: button_click("2"))
    btn_3 = ctk.CTkButton(calendar, text="3", width=180, height=180, border_width=2, command=lambda: button_click("3"))
    btn_4 = ctk.CTkButton(calendar, text="4", width=180, height=180, border_width=2, command=lambda: button_click("4"))
    btn_5 = ctk.CTkButton(calendar, text="5", width=180, height=180, border_width=2, command=lambda: button_click("5"))
    btn_6 = ctk.CTkButton(calendar, text="6", width=180, height=180, border_width=2, command=lambda: button_click("6"))
    btn_7 = ctk.CTkButton(calendar, text="7", width=180, height=180, border_width=2, command=lambda: button_click("7"))
    btn_8 = ctk.CTkButton(calendar, text="8", width=180, height=180, border_width=2, command=lambda: button_click("8"))
    btn_9 = ctk.CTkButton(calendar, text="9", width=180, height=180, border_width=2, command=lambda: button_click("9"))
    btn_10 = ctk.CTkButton(calendar, text="10", width=180, height=180, border_width=2,
                           command=lambda: button_click("10"))
    btn_11 = ctk.CTkButton(calendar, text="11", width=180, height=180, border_width=2,
                           command=lambda: button_click("11"))
    btn_12 = ctk.CTkButton(calendar, text="12", width=180, height=180, border_width=2,
                           command=lambda: button_click("12"))
    btn_13 = ctk.CTkButton(calendar, text="13", width=180, height=180, border_width=2,
                           command=lambda: button_click("13"))
    btn_14 = ctk.CTkButton(calendar, text="14", width=180, height=180, border_width=2,
                           command=lambda: button_click("14"))
    btn_15 = ctk.CTkButton(calendar, text="15", width=180, height=180, border_width=2,
                           command=lambda: button_click("15"))
    btn_16 = ctk.CTkButton(calendar, text="16", width=180, height=180, border_width=2,
                           command=lambda: button_click("16"))
    btn_17 = ctk.CTkButton(calendar, text="17", width=180, height=180, border_width=2,
                           command=lambda: button_click("17"))
    btn_18 = ctk.CTkButton(calendar, text="18", width=180, height=180, border_width=2,
                           command=lambda: button_click("18"))
    btn_19 = ctk.CTkButton(calendar, text="19", width=180, height=180, border_width=2,
                           command=lambda: button_click("19"))
    btn_20 = ctk.CTkButton(calendar, text="20", width=180, height=180, border_width=2,
                           command=lambda: button_click("20"))
    btn_21 = ctk.CTkButton(calendar, text="21", width=180, height=180, border_width=2,
                           command=lambda: button_click("21"))
    btn_22 = ctk.CTkButton(calendar, text="22", width=180, height=180, border_width=2,
                           command=lambda: button_click("22"))
    btn_23 = ctk.CTkButton(calendar, text="23", width=180, height=180, border_width=2,
                           command=lambda: button_click("23"))
    btn_24 = ctk.CTkButton(calendar, text="24", width=180, height=180, border_width=2,
                           command=lambda: button_click("24"))

    # Buttons grid

    btn_1.grid(row=0, column=1)
    btn_2.grid(row=1, column=5)
    btn_3.grid(row=3, column=0)
    btn_4.grid(row=0, column=3)
    btn_5.grid(row=3, column=2)
    btn_6.grid(row=2, column=4)
    btn_7.grid(row=0, column=0)
    btn_8.grid(row=1, column=3)
    btn_9.grid(row=2, column=1)
    btn_10.grid(row=0, column=5)
    btn_11.grid(row=1, column=4)
    btn_12.grid(row=2, column=2)
    btn_13.grid(row=3, column=3)
    btn_14.grid(row=0, column=2)
    btn_15.grid(row=3, column=5)
    btn_16.grid(row=2, column=0)
    btn_17.grid(row=1, column=2)
    btn_18.grid(row=3, column=4)
    btn_19.grid(row=1, column=0)
    btn_20.grid(row=2, column=3)
    btn_21.grid(row=1, column=1)
    btn_22.grid(row=3, column=1)
    btn_23.grid(row=0, column=4)
    btn_24.grid(row=2, column=5)
