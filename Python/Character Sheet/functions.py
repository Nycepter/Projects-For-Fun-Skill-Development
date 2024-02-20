import customtkinter as ctk
from customtkinter import *
from typing import Union, Tuple, Dict, List, Callable, Optional, Any
import tkinter as tk
import json
import math
from typing import Tuple, Dict, Callable, List
try:
    from PIL import Image, ImageTk, ImageChops
except ImportError:
    pass







from PIL import Image, ImageDraw, ImageOps

def add_rounded_corners(image, radius):
    """Add rounded corners to an image."""
    image = image.convert("RGBA")
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    w, h = image.size
    alpha = Image.new('L', image.size, 255)
    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
    # Combine the new alpha channel with the original alpha channel
    alpha = ImageChops.multiply(alpha, image.split()[3])
    image.putalpha(alpha)
    return image


def load_data():
    if os.path.exists('characters.json'):
        with open('characters.json', 'r') as f:
            return json.load(f)
    else:
        return {"characters": [], "last_selected_character": ""}
    
def save_data(data):
    with open('characters.json', 'w') as f:
        json.dump(data, f)


class IntSpinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 28,
                 step_size: int = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("#343638", "#565B5E"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(value))



class MyCTkTabview(ctk.CTkTabview):
    
    _outer_spacing: int = 10  # px on top or below the button
    _outer_button_overhang: int = 8  # px
    _button_height: int = 10
    _segmented_button_border_width: int = 3


    def _set_grid_segmented_button(self):
        """ needs to be called for changes in corner_radius, anchor """

        if self._anchor.lower() in ("center", "n", "s"):
            self._segmented_button.grid(row=1, rowspan=2, column=0, columnspan=1, sticky="ns")
        elif self._anchor.lower() in ("nw", "w", "sw"):
            self._segmented_button.grid(row=1, rowspan=2, column=0, columnspan=1, sticky="nsw")
        elif self._anchor.lower() in ("ne", "e", "se"):
            self._segmented_button.grid(row=1, rowspan=2, column=0, columnspan=1, sticky="nse")



    def _set_grid_current_tab(self):
        """ needs to be called for changes in corner_radius, border_width """
        if self._anchor.lower() in ("center", "w", "nw", "n", "ne", "e", "e"):
            self._tab_dict[self._current_name].grid(row=3, column=0, sticky="nsew",
                                                    padx=self._corner_radius-10,
                                                    pady=self._corner_radius-15)
        else:
            self._tab_dict[self._current_name].grid(row=3, column=0, sticky="nsew",
                                                    padx=self._corner_radius-10,
                                                    pady=self._corner_radius-15)
            
    def _configure_grid(self):
        """ create 3 x 4 grid system """

        if self._anchor.lower() in ("center", "w", "nw", "n", "ne", "e", "e"):
            self.grid_rowconfigure(0, weight=0, minsize=self._outer_spacing)
            self.grid_rowconfigure(1, weight=0, minsize=self._outer_button_overhang)
            self.grid_rowconfigure(2, weight=0, minsize=self._button_height - self._outer_button_overhang)
            self.grid_rowconfigure(3, weight=1)
        else:
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=0, minsize=self._button_height - self._outer_button_overhang)
            self.grid_rowconfigure(2, weight=0, minsize=self._outer_button_overhang)
            self.grid_rowconfigure(3, weight=0, minsize=self._outer_spacing)

        self.grid_columnconfigure(0, weight=1,)

class TristateCheckbox(ctk.CTkButton):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.states = {0: "", 1: "P", 2: "E"}
        self.current_state = 0
        self.configure(text=self.states[self.current_state])
        self.configure(command=self.change_state)

    def change_state(self):
        self.current_state = (self.current_state + 1) % 3
        self.configure(text=self.states[self.current_state])
        if self.current_state != 0:
            self.configure(border_color="#1f6aa5")
        else:
            self.configure(border_color="#949A9F")

class Skill:
    def __init__(self, frame, skill_name, y_position):
        self.checkbox = TristateCheckbox(frame, height=25, width=25, border_width=3)
        self.checkbox.configure(fg_color ="#343638")
        self.checkbox.place(x=0, y=y_position)

        self.text = CTkLabel(frame, text="  __  ", font=("Arial", 15))
        self.text.place(x=30, y=y_position)

        self.button = ctk.CTkButton(frame, text=skill_name, border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
        self.button.place(x=55, y=y_position)

class SaveThrow:
    def __init__(self, frame, attribute, x, y):
        self.radio = ctk.CTkRadioButton(frame, radiobutton_width=20, radiobutton_height=20, font=("Arial", 15))
        self.radio.configure(text="  __  ")
        self.radio.place(x=x, y=y)
        self.button = ctk.CTkButton(frame, text=attribute, border_spacing=0, width=20, height=10, fg_color="#2B2B2B", font=("Arial", 15))
        self.button.place(x=x+52, y=y)

class Attribute:
    def __init__(self, frame, name, x, y):
        self.frame = MyCTkTabview(frame, width=60, height=100, corner_radius=20, fg_color="#2b2b2b")
        self.frame.place(x=x, y=y)
        self.tab = self.frame.add(f"{name}:")
        self.frame._segmented_button.configure(corner_radius=10)
        self.tab_frame = ctk.CTkFrame(self.tab, width=60, height=100, corner_radius=20)
        self.tab_frame.place(x=0, y=0)
        self.mod = ctk.CTkLabel(self.tab_frame, text="", corner_radius=20, height=8, width=8, font=("Arial", 25))
        self.mod.place(x=0, y=0)
        self.total = ctk.CTkEntry(self.frame, width=40, height=15, corner_radius=20, border_width=1)
        self.total.bind('<Return>', lambda event: self.set_attribute(name))
        self.total.bind('<FocusOut>', lambda event: self.set_attribute(name))
        self.total.bind('<Return>', lambda event: self.set_attribute_mod(name))
        self.total.bind('<FocusOut>', lambda event: self.set_attribute_mod(name))
        self.total.place(x=10, y=70)


    def set_attribute(self, name):
        data = load_data()
        last_selected_name = data['last_selected_character']

        # Find the dictionary for the last selected character
        for character in data['characters']:
            if character['name'] == last_selected_name:
                # Set the background
                character[name] = self.total.get()
                break

        save_data(data)
    
    def set_attribute_mod(self, name):
        data = load_data()
        last_selected_name = data['last_selected_character']

        # Find the dictionary for the last selected character
        for character in data['characters']:
            if character['name'] == last_selected_name:
                # Set the background
                value = math.floor((int(self.total.get()) - 10) / 2)
                character[f"{name}_mod"] = f"{f' {value}' if value < 0 else f'+{value}'}"
                self.mod.configure(text=f"{f' {value}' if value < 0 else f'+{value}'}")

        save_data(data)












        


