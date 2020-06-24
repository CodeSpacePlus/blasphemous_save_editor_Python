import tkinter as tk


class Application(object):
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("800x500")
        self.master.title('Blasphemous Save Editor -- Python Version: a0.0.1')
        self.master.resizable(False, False)

        self.load = tk.Frame(self.master, bd=1, highlightbackground="green", highlightthickness=.5)
        self.header = tk.Frame(self.master, bd=1, highlightbackground="blue", highlightthickness=.5)
        self.stats = tk.Frame(self.master, bd=1, relief=tk.SUNKEN, highlightbackground="gray", highlightthickness=.5)
        self.footer = tk.Frame(self.master, bd=1, highlightbackground="red", highlightthickness=.5)

        self.load.place(relx=0, relheight=.10, relwidth=1)
        self.header.place(rely=.20, relheight=.60, relwidth=.5)
        self.stats.place(relx=.5, rely=.20, relheight=.60, relwidth=1.0 - .5)
        self.footer.place(rely=.90, relheight=.10, relwidth=1)

        self.selected_item = 0
        self.load_widgets()
        self.header_widgets()
        self.footer_widgets()
        self.stats_widgets()

    # Commands

    # Widgets
    def load_widgets(self):
        # Load textbox
        self.load_text = tk.StringVar()
        self.load_label = tk.Label(self.load, text='Load:', font=('bold', 14), pady=10)
        self.load_label.grid(row=0, column=0, sticky=tk.E)
        self.load_entry = tk.Entry(self.load, textvariable=self.load_text, width=50, state='disabled')
        self.load_entry.grid(row=0, column=1, sticky=tk.E)

        # Load button
        self.load_btn = tk.Button(self.load, text='Load file', width=12)
        self.load_btn.grid(row=0, column=2, sticky=tk.E, padx=10)

        # New button
        self.new_btn = tk.Button(self.load, text='New file', width=12)
        self.new_btn.grid(row=0, column=3, sticky=tk.E)

    def header_widgets(self):
        # Time textbox
        self.time_text = tk.StringVar()
        self.time_text.set("0 s")
        self.time_label = tk.Label(self.header, text='Time:', font=('bold', 14))
        self.time_label.grid(row=2, column=0, sticky=tk.E, pady=(50, 10), padx=(10, 0))
        self.time_entry = tk.Entry(self.header, textvariable=self.time_text, justify=tk.RIGHT, state='disabled')
        self.time_entry.grid(row=2, column=1, sticky=tk.W, pady=(50, 10))

        # Percent textbox
        self.percent_text = tk.StringVar()
        self.percent_text.set("0 %")
        self.percent_label = tk.Label(self.header, text='Percent:', font=('bold', 14), pady=10)
        self.percent_label.grid(row=3, column=0, sticky=tk.E, padx=(10, 0))
        self.percent_entry = tk.Entry(self.header, textvariable=self.percent_text, justify=tk.RIGHT)
        self.percent_entry.grid(row=3, column=1, sticky=tk.W)

        # Purge textbox
        self.purge_text = tk.StringVar()
        self.purge_text.set("0")
        self.purge_label = tk.Label(self.header, text='Purge:', font=('bold', 14), pady=10)
        self.purge_label.grid(row=4, column=0, sticky=tk.E, padx=(10, 0))
        self.purge_entry = tk.Entry(self.header, textvariable=self.purge_text, justify=tk.RIGHT)
        self.purge_entry.grid(row=4, column=1, sticky=tk.E)

        # Location textbox
        self.location_text = tk.StringVar()
        self.location_label = tk.Label(self.header, text='Location:', font=('bold', 14), pady=10)
        self.location_label.grid(row=5, column=0, sticky=tk.E, padx=(10, 0))
        self.location_entry = tk.Entry(self.header, textvariable=self.location_text, justify=tk.RIGHT, state='disabled')
        self.location_entry.grid(row=5, column=1, sticky=tk.E)

    def stats_widgets(self):
        # Attack Speed textbox
        self.attackSpeed_text = tk.StringVar()
        self.attackSpeed_label = tk.Label(self.stats, text='Attack Speed:', font=('bold', 14))
        self.attackSpeed_label.grid(row=0, column=0, sticky=tk.E, padx=(10, 0), pady=(30, 10))
        self.attackSpeed_entry = tk.Entry(self.stats, textvariable=self.attackSpeed_text)
        self.attackSpeed_entry.grid(row=0, column=1, sticky=tk.E, pady=(30, 10))

        # Fervour textbox
        self.fervour_text = tk.StringVar()
        self.fervour_label = tk.Label(self.stats, text='Fervour:', font=('bold', 14), pady=10)
        self.fervour_label.grid(row=1, column=0, sticky=tk.E, padx=(10, 0))
        self.fervour_entry = tk.Entry(self.stats, textvariable=self.fervour_text)
        self.fervour_entry.grid(row=1, column=1, sticky=tk.E)

        # Life textbox
        self.life_text = tk.StringVar()
        self.life_label = tk.Label(self.stats, text="Life:", font=('bold', 14), pady=10)
        self.life_label.grid(row=2, column=0, sticky=tk.E, padx=(10, 0))
        self.life_entry = tk.Entry(self.stats, textvariable=self.life_text)
        self.life_entry.grid(row=2, column=1, sticky=tk.E)

        # Flask textbox
        self.flask_text = tk.StringVar()
        self.flask_label = tk.Label(self.stats, text="Flask:", font=('bold', 14), pady=10)
        self.flask_label.grid(row=3, column=0, sticky=tk.E, padx=(10, 0))
        self.flask_entry = tk.Entry(self.stats, textvariable=self.flask_text)
        self.flask_entry.grid(row=3, column=1, sticky=tk.E)

        # Purge textbox
        self.stats_purge_text = tk.StringVar()
        self.stats_purge_label = tk.Label(self.stats, text="Purge:", font=('bold', 14), pady=10)
        self.stats_purge_label.grid(row=4, column=0, sticky=tk.E, padx=(10, 0))
        self.stats_purge_entry = tk.Entry(self.stats, textvariable=self.stats_purge_text)
        self.stats_purge_entry.grid(row=4, column=1, sticky=tk.E)

    def footer_widgets(self):
        # Exit button
        self.exit_btn = tk.Button(self.footer, text='Exit', width=12, command=self.master.destroy)
        self.exit_btn.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # Clear button
        self.clear_btn = tk.Button(self.footer, text='Clear', width=12)
        self.clear_btn.grid(row=0, column=1, sticky=tk.W)

        # Save as button
        self.saveAs_btn = tk.Button(self.footer, text='Save as...', width=12)
        self.saveAs_btn.grid(row=0, column=2, sticky=tk.E, columnspan=6, padx=480)


app = Application()
app.master.mainloop()
