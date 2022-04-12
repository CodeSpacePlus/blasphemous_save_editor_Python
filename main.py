from tkinter import filedialog, PhotoImage
from idlelib.tooltip import Hovertip
from functools import partial
import tkinter as tk
import os
import base64
import json


class Application(object):
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("800x500")
        self.master.iconbitmap(os.getcwd() + "/assets/images/mask.ico")
        self.master.title('Blasphemous Save Editor -- Python Version: a0.0.1')
        self.master.resizable(False, False)

        self.frame_navigation = tk.Frame(self.master, bd=1, highlightbackground="black", highlightthickness=.5)
        self.frame_menu = tk.Frame(self.master, bd=1, highlightbackground="white", highlightthickness=.5)
        self.frame_footer = tk.Frame(self.master, bd=1, highlightbackground="red", highlightthickness=.5)

        # Sections
        self.load = tk.Frame(self.frame_menu, bd=1, highlightbackground="green", highlightthickness=.5)
        self.header = tk.Frame(self.frame_menu, bd=1, highlightbackground="blue", highlightthickness=.5)
        self.general_stats = tk.Frame(self.frame_menu, bd=1, relief=tk.SUNKEN, highlightbackground="gray", highlightthickness=.5)
        self.stats = tk.Frame(self.frame_menu, bd=1, highlightbackground="gray", highlightthickness=.5)

        self.frame_navigation.place(relx=0, relheight=.10, relwidth=1)
        self.frame_menu.place(rely=.10, relx=0, relheight=.90, relwidth=1)
        self.frame_footer.place(rely=.90, relheight=.10, relwidth=1)

        self.navigation_widgets()
        self.load_widgets()
        self.footer_widgets()

    # Commands
    def select_file(self):
        filepath = os.getenv('APPDATA') + '/../LocalLow/TheGameKitchen/Blasphemous/Savegames'
        filename = tk.filedialog.askopenfilename(initialdir=filepath, title='Select file',
                                                 filetype=(
                                                     ('.save file', '.save'),
                                                     ('.json file', 'json'))
                                                 )
        if not filename:
            return
        self.load_text.set(filename)
        self.load_file(filename)

    def load_file(self, filepath):
        file = open(filepath, 'rb')
        _, file_extension = os.path.splitext(filepath)
        file_read = file.read()

        if file_extension == '.save':
            file_decoded = base64.decodebytes(file_read)
            self.file_json = json.loads(file_decoded)
        else:
            self.file_json = json.loads(file_read)

        self.time_text.set(self.file_json['commonElements']['ID_PERSISTENT_MANAGER']['Time'])
        self.percent_text.set(self.file_json['commonElements']['ID_PERSISTENT_MANAGER']['Percent'])
        self.purge_text.set(self.file_json['commonElements']['ID_PERSISTENT_MANAGER']['Purge'])

        self.attackSpeed_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['AttackSpeed'])
        self.fervour_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Fervour'])
        self.life_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Life'])
        self.flask_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Flask'])
        self.general_stats_purge_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Purge'])

        self.stats_attackSpeed_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['AttackSpeed'])

    def new_file(self):
        self.load_file(filepath=os.getcwd()+"/assets/NewSave.json")
        self.load_text.set("NewSave.json")

    def clear_fields(self):
        self.load_text.set("")

        self.time_text.set("0 s")
        self.percent_text.set("0 %")
        self.purge_text.set("0")
        self.location_text.set("-")

        self.attackSpeed_text.set("")
        self.life_text.set("")
        self.fervour_text.set("")
        self.flask_text.set("")
        self.general_stats_purge_text.set("")

    def clear_widgets(self):
        self.load.place_forget()
        self.header.place_forget()
        self.general_stats.place_forget()
        self.stats.place_forget()
    
    # Widgets
    def navigation_widgets(self):
        home_dic = os.getcwd()

        # Home button
        self.home_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_home.png')
        self.home_btn = tk.Button(self.frame_navigation, image=self.home_icon, bg='red', command=self.load_widgets)
        Hovertip(self.home_btn, "Home/Load file", hover_delay=300)
        self.home_btn.grid(row=0, column=0, sticky=tk.E, padx=(5, 0), pady=(3, 0))

        # Hearts button
        self.heart_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_hearts.png')
        self.heart_btn = tk.Button(self.frame_navigation, image=self.heart_icon, bg='red', command=partial(self.load_widgets, "hearts"))
        Hovertip(self.heart_btn, "Heart selection", hover_delay=300)
        self.heart_btn.grid(row=0, column=1, sticky=tk.E, padx=(5, 0), pady=(3, 0))

        # Prayers button
        self.prayer_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_prayers.png')
        self.prayer_btn = tk.Button(self.frame_navigation, image=self.prayer_icon, bg='red', command=partial(self.load_widgets, "prayers"))
        Hovertip(self.prayer_btn, "Prayer selection", hover_delay=300)
        self.prayer_btn.grid(row=0, column=2, sticky=tk.E, padx=(5, 0), pady=(3, 0))

        # Relics button
        self.relic_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_relics.png')
        self.relic_btn = tk.Button(self.frame_navigation, image=self.relic_icon, bg='red', command=partial(self.load_widgets, "relics"))
        Hovertip(self.relic_btn, "Relic selection", hover_delay=300)
        self.relic_btn.grid(row=0, column=3, sticky=tk.E, padx=(5, 0), pady=(3, 0))

        # Beads button
        self.bead_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_beads.png')
        self.bead_btn = tk.Button(self.frame_navigation, image=self.bead_icon, bg='red', command=partial(self.load_widgets, "beads"))
        Hovertip(self.bead_btn, "Bead selection", hover_delay=300)
        self.bead_btn.grid(row=0, column=4, sticky=tk.E, padx=(5, 0), pady=(3, 0))

        # Stats button
        self.general_stats_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_stats.png')
        self.general_stats_btn = tk.Button(self.frame_navigation, image=self.general_stats_icon, bg='red', command=partial(self.load_widgets, "stats"))
        Hovertip(self.general_stats_btn, "Stats display", hover_delay=300)
        self.general_stats_btn.grid(row=0, column=5, sticky=tk.E, padx=(5, 0), pady=(3, 0))

        # Abilities button
        self.abilities_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_abilities.png')
        self.abilities_btn = tk.Button(self.frame_navigation, image=self.abilities_icon, bg='red', command=partial(self.load_widgets, "abilities"))
        Hovertip(self.abilities_btn, "Abilities selection", hover_delay=300)
        self.abilities_btn.grid(row=0, column=6, sticky=tk.E, padx=(5, 0), pady=(3, 0))

    def load_widgets(self, option="home"):
        self.clear_widgets()

        match option:
            case "home":
                self.load.place(rely=0, relx=0, relheight=.10, relwidth=1)
                self.header.place(rely=.1, relheight=1, relwidth=.5)
                self.general_stats.place(rely=.1, relx=.5, relheight=1, relwidth=.5)
                self.file_widgets()
                self.header_widgets()
                self.general_stats_widgets()

            case "stats":
                self.stats.place(relheight=1, relwidth=1)
                self.stats_widgets()

    def file_widgets(self):
        # Load textbox
        self.load_text = tk.StringVar()
        self.load_label = tk.Label(self.load, text='Load:', font=('bold', 14))
        self.load_label.grid(row=0, column=0, sticky=tk.E, pady=5)
        self.load_entry = tk.Entry(self.load, textvariable=self.load_text, width=80, state='disabled')
        self.load_entry.grid(row=0, column=1, sticky=tk.E)

        # Load button
        self.load_btn = tk.Button(self.load, text='Load file', width=12, command=self.select_file)
        self.load_btn.grid(row=0, column=2, sticky=tk.E, padx=10)

        # New button
        self.new_btn = tk.Button(self.load, text='New file', width=12, command=self.new_file)
        self.new_btn.grid(row=0, column=3, sticky=tk.E)

    def header_widgets(self):
        # Time textbox
        self.time_text = tk.StringVar(value="0 s")
        self.time_label = tk.Label(self.header, text='Time:', font=('bold', 14))
        self.time_label.grid(row=2, column=0, sticky=tk.E, pady=(50, 10), padx=(10, 0))
        self.time_entry = tk.Entry(self.header, textvariable=self.time_text, justify=tk.RIGHT, state='disabled')
        self.time_entry.grid(row=2, column=1, sticky=tk.W, pady=(50, 10))

        # Percent textbox
        self.percent_text = tk.StringVar(value="0 %")
        self.percent_label = tk.Label(self.header, text='Percent:', font=('bold', 14), pady=10)
        self.percent_label.grid(row=3, column=0, sticky=tk.E, padx=(10, 0))
        self.percent_entry = tk.Entry(self.header, textvariable=self.percent_text, justify=tk.RIGHT)
        self.percent_entry.grid(row=3, column=1, sticky=tk.W)

        # Purge textbox
        self.purge_text = tk.StringVar(value="0")
        self.purge_label = tk.Label(self.header, text='Purge:', font=('bold', 14), pady=10)
        self.purge_label.grid(row=4, column=0, sticky=tk.E, padx=(10, 0))
        self.purge_entry = tk.Entry(self.header, textvariable=self.purge_text, justify=tk.RIGHT)
        self.purge_entry.grid(row=4, column=1, sticky=tk.E)

        # Location textbox
        self.location_text = tk.StringVar(value="-")
        self.location_label = tk.Label(self.header, text='Location:', font=('bold', 14), pady=10)
        self.location_label.grid(row=5, column=0, sticky=tk.E, padx=(10, 0))
        self.location_entry = tk.Entry(self.header, textvariable=self.location_text, justify=tk.RIGHT, state='disabled')
        self.location_entry.grid(row=5, column=1, sticky=tk.E)

    def general_stats_widgets(self):
        # Attack Speed textbox
        self.attackSpeed_text = tk.StringVar()
        self.attackSpeed_label = tk.Label(self.general_stats, text='Attack Speed:', font=('bold', 14))
        self.attackSpeed_label.grid(row=0, column=0, sticky=tk.E, padx=(10, 0), pady=(30, 10))
        self.attackSpeed_entry = tk.Entry(self.general_stats, textvariable=self.attackSpeed_text)
        self.attackSpeed_entry.grid(row=0, column=1, sticky=tk.E, pady=(30, 10))

        # Fervour textbox
        self.fervour_text = tk.StringVar()
        self.fervour_label = tk.Label(self.general_stats, text='Fervour:', font=('bold', 14), pady=10)
        self.fervour_label.grid(row=1, column=0, sticky=tk.E, padx=(10, 0))
        self.fervour_entry = tk.Entry(self.general_stats, textvariable=self.fervour_text)
        self.fervour_entry.grid(row=1, column=1, sticky=tk.E)

        # Life textbox
        self.life_text = tk.StringVar()
        self.life_label = tk.Label(self.general_stats, text="Life:", font=('bold', 14), pady=10)
        self.life_label.grid(row=2, column=0, sticky=tk.E, padx=(10, 0))
        self.life_entry = tk.Entry(self.general_stats, textvariable=self.life_text)
        self.life_entry.grid(row=2, column=1, sticky=tk.E)

        # Flask textbox
        self.flask_text = tk.StringVar()
        self.flask_label = tk.Label(self.general_stats, text="Flask:", font=('bold', 14), pady=10)
        self.flask_label.grid(row=3, column=0, sticky=tk.E, padx=(10, 0))
        self.flask_entry = tk.Entry(self.general_stats, textvariable=self.flask_text)
        self.flask_entry.grid(row=3, column=1, sticky=tk.E)

        # Purge textbox
        self.general_stats_purge_text = tk.StringVar()
        self.general_stats_purge_label = tk.Label(self.general_stats, text="Purge:", font=('bold', 14), pady=10)
        self.general_stats_purge_label.grid(row=4, column=0, sticky=tk.E, padx=(10, 0))
        self.general_stats_purge_entry = tk.Entry(self.general_stats, textvariable=self.general_stats_purge_text)
        self.general_stats_purge_entry.grid(row=4, column=1, sticky=tk.E)

    def stats_widgets(self):
        # Attack Speed textbox
        self.stats_attackSpeed_text = tk.StringVar()
        self.stats_attackSpeed_label = tk.Label(self.stats, text="Attack Speed:")
        self.stats_attackSpeed_label.grid(row=0, column=0, sticky=tk.E, padx=(10, 0), pady=(30, 10))
        self.stats_attackSpeed_entry = tk.Entry(self.stats, textvariable=self.stats_attackSpeed_text)
        self.stats_attackSpeed_entry.grid(row=0, column=1, sticky=tk.E, pady=(30, 10))

        self.stats_agility_text = tk.StringVar()
        self.stats_agility_label = tk.Label(self.stats, text="Agility:")
        self.stats_agility_label.grid(row=1, column=0, sticky=tk.E, padx=(10, 0), pady=(30, 10))
        self.stats_agility_entry = tk.Entry(self.stats, textvariable=self.stats_agility_text)
        self.stats_agility_entry.grid(row=1, column=1, sticky=tk.E, pady=(30, 10))
    
    def footer_widgets(self):
        # Exit button
        self.exit_btn = tk.Button(self.frame_footer, text='Exit', width=12, command=self.master.destroy)
        self.exit_btn.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # Clear button
        self.clear_btn = tk.Button(self.frame_footer, text='Clear', width=12, command=self.clear_fields)
        self.clear_btn.grid(row=0, column=1, sticky=tk.W)

        # Save as button
        self.saveAs_btn = tk.Button(self.frame_footer, text='Save as...', width=12)
        self.saveAs_btn.grid(row=0, column=2, sticky=tk.E, columnspan=6, padx=480)


def load_json(arg):
    for asset in arg:
        json_path = os.getcwd() + '/assets/' + asset + '.json'
        json_file = open(json_path, 'rb')
        asset_json = json.loads(json_file.read())
        return asset_json[asset]


app = Application()
app.master.mainloop()
