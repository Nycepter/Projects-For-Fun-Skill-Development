import tkinter as tk
import customtkinter as ctk
from tkinter import *
import sqlite3
from functions import * 
from CTkTable import *


ctk.set_appearance_mode("Dark")

def main():
    # Create a new Tkinter window
    root = ctk.CTk()
    root.title("Nycepter's Character Manager")
    root.minsize(width=1600, height=1000)
    

    tabs = ctk.CTkTabview(root, width=1550, height=980, corner_radius=20, fg_color="#383838")
    tabs.pack()

    conn = sqlite3.connect('characters.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS characters
                (name text)''')
    c.execute("SELECT name FROM characters")
    c.execute('''CREATE TABLE IF NOT EXISTS last_selected_character
            (name text)''')
    names = [row[0] for row in c.fetchall()]
    names.append("New Character")

#--------------------FUNCTIONS
    def on_name_selected(event):
    # This function is called when a name is selected from the combobox
        selected_name = name_box.get()
        if selected_name == "New Character":
            name_box.set("")
            name_box.configure(state="normal")
            name_box.focus_set()
        else:
            conn = sqlite3.connect('characters.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS characters
                    (name text)''')
        c.execute("SELECT name FROM characters")
        names = [row[0] for row in c.fetchall()]
        names.append("New Character")
        name_box.configure(values=names)


    def on_enter_pressed(event):
        # This function is called when the Enter key is pressed
        new_name = name_box.get()
        if new_name and new_name != "New Character":
            # Insert the new name into the database
            c.execute("INSERT INTO characters VALUES (?)", (new_name,))
            conn.commit()
            # Add the new name to the combobox
            names.append(new_name)
            name_box['values'] = names  # Update the values of the combobox
            name_box.configure(state="readonly")   
    



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
    #-----NAME
    name_frame1 = ctk.CTkFrame(tab1, width=300, height=75, corner_radius=20)
    name_frame1.place(x=10, y=10)
    #-----OPTIONS
    options_frame1 = ctk.CTkFrame(tab1, width=450, height=75, corner_radius=20)
    options_frame1.place(x=320, y=10)
    #-----DETAILS
    details_frame1 = ctk.CTkFrame(tab1, width=720, height=75, corner_radius=20)
    details_frame1.place(x=780, y=10)
    #-----LEVEL
    level_frame = ctk.CTkFrame(tab1, width=1490, height=17, corner_radius=20)
    level_frame.place(x=10, y=90)
    #-----STR
    str_frame = MyCTkTabview(tab1, width=60, height=100, corner_radius=20, fg_color="#2b2b2b")
    str_frame.place(x=10, y=112)
    #-----DEX
    dex_frame = MyCTkTabview(tab1, width=60, height=100, corner_radius=20, fg_color="#2b2b2b")
    dex_frame.place(x=10, y=212)
    #-----CON
    con_frame = MyCTkTabview(tab1, width=60, height=100, corner_radius=20, fg_color="#2b2b2b")
    con_frame.place(x=10, y=312)
    #-----INT
    int_frame = MyCTkTabview(tab1, width=60, height=100, corner_radius=20, fg_color="#2b2b2b")
    int_frame.place(x=10, y=412)
    #-----WIS
    wis_frame = MyCTkTabview(tab1, width=60, height=100, corner_radius=20, fg_color="#2b2b2b")
    wis_frame.place(x=10, y=512)
    #-----CHA
    cha_frame = MyCTkTabview(tab1, width=60, height=100, corner_radius=20, fg_color="#2b2b2b")
    cha_frame.place(x=10, y=612)
    #-----SAVING THROW
    # savethrow_frame = ctk.CTkTabview(tab1, width=220, height=250, corner_radius=20, fg_color="#2b2b2b", state="active")
    # savethrow_frame.place(x=330, y=112)
    #-----SKILLS
    skills_frame = ctk.CTkTabview(tab1, width=220, height=610, corner_radius=20, fg_color="#2b2b2b")
    skills_frame.place(x=90, y=112)

    








#--------------------TAB 2 FRAMES
    #------NAME
    name_frame2 = ctk.CTkFrame(tab2, width=300, height=75, corner_radius=20)
    name_frame2.place(x=10, y=10)
    #-----OPTIONS
    options_frame2 = ctk.CTkFrame(tab2, width=450, height=75, corner_radius=20)
    options_frame2.place(x=320, y=10)
    #------DETAILS
    details_frame2 = ctk.CTkFrame(tab2, width=720, height=75, corner_radius=20)
    details_frame2.place(x=780, y=10)

#-------------------NAME FRAME
    character_name_label = ctk.CTkLabel(name_frame1, text="CHARACTER:", fg_color="#1f6aa5", corner_radius=20)
    character_name_label.place(x=100, y=5)
    name_box = ctk.CTkComboBox(name_frame1, values= names, width=280, state="readonly", command=on_name_selected)
    name_box.bind('<Return>', on_enter_pressed)
    name_box.place(x=10, y=35)
    #--------------------------------------------------------------TAB 2
    character_name_label2 = ctk.CTkLabel(name_frame2, text="CHARACTER:", fg_color="#1f6aa5", corner_radius=20)
    character_name_label2.place(x=100, y=5)
    name_box2 = ctk.CTkComboBox(name_frame2, values= names, state="readonly", width=280)
    name_box2.place(x=10, y=35)

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


#------------------------LEVEL FRAME    
    level_prgress_bar = ctk.CTkProgressBar(level_frame, width=1470, progress_color="#9B902B", corner_radius=20)
    level_prgress_bar.place(x=10, y=4)
    level_prgress_bar.set(0)

#-------------------------STATS FRAME
    #--------STR
    str_tab = str_frame.add("STR:")
    str_frame._segmented_button.configure(corner_radius=10)
    str_tab_frame = ctk.CTkFrame(str_tab, width=60, height=100, corner_radius=20)
    str_tab_frame.place(x=0, y=0)
    str_mod = ctk.CTkLabel(str_tab_frame, text="+2", corner_radius=20, height=8, width=8, font=("Arial", 25))
    str_mod.place(x=0, y=0)
    str_total = ctk.CTkEntry(str_frame, width=40, height=15, corner_radius=20, border_width=1)
    str_total.place(x=10, y=70)
    #--------DEX
    dex_tab = dex_frame.add("DEX:")
    dex_frame._segmented_button.configure(corner_radius=10)
    dex_tab_frame = ctk.CTkFrame(dex_tab, width=60, height=100, corner_radius=20)
    dex_tab_frame.place(x=0, y=0)
    dex_mod = ctk.CTkLabel(dex_tab_frame, text="+2", corner_radius=20, height=8, width=8, font=("Arial", 25))
    dex_mod.place(x=0, y=0)
    dex_total = ctk.CTkEntry(dex_frame, width=40, height=15, corner_radius=20, border_width=1)
    dex_total.place(x=10, y=70)
    #--------CON
    con_tab = con_frame.add("CON:")
    con_frame._segmented_button.configure(corner_radius=10)
    con_tab_frame = ctk.CTkFrame(con_tab, width=60, height=100, corner_radius=20)
    con_tab_frame.place(x=0, y=0)
    con_mod = ctk.CTkLabel(con_tab_frame, text="+2", corner_radius=20, height=8, width=8, font=("Arial", 25))
    con_mod.place(x=0, y=0)
    con_total = ctk.CTkEntry(con_frame, width=40, height=15, corner_radius=20, border_width=1)
    con_total.place(x=10, y=70)
    #--------INT
    int_tab = int_frame.add("INT:")
    int_frame._segmented_button.configure(corner_radius=10)
    int_tab_frame = ctk.CTkFrame(int_tab, width=60, height=100, corner_radius=20)
    int_tab_frame.place(x=0, y=0)
    int_mod = ctk.CTkLabel(int_tab_frame, text="+2", corner_radius=20, height=8, width=8, font=("Arial", 25))
    int_mod.place(x=0, y=0)
    int_total = ctk.CTkEntry(int_frame, width=40, height=15, corner_radius=20, border_width=1)
    int_total.place(x=10, y=70)
    #--------WIS
    wis_tab = wis_frame.add("WIS:")
    wis_frame._segmented_button.configure(corner_radius=10)
    wis_tab_frame = ctk.CTkFrame(wis_tab, width=60, height=100, corner_radius=20)
    wis_tab_frame.place(x=0, y=0)
    wis_mod = ctk.CTkLabel(wis_tab_frame, text="+2", corner_radius=20, height=8, width=8, font=("Arial", 25))
    wis_mod.place(x=0, y=0)
    wis_total = ctk.CTkEntry(wis_frame, width=40, height=15, corner_radius=20, border_width=1)
    wis_total.place(x=10, y=70)
    #--------CHA
    cha_tab = cha_frame.add("CHA:")
    cha_frame._segmented_button.configure(corner_radius=10)
    cha_tab_frame = ctk.CTkFrame(cha_tab, width=60, height=100, corner_radius=20)
    cha_tab_frame.place(x=0, y=0)
    cha_mod = ctk.CTkLabel(cha_tab_frame, text="+2", corner_radius=20, height=8, width=8, font=("Arial", 25))
    cha_mod.place(x=0, y=0)
    cha_total = ctk.CTkEntry(cha_frame, width=40, height=15, corner_radius=20, border_width=1)
    cha_total.place(x=10, y=70)


#---------------------------SKILLS FRAME
    skills_tab = skills_frame.add("SKILLS")
    skills_frame._segmented_button.configure(corner_radius=20)
    skills_tab_frame = ctk.CTkFrame(skills_tab, width=220, height=610, corner_radius=20)
    skills_tab_frame.place(x=0, y=0)

    skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]

    for i, skill in enumerate(skills):
        Skill(skills_tab_frame, skill, i * 30)
#---------------------------SAVING THROW FRAME
    savethrow_tab = skills_frame.add("SAVES")
    savethrow_tab_frame = ctk.CTkFrame(savethrow_tab, width=220, height=400, corner_radius=20)
    savethrow_tab_frame.place(x=0, y=0)

    attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
   
    for i, attr in enumerate(attributes):
        SaveThrow(savethrow_tab_frame, attr, 0, i*30)







    root.mainloop()

if __name__ == "__main__":
    main()