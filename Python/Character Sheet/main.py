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
    name_box = ctk.CTkComboBox(name_frame1, values= names, state="readonly", width=280)
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
    #--------ACROBATICS
    acrobatics_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    acrobatics_checkbox.configure(fg_color ="#343638")
    acrobatics_checkbox.place(x=0, y=0)
    acrobatics_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    acrobatics_text.place(x=30, y=0)
    acrobatics_button = ctk.CTkButton(skills_tab_frame, text="Acrobatics", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    acrobatics_button.place(x=55, y=0)
    #--------ANIMAL HANDLING
    animal_handling_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    animal_handling_checkbox.configure(fg_color ="#343638")
    animal_handling_checkbox.place(x=0, y=30)
    animal_handling_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    animal_handling_text.place(x=30, y=30)
    animal_handling_button = ctk.CTkButton(skills_tab_frame, text="Animal Handling", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    animal_handling_button.place(x=55, y=30)
    #--------ARCANA
    arcana_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    arcana_checkbox.configure(fg_color ="#343638")
    arcana_checkbox.place(x=0, y=60)
    arcana_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    arcana_text.place(x=30, y=60)
    arcana_button = ctk.CTkButton(skills_tab_frame, text="Arcana", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    arcana_button.place(x=55, y=60)
    #--------ATHLETICS
    athletics_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    athletics_checkbox.configure(fg_color ="#343638")
    athletics_checkbox.place(x=0, y=90)
    athletics_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    athletics_text.place(x=30, y=90)
    athletics_button = ctk.CTkButton(skills_tab_frame, text="Athletics", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    athletics_button.place(x=55, y=90)
    #--------DECEPTION
    deception_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    deception_checkbox.configure(fg_color ="#343638")
    deception_checkbox.place(x=0, y=120)
    deception_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    deception_text.place(x=30, y=120)
    deception_button = ctk.CTkButton(skills_tab_frame, text="Deception", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    deception_button.place(x=55, y=120)
    #--------HISTORY
    history_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    history_checkbox.configure(fg_color ="#343638")
    history_checkbox.place(x=0, y=150)
    history_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    history_text.place(x=30, y=150)
    history_button = ctk.CTkButton(skills_tab_frame, text="History", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    history_button.place(x=55, y=150)
    #--------INSIGHT
    insight_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    insight_checkbox.configure(fg_color ="#343638")
    insight_checkbox.place(x=0, y=180)
    insight_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    insight_text.place(x=30, y=180)
    insight_button = ctk.CTkButton(skills_tab_frame, text="Insight", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    insight_button.place(x=55, y=180)
    #--------INTIMIDATION
    intimidation_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    intimidation_checkbox.configure(fg_color ="#343638")
    intimidation_checkbox.place(x=0, y=210)
    intimidation_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    intimidation_text.place(x=30, y=210)
    intimidation_button = ctk.CTkButton(skills_tab_frame, text="Intimidation", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    intimidation_button.place(x=55, y=210)
    #--------INVESTIGATION
    investigation_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    investigation_checkbox.configure(fg_color ="#343638")
    investigation_checkbox.place(x=0, y=240)
    investigation_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    investigation_text.place(x=30, y=240)
    investigation_button = ctk.CTkButton(skills_tab_frame, text="Investigation", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    investigation_button.place(x=55, y=240)
    #--------MEDICINE
    medicine_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    medicine_checkbox.configure(fg_color ="#343638")
    medicine_checkbox.place(x=0, y=270)
    medicine_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    medicine_text.place(x=30, y=270)
    medicine_button = ctk.CTkButton(skills_tab_frame, text="Medicine", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    medicine_button.place(x=55, y=270)
    #--------NATURE
    nature_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    nature_checkbox.configure(fg_color ="#343638")
    nature_checkbox.place(x=0, y=300)
    nature_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    nature_text.place(x=30, y=300)
    nature_button = ctk.CTkButton(skills_tab_frame, text="Nature", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    nature_button.place(x=55, y=300)
    #--------PERCEPTION
    perception_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    perception_checkbox.configure(fg_color ="#343638")
    perception_checkbox.place(x=0, y=330)
    perception_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    perception_text.place(x=30, y=330)
    perception_button = ctk.CTkButton(skills_tab_frame, text="Perception", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    perception_button.place(x=55, y=330)
    #--------PERFORMANCE
    performance_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    performance_checkbox.configure(fg_color ="#343638")
    performance_checkbox.place(x=0, y=360)
    performance_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    performance_text.place(x=30, y=360)
    performance_button = ctk.CTkButton(skills_tab_frame, text="Performance", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    performance_button.place(x=55, y=360)
    #--------PERSUASION
    persuasion_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    persuasion_checkbox.configure(fg_color ="#343638")
    persuasion_checkbox.place(x=0, y=390)
    persuasion_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    persuasion_text.place(x=30, y=390)
    persuasion_button = ctk.CTkButton(skills_tab_frame, text="Persuasion", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    persuasion_button.place(x=55, y=390)
    #--------RELIGION
    religion_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    religion_checkbox.configure(fg_color ="#343638")
    religion_checkbox.place(x=0, y=420)
    religion_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    religion_text.place(x=30, y=420)
    religion_button = ctk.CTkButton(skills_tab_frame, text="Religion", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    religion_button.place(x=55, y=420)
    #--------SLEIGHT OF HAND
    sleight_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    sleight_checkbox.configure(fg_color ="#343638")
    sleight_checkbox.place(x=0, y=450)
    sleight_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    sleight_text.place(x=30, y=450)
    sleight_button = ctk.CTkButton(skills_tab_frame, text="Sleight of Hand", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    sleight_button.place(x=55, y=450)
    #--------STEALTH
    stealth_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    stealth_checkbox.configure(fg_color ="#343638")
    stealth_checkbox.place(x=0, y=480)
    stealth_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    stealth_text.place(x=30, y=480)
    stealth_button = ctk.CTkButton(skills_tab_frame, text="Stealth", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    stealth_button.place(x=55, y=480)
    #--------SURVIVAL
    survival_checkbox = TristateCheckbox(skills_tab_frame, height=25, width=25, border_width=3)
    survival_checkbox.configure(fg_color ="#343638")
    survival_checkbox.place(x=0, y=510)
    survival_text = CTkLabel(skills_tab_frame, text="  __  ", font=("Arial", 15))
    survival_text.place(x=30, y=510)
    survival_button = ctk.CTkButton(skills_tab_frame, text="Survival", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    survival_button.place(x=55, y=510)
#---------------------------SAVING THROW FRAME
    savethrow_tab = skills_frame.add("SAVES")
    savethrow_tab_frame = ctk.CTkFrame(savethrow_tab, width=220, height=400, corner_radius=20)
    savethrow_tab_frame.place(x=0, y=0)
    #--------STR
    strsave_radio = ctk.CTkRadioButton(savethrow_tab_frame, radiobutton_width=20, radiobutton_height=20, font=("Arial", 15))
    strsave_radio.configure(text="  __  ")
    strsave_radio.place(x=0, y=0)
    strsave_button = ctk.CTkButton(savethrow_tab_frame, text="Strength", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    strsave_button.place(x=52, y=0)
    #--------DEX
    dexsave_radio = ctk.CTkRadioButton(savethrow_tab_frame, radiobutton_width=20, radiobutton_height=20, font=("Arial", 15))
    dexsave_radio.configure(text="  __  ")
    dexsave_radio.place(x=0, y=30)
    dexsave_button = ctk.CTkButton(savethrow_tab_frame, text="Dexterity", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    dexsave_button.place(x=52, y=30)
    #--------CON
    consave_radio = ctk.CTkRadioButton(savethrow_tab_frame, radiobutton_width=20, radiobutton_height=20, font=("Arial", 15))
    consave_radio.configure(text="  __  ")
    consave_radio.place(x=0, y=60)
    consave_button = ctk.CTkButton(savethrow_tab_frame, text="Constitution", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    consave_button.place(x=52, y=60)
    #--------INT
    intsave_radio = ctk.CTkRadioButton(savethrow_tab_frame, radiobutton_width=20, radiobutton_height=20, font=("Arial", 15))
    intsave_radio.configure(text="  __  ")
    intsave_radio.place(x=0, y=90)
    intsave_button = ctk.CTkButton(savethrow_tab_frame, text="Intelligence", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    intsave_button.place(x=52, y=90)
    #--------WIS
    wissave_radio = ctk.CTkRadioButton(savethrow_tab_frame, radiobutton_width=20, radiobutton_height=20, font=("Arial", 15))
    wissave_radio.configure(text="  __  ")
    wissave_radio.place(x=0, y=120)
    wissave_button = ctk.CTkButton(savethrow_tab_frame, text="Wisdom", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    wissave_button.place(x=52, y=120)
    #--------CHA
    chasave_radio = ctk.CTkRadioButton(savethrow_tab_frame, radiobutton_width=20, radiobutton_height=20, font=("Arial", 15))
    chasave_radio.configure(text="  __  ")
    chasave_radio.place(x=0, y=150)
    chasave_button = ctk.CTkButton(savethrow_tab_frame, text="Charisma", border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
    chasave_button.place(x=52, y=150)








    root.mainloop()

if __name__ == "__main__":
    main()