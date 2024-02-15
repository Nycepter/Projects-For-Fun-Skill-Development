import customtkinter as ctk
from customtkinter import *
from typing import Union, Tuple, Dict, List, Callable, Optional, Any

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




        


