import tkinter as tk
import customtkinter as ctk
from tkinter import *
import sqlite3
from functions import *
from CTkTable import *
import tkinter.simpledialog as simpledialog

import json
import os


ctk.set_appearance_mode("Dark")

def load_data():
    if os.path.exists('characters.json'):
        with open('characters.json', 'r') as f:
            return json.load(f)
    else:
        return {"characters": [], "last_selected_character": ""}
    
def save_data(data):
    with open('characters.json', 'w') as f:
        json.dump(data, f)





def main():
    # Create a new Tkinter window
    root = ctk.CTk()
    root.title("Nycepter's Character Manager")
    root.minsize(width=1600, height=1000)

    

    tabs = ctk.CTkTabview(root, width=1550, height=980, corner_radius=20, fg_color="#383838")
    tabs.pack()

    # Load data from JSON file
    data = load_data()
    names = [character['name'] for character in data["characters"]]
    names.append("New Character")
    last_selected_name = data["last_selected_character"]
    print(last_selected_name)
    print(data)
    
    def unfocus_all(event):
        if event.widget == root or event.widget.master in [tab1, tab2]:
            root.focus_set()

    root.bind('<1>', unfocus_all)
        




#--------------------FUNCTIONS
    def load_character():
        if not os.path.exists('characters.json'):
            # If it doesn't exist, create it
            with open('characters.json', 'w') as f:
                f.write('{"characters": [], "last_selected_character": ""}')

        # Now you can open the file
        with open('characters.json', 'r') as f:
            data = json.load(f)

        # Get the name of the last selected character
        last_selected_name = data['last_selected_character']

        # Find the dictionary for the last selected character
        for character in data['characters']:
            if character['name'] == last_selected_name:
                # Get the background value
                background_listbox.set(character['background'])
                background_listbox2.set(character['background'])
                for key in attribute_objects:
                    # Get the value for this key, if it exists
                    value = character.get(key, '')
                    # Delete existing content in the corresponding Attribute object
                    attribute_objects[key].total.delete(0, 'end')
                    # If a value exists, insert it into the Attribute object
                    if value:
                        attribute_objects[key].total.insert(0, value)

                break


    


    def set_selected_character(namebox, selected_name):
        data = load_data()
        if selected_name == "New Character":
            namebox.set("")
            namebox.configure(state="normal")
            namebox.focus_set()
        else:
            data["last_selected_character"] = selected_name
            save_data(data)
            data = load_data()
            names = [character['name'] for character in data["characters"]]
            names.append("New Character")
            name_box.configure(values=names)
            name_box2.configure(values=names)
            load_character()
            
            

    def on_name_selected_tab1(event):
        selected_name = name_box.get()
        set_selected_character(name_box, selected_name)
        name_box2.set(selected_name)
        load_character()
          
        # Set the selected character in the combobox on tab2

    def on_name_selected_tab2(event):
        selected_name = name_box2.get()
        set_selected_character(name_box2, selected_name)
        name_box.set(selected_name)
        load_character()
        
          # Set the selected character in the combobox on tab1

    def on_enter_pressed(name_box):
        new_name = name_box.get()
        if new_name and new_name != "New Character":
            data = load_data()
            # Create a dictionary for the new character
            new_character = {'name': new_name, 'background': ''}
            # Append the dictionary to the characters list
            data["characters"].append(new_character)
            data["last_selected_character"] = new_name
            save_data(data)
            data = load_data()
            names = [character['name'] for character in data["characters"]]
            names.append("New Character")
            name_box['values'] = names
            name_box.configure(state="readonly")
            name_box2['values'] = names
            name_box2.configure(state="readonly")

    def new_name_tab1(event):
        new_name = name_box.get()
        on_enter_pressed(name_box)
        name_box2.set(new_name)  # Set the selected character in the combobox on tab2

    def new_name_tab2(event):
        new_name = name_box2.get()
        on_enter_pressed(name_box2)
        name_box.set(new_name)  # Set the selected character in the combobox on tab1

    def set_background(bg):
        data = load_data()
        last_selected_name = data['last_selected_character']

        # Find the dictionary for the last selected character
        for character in data['characters']:
            if character['name'] == last_selected_name:
                # Set the background
                character['background'] = bg
                break

        save_data(data)

    


        
    



#-------------------VARIABLES

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
    #------SKILLS/SAVE
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
    name_box = ctk.CTkComboBox(name_frame1, values= names, width=280, state="readonly", command=on_name_selected_tab1)
    if last_selected_name is not None:
        name_box.set(last_selected_name)
    name_box.bind('<Return>', new_name_tab1)
    name_box.bind('<FocusOut>', new_name_tab1)
    name_box.place(x=10, y=35)
    #--------------------------------------------------------------TAB 2
    character_name_label2 = ctk.CTkLabel(name_frame2, text="CHARACTER:", fg_color="#1f6aa5", corner_radius=20)
    character_name_label2.place(x=100, y=5)
    name_box2 = ctk.CTkComboBox(name_frame2, values= names, width=280, state="readonly", command=on_name_selected_tab2)
    if last_selected_name is not None:
        name_box2.set(last_selected_name)
    name_box2.bind('<Return>', new_name_tab2)
    name_box2.bind('<FocusOut>', new_name_tab2)
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
    background_listbox = ctk.CTkComboBox(details_frame1, values= backgrounds, state="readonly", width=150, command=set_background)
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
    attributes = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    x = 10
    y = 110
    attribute_objects = {}  # Create an empty dictionary
    for attribute in attributes:
        attribute_objects[attribute] = Attribute(tab1, attribute, x, y)
        y += 112  # Adjust as needed
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


    

#---------------------------changes
        
    load_character()
    

    

    root.mainloop()

if __name__ == "__main__":
    main()