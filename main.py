from tkinter import filedialog, PhotoImage
from idlelib.tooltip import Hovertip
from functools import partial
import tkinter as tk
import os
import base64
import json


home_dic = os.getcwd()

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
        self.hearts = tk.Frame(self.frame_menu, bd=1, highlightbackground='gray', highlightthickness=.5)
        self.prayers = tk.Frame(self.frame_menu, bd=1, highlightbackground='gray', highlightthickness=.5)
        self.relics = tk.Frame(self.frame_menu, bd=1, highlightbackground='gray', highlightthickness=.5)
        self.beads = tk.Frame(self.frame_menu, bd=1, highlightbackground='gray', highlightthickness=.5)
        self.stats = tk.Frame(self.frame_menu, bd=1, highlightbackground="gray", highlightthickness=.5)
        self.abilities = tk.Frame(self.frame_menu, bd=1, highlightbackground="gray", highlightthickness=.5)

        self.frame_navigation.place(relx=0, relheight=.10, relwidth=1)
        self.frame_menu.place(rely=.10, relx=0, relheight=.90, relwidth=1)
        self.frame_footer.place(rely=.90, relheight=.10, relwidth=1)

        self.navigation_widgets()
        self.load_widgets()
        self.footer_widgets()

        self.hearts_list = self.load_json('hearts')
        self.prayers_list = self.load_json('prayers')
        self.relics_list = self.load_json('relics')
        self.beads_list = self.load_json('beads')
        self.abilities_list = self.load_json('skills')

    def load_json(self, arg):
        json_path = os.getcwd() + '/assets/' + arg + '.json'
        json_file = open(json_path, 'rb')
        asset_json = json.loads(json_file.read())
        return asset_json[arg]
    
    # Commands
    def select_file(self):
        filepath = os.getenv('APPDATA') + '/../LocalLow/TheGameKitchen/Blasphemous/Savegames'
        self.filename = tk.filedialog.askopenfilename(initialdir=filepath, title='Select file',
                                                 filetype=(
                                                     ('.save file', '.save'),
                                                     ('.json file', 'json'))
                                                 )
        if not self.filename:
            return
        self.load_text.set(self.filename)
        self.load_file(self.filename)

    def load_file(self, filepath):
        file = open(filepath, 'rb')
        _, file_extension = os.path.splitext(filepath)
        file_read = file.read()

        if file_extension == '.save':
            file_decoded = base64.decodebytes(file_read)
            self.file_json = json.loads(file_decoded)
        else:
            self.file_json = json.loads(file_read)

        self.heart_btn['state'] = 'normal'
        self.relic_btn['state'] = 'normal'
        self.prayer_btn['state'] = 'normal'
        self.bead_btn['state'] = 'normal'
        self.stats_btn['state'] = 'normal'
        self.abilities_btn['state'] = 'normal'

        self.load_widgets('home')

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

        self.file_json = ""

        self.heart_btn['state'] = 'disabled'
        self.relic_btn['state'] = 'disabled'
        self.prayer_btn['state'] = 'disabled'
        self.bead_btn['state'] = 'disabled'
        self.stats_btn['state'] = 'disabled'
        self.abilities_btn['state'] = 'disabled'

    def clear_widgets(self):
        self.load.place_forget()
        self.header.place_forget()
        self.general_stats.place_forget()
        self.hearts.place_forget()
        self.prayers.place_forget()
        self.relics.place_forget()
        self.beads.place_forget()
        self.stats.place_forget()
        self.abilities.place_forget()
    
    # Widgets
    def navigation_widgets(self):
        global home_dic

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
        self.heart_btn['state'] = 'disabled'

        # Prayers button
        self.prayer_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_prayers.png')
        self.prayer_btn = tk.Button(self.frame_navigation, image=self.prayer_icon, bg='red', command=partial(self.load_widgets, "prayers"))
        Hovertip(self.prayer_btn, "Prayer selection", hover_delay=300)
        self.prayer_btn.grid(row=0, column=2, sticky=tk.E, padx=(5, 0), pady=(3, 0))
        self.prayer_btn['state'] = 'disabled'

        # Relics button
        self.relic_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_relics.png')
        self.relic_btn = tk.Button(self.frame_navigation, image=self.relic_icon, bg='red', command=partial(self.load_widgets, "relics"))
        Hovertip(self.relic_btn, "Relic selection", hover_delay=300)
        self.relic_btn.grid(row=0, column=3, sticky=tk.E, padx=(5, 0), pady=(3, 0))
        self.relic_btn['state'] = 'disabled'

        # Beads button
        self.bead_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_beads.png')
        self.bead_btn = tk.Button(self.frame_navigation, image=self.bead_icon, bg='red', command=partial(self.load_widgets, "beads"))
        Hovertip(self.bead_btn, "Bead selection", hover_delay=300)
        self.bead_btn.grid(row=0, column=4, sticky=tk.E, padx=(5, 0), pady=(3, 0))
        self.bead_btn['state'] = 'disabled'

        # Stats button
        self.stats_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_stats.png')
        self.stats_btn = tk.Button(self.frame_navigation, image=self.stats_icon, bg='red', command=partial(self.load_widgets, "stats"))
        Hovertip(self.stats_btn, "Stats display", hover_delay=300)
        self.stats_btn.grid(row=0, column=5, sticky=tk.E, padx=(5, 0), pady=(3, 0))
        self.stats_btn['state'] = 'disabled'

        # Abilities button
        self.abilities_icon = PhotoImage(file=home_dic + '\\assets\\images\\Menu_abilities.png')
        self.abilities_btn = tk.Button(self.frame_navigation, image=self.abilities_icon, bg='red', command=partial(self.load_widgets, "abilities"))
        Hovertip(self.abilities_btn, "Abilities selection", hover_delay=300)
        self.abilities_btn.grid(row=0, column=6, sticky=tk.E, padx=(5, 0), pady=(3, 0))
        self.abilities_btn['state'] = 'disabled'

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
            
            case 'hearts':
                self.hearts.place(relheight=1, relwidth=1)
                self.hearts_widgets()

            case 'prayers':
                self.prayers.place(relheight=1, relwidth=1)
                self.prayer_widgets()

            case 'relics':
                self.relics.place(relheight=1, relwidth=1)
                self.relic_widgets()

            case 'beads':
                self.beads.place(relheight=1, relwidth=1)
                self.bead_widgets()

            case "stats":
                self.stats.place(relheight=1, relwidth=1)
                self.stats_widgets()

            case 'abilities':
                self.abilities.place(relheight=1, relwidth=1)
                self.abilities_widgets()

    def file_widgets(self):
        # Load textbox
        self.load_text = tk.StringVar()
        load_label = tk.Label(self.load, text='Load:', font=('bold', 14))
        load_label.grid(row=0, column=0, sticky=tk.E, pady=5)
        load_entry = tk.Entry(self.load, textvariable=self.load_text, width=80, state='disabled')
        load_entry.grid(row=0, column=1, sticky=tk.E)

        # Load button
        load_btn = tk.Button(self.load, text='Load file', width=12, command=self.select_file)
        load_btn.grid(row=0, column=2, sticky=tk.E, padx=10)

        # New button
        new_btn = tk.Button(self.load, text='New file', width=12, command=self.new_file)
        new_btn.grid(row=0, column=3, sticky=tk.E)

        if(hasattr(self, 'file_json')):
            self.load_text.set(self.filename)

    def header_widgets(self):
        # Time textbox
        self.time_text = tk.StringVar(value="0 s")
        time_label = tk.Label(self.header, text='Time:', font=('bold', 14))
        time_label.grid(row=2, column=0, sticky=tk.E, pady=(50, 10), padx=(10, 0))
        time_entry = tk.Entry(self.header, textvariable=self.time_text, justify=tk.RIGHT, state='disabled')
        time_entry.grid(row=2, column=1, sticky=tk.W, pady=(50, 10))

        # Percent textbox
        self.percent_text = tk.StringVar(value="0 %")
        percent_label = tk.Label(self.header, text='Percent:', font=('bold', 14), pady=10)
        percent_label.grid(row=3, column=0, sticky=tk.E, padx=(10, 0))
        percent_entry = tk.Entry(self.header, textvariable=self.percent_text, justify=tk.RIGHT)
        percent_entry.grid(row=3, column=1, sticky=tk.W)

        # Purge textbox
        self.purge_text = tk.StringVar(value="0")
        purge_label = tk.Label(self.header, text='Purge:', font=('bold', 14), pady=10)
        purge_label.grid(row=4, column=0, sticky=tk.E, padx=(10, 0))
        purge_entry = tk.Entry(self.header, textvariable=self.purge_text, justify=tk.RIGHT)
        purge_entry.grid(row=4, column=1, sticky=tk.E)

        # Location textbox
        self.location_text = tk.StringVar(value="-")
        location_label = tk.Label(self.header, text='Location:', font=('bold', 14), pady=10)
        location_label.grid(row=5, column=0, sticky=tk.E, padx=(10, 0))
        location_entry = tk.Entry(self.header, textvariable=self.location_text, justify=tk.RIGHT, state='disabled')
        location_entry.grid(row=5, column=1, sticky=tk.E)

        if(hasattr(self, 'file_json')):
            self.time_text.set(self.file_json['commonElements']['ID_PERSISTENT_MANAGER']['Time'])
            self.percent_text.set(self.file_json['commonElements']['ID_PERSISTENT_MANAGER']['Percent'])
            self.purge_text.set(self.file_json['commonElements']['ID_PERSISTENT_MANAGER']['Purge'])

    def general_stats_widgets(self):
        # Attack Speed textbox
        self.attackSpeed_text = tk.StringVar()
        attackSpeed_label = tk.Label(self.general_stats, text='Attack Speed:', font=('bold', 14))
        attackSpeed_label.grid(row=0, column=0, sticky=tk.E, padx=(10, 0), pady=(30, 10))
        attackSpeed_entry = tk.Entry(self.general_stats, textvariable=self.attackSpeed_text)
        attackSpeed_entry.grid(row=0, column=1, sticky=tk.E, pady=(30, 10))

        # Fervour textbox
        self.fervour_text = tk.StringVar()
        fervour_label = tk.Label(self.general_stats, text='Fervour:', font=('bold', 14), pady=10)
        fervour_label.grid(row=1, column=0, sticky=tk.E, padx=(10, 0))
        fervour_entry = tk.Entry(self.general_stats, textvariable=self.fervour_text)
        fervour_entry.grid(row=1, column=1, sticky=tk.E)

        # Life textbox
        self.life_text = tk.StringVar()
        life_label = tk.Label(self.general_stats, text="Life:", font=('bold', 14), pady=10)
        life_label.grid(row=2, column=0, sticky=tk.E, padx=(10, 0))
        life_entry = tk.Entry(self.general_stats, textvariable=self.life_text)
        life_entry.grid(row=2, column=1, sticky=tk.E)

        # Flask textbox
        self.flask_text = tk.StringVar()
        flask_label = tk.Label(self.general_stats, text="Flask:", font=('bold', 14), pady=10)
        flask_label.grid(row=3, column=0, sticky=tk.E, padx=(10, 0))
        flask_entry = tk.Entry(self.general_stats, textvariable=self.flask_text)
        flask_entry.grid(row=3, column=1, sticky=tk.E)

        # Purge textbox
        self.general_stats_purge_text = tk.StringVar()
        general_stats_purge_label = tk.Label(self.general_stats, text="Purge:", font=('bold', 14), pady=10)
        general_stats_purge_label.grid(row=4, column=0, sticky=tk.E, padx=(10, 0))
        general_stats_purge_entry = tk.Entry(self.general_stats, textvariable=self.general_stats_purge_text)
        general_stats_purge_entry.grid(row=4, column=1, sticky=tk.E)

        if(hasattr(self, 'file_json')):
            self.attackSpeed_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['AttackSpeed'])
            self.fervour_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Fervour'])
            self.life_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Life'])
            self.flask_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Flask'])
            self.general_stats_purge_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['Purge'])

    def hearts_widgets(self):
        global home_dic

        for index, heart in enumerate(self.hearts_list):
            # PhotoImages have to be self/global 
            globals()[heart['name'] + "_icon"] = PhotoImage(file=home_dic + f"\\assets\\real_hearts\\{heart['source']}.png")
            locals()[heart['name'] + "_label"] = tk.Label(self.hearts, text=heart['name'])
            locals()[heart['name'] + "_label"].grid(row=index, column=0, sticky=tk.E)
            locals()[heart['name'] + "_button"] = tk.Button(self.hearts, image=globals()[heart['name'] + "_icon"])
            locals()[heart['name'] + "_button"].grid(row=index, column=1, sticky=tk.E)

    def prayer_widgets(self):
        global home_dic

        for index, prayer in enumerate(self.prayers_list):
            globals()[prayer['name'] + "_icon"] = PhotoImage(file=home_dic + f"\\assets\\real_prayers\\{prayer['source']}.png")
            locals()[prayer['name'] + "_label"] = tk.Label(self.prayers, text=prayer['name'])
            locals()[prayer['name'] + "_label"].grid(row=index, column=0, sticky=tk.E)
            locals()[prayer['name'] + "_button"] = tk.Button(self.prayers, image=globals()[prayer['name'] + "_icon"])
            locals()[prayer['name'] + "_button"].grid(row=index, column=1, sticky=tk.E)

    def relic_widgets(self):
        global home_dic

        for index, relic in enumerate(self.relics_list):
            globals()[relic['name'] + "_icon"] = PhotoImage(file=home_dic + f"\\assets\\real_relics\\{relic['source']}.png")
            locals()[relic['name'] + "_label"] = tk.Label(self.relics, text=relic['name'])
            locals()[relic['name'] + "_label"].grid(row=index, column=0, sticky=tk.E)
            locals()[relic['name'] + "_button"] = tk.Button(self.relics, image=globals()[relic['name'] + "_icon"])
            locals()[relic['name'] + "_button"].grid(row=index, column=1, sticky=tk.E)

    def bead_widgets(self):
        global home_dic

        for index, bead in enumerate(self.beads_list):
            globals()[bead['name'] + "_icon"] = PhotoImage(file=home_dic + f"\\assets\\real_beads\\{bead['source']}.png")
            locals()[bead['name'] + "_label"] = tk.Label(self.beads, text=bead['name'])
            locals()[bead['name'] + "_label"].grid(row=index, column=0, sticky=tk.E)
            locals()[bead['name'] + "_button"] = tk.Button(self.beads, image=globals()[bead['name'] + "_icon"])
            locals()[bead['name'] + "_button"].grid(row=index, column=1, sticky=tk.E)
    
    def stats_widgets(self):
        # Attack Speed textbox
        stats_attackSpeed_text = tk.StringVar()
        stats_attackSpeed_label = tk.Label(self.stats, text="Attack Speed:")
        stats_attackSpeed_label.grid(row=0, column=0, sticky=tk.E, padx=(10, 0), pady=(30, 10))
        stats_attackSpeed_entry = tk.Entry(self.stats, textvariable=stats_attackSpeed_text)
        stats_attackSpeed_entry.grid(row=0, column=1, sticky=tk.E, pady=(30, 10))

        stats_agility_text = tk.StringVar()
        stats_agility_label = tk.Label(self.stats, text="Agility:")
        stats_agility_label.grid(row=1, column=0, sticky=tk.E, padx=(10, 0), pady=(30, 10))
        stats_agility_entry = tk.Entry(self.stats, textvariable=stats_agility_text)
        stats_agility_entry.grid(row=1, column=1, sticky=tk.E, pady=(30, 10))

        if(hasattr(self, 'file_json')):
            stats_attackSpeed_text.set(self.file_json['commonElements']['ID_STATS']['currentValues']['AttackSpeed'])
    
    def abilities_widgets(self):
        global home_dic

        for index, abilities in enumerate(self.abilities_list):
            globals()[abilities['name'] + "_icon"] = PhotoImage(file=home_dic + f"\\assets\\real_skills\\{abilities['source']}.png")
            locals()[abilities['name'] + "_label"] = tk.Label(self.abilities, text=abilities['name'])
            locals()[abilities['name'] + "_label"].grid(row=index, column=0, sticky=tk.E)
            locals()[abilities['name'] + "_button"] = tk.Button(self.abilities, image=globals()[abilities['name'] + "_icon"])
            locals()[abilities['name'] + "_button"].grid(row=index, column=1, sticky=tk.E)
    
    def footer_widgets(self):
        # Exit button
        exit_btn = tk.Button(self.frame_footer, text='Exit', width=12, command=self.master.destroy)
        exit_btn.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # Clear button
        clear_btn = tk.Button(self.frame_footer, text='Clear', width=12, command=self.clear_fields)
        clear_btn.grid(row=0, column=1, sticky=tk.W)

        # Save as button
        saveAs_btn = tk.Button(self.frame_footer, text='Save as...', width=12)
        saveAs_btn.grid(row=0, column=2, sticky=tk.E, columnspan=6, padx=480)


app = Application()
app.master.mainloop()
