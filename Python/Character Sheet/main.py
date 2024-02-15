import tkinter as tk
import customtkinter as ctk
from tkinter import *
import sqlite3
from functions import *


ctk.set_appearance_mode("Dark")

def main():
    # Create a new Tkinter window
    root = ctk.CTk()
    root.title("My Application")
    root.minsize(width=1600, height=1000)

    tabs = ctk.CTkTabview(root, width=1550, height=950, corner_radius=20, fg_color="#383838")
    tabs.pack()



#--------------------FUNCTIONS
    



#-------------------VARIABLES
    names = ["Test 1", "Test 2"]
    classes = ["Test 1", "Test 2"]
    subclasses = ["Test 1", "Test 2"]
    backgrounds = ["Test 1", "Test 2"]
    races = ["Test 1", "Test 2"]
    

    
#---------------------TABS
    tab1 = tabs.add("Main")
    tab2 = tabs.add("Inventory")




#--------------------TAB 1 FRAMES
    name_frame1 = ctk.CTkFrame(tab1, width=300, height=75, corner_radius=20)
    name_frame1.place(x=10, y=10)

    options_frame1 = ctk.CTkFrame(tab1, width=450, height=75, corner_radius=20)
    options_frame1.place(x=320, y=10)

    details_frame1 = ctk.CTkFrame(tab1, width=720, height=75, corner_radius=20)
    details_frame1.place(x=780, y=10)

    level_frame = ctk.CTkFrame(tab1, width=1490, height=17, corner_radius=20)
    level_frame.place(x=10, y=90)







#--------------------TAB 2 FRAMES
    name_frame2 = ctk.CTkFrame(tab2, width=300, height=75, corner_radius=20)
    name_frame2.place(x=10, y=10)

    options_frame2 = ctk.CTkFrame(tab2, width=450, height=75, corner_radius=20)
    options_frame2.place(x=320, y=10)

    details_frame2 = ctk.CTkFrame(tab2, width=720, height=75, corner_radius=20)
    details_frame2.place(x=780, y=10)

#-------------------NAME FRAME
    character_name_label = ctk.CTkLabel(name_frame1, text="CHARACTER:", fg_color="#1f6aa5", corner_radius=20)
    character_name_label.place(x=100, y=5)

    name_box = ctk.CTkComboBox(name_frame1, values= names, state="readonly", width=280)
    name_box.place(x=10, y=35)
    #--------------------------------------------------------------TAB 2
    character_name_label = ctk.CTkLabel(name_frame2, text="CHARACTER:", fg_color="#1f6aa5", corner_radius=20)
    character_name_label.place(x=100, y=5)

    name_box = ctk.CTkComboBox(name_frame2, values= names, state="readonly", width=280)
    name_box.place(x=10, y=35)

#-------------------DETAILS FRAME
    class_name_label = ctk.CTkLabel(details_frame1, text="CLASS:", fg_color="#1f6aa5", corner_radius=20)
    class_name_label.place(x=5, y=5)

    class_listbox = ctk.CTkComboBox(details_frame1, values= classes, state="readonly", width=175)
    class_listbox.place(x=80, y=5)
    #------
    subclass_name_label = ctk.CTkLabel(details_frame1, text="SUBCLASS:", fg_color="#1f6aa5", corner_radius=20)
    subclass_name_label.place(x=5, y=40)

    subclass_listbox = ctk.CTkComboBox(details_frame1, values= subclasses, state="readonly", width=150)
    subclass_listbox.place(x=105, y=40)
    #-------
    background_name_label = ctk.CTkLabel(details_frame1, text="BACKGROUND:", fg_color="#1f6aa5", corner_radius=20)
    background_name_label.place(x=260, y=5)

    background_listbox = ctk.CTkComboBox(details_frame1, values= backgrounds, state="readonly", width=150)
    background_listbox.place(x=380, y=5)
    #--------
    race_name_label = ctk.CTkLabel(details_frame1, text="RACE:", fg_color="#1f6aa5", corner_radius=20)
    race_name_label.place(x=260, y=40)

    race_listbox = ctk.CTkComboBox(details_frame1, values= races, state="readonly", width=202)
    race_listbox.place(x=328, y=40)
    #------
    level_label = ctk.CTkLabel(details_frame1, text="LEVEL:", fg_color="#1f6aa5", corner_radius=20)
    level_label.place(x=535, y=5)

    level_spinbox = IntSpinbox(details_frame1, width=100, step_size=1)
    level_spinbox.place(x=607, y=5)
    level_spinbox.set(0)
    #------
    exp_label = ctk.CTkLabel(details_frame1, text="EXP:", fg_color="#1f6aa5", corner_radius=20)
    exp_label.place(x=535, y=40)

    exp_total = ctk.CTkEntry(details_frame1, fg_color="#343638", corner_radius=20, width=115)
    exp_total.place(x=595, y=40)
    #-------


#------------------------LEVEL FRAME    
    level_prgress_bar = ctk.CTkProgressBar(level_frame, width=1470, progress_color="#9B902B")
    level_prgress_bar.place(x=10, y=4)





    #----------------------------------------------------------------- TAB 2
    class_name_label2 = ctk.CTkLabel(details_frame2, text="CLASS:", fg_color="#1f6aa5", corner_radius=20)
    class_name_label2.place(x=5, y=5)

    class_listbox2 = ctk.CTkComboBox(details_frame2, values= classes, state="readonly", width=175)
    class_listbox2.place(x=80, y=5)
    #------
    subclass_name_label2 = ctk.CTkLabel(details_frame2, text="SUBCLASS:", fg_color="#1f6aa5", corner_radius=20)
    subclass_name_label2.place(x=5, y=40)

    subclass_listbox2 = ctk.CTkComboBox(details_frame2, values= subclasses, state="readonly", width=150)
    subclass_listbox2.place(x=105, y=40)
    #------
    background_name_label2 = ctk.CTkLabel(details_frame2, text="BACKGROUND:", fg_color="#1f6aa5", corner_radius=20)
    background_name_label2.place(x=260, y=5)

    background_listbox2 = ctk.CTkComboBox(details_frame2, values= backgrounds, state="readonly", width=150)
    background_listbox2.place(x=380, y=5)
    #--------
    race_name_label2 = ctk.CTkLabel(details_frame2, text="RACE:", fg_color="#1f6aa5", corner_radius=20)
    race_name_label2.place(x=260, y=40)

    race_listbox2 = ctk.CTkComboBox(details_frame2, values= races, state="readonly", width=202)
    race_listbox2.place(x=328, y=40)
    #------
    level_label2 = ctk.CTkLabel(details_frame2, text="LEVEL:", fg_color="#1f6aa5", corner_radius=20)
    level_label2.place(x=535, y=5)

    level_spinbox2 = IntSpinbox(details_frame2, width=100, step_size=1)
    level_spinbox2.place(x=607, y=5)
    level_spinbox2.set(0)
    #------
    exp_label2 = ctk.CTkLabel(details_frame2, text="EXP:", fg_color="#1f6aa5", corner_radius=20)
    exp_label2.place(x=535, y=40)

    exp_total2 = ctk.CTkEntry(details_frame2, fg_color="#343638", corner_radius=20, width=115)
    exp_total2.place(x=595, y=40)
    #-------


    root.mainloop()

if __name__ == "__main__":
    main()