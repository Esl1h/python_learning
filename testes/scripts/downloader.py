#!/bin/env python3
# -*- coding: utf-8 -*-

import queue, threading, os
from urllib.request import urlretrieve
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_title("Py3k Downloader")
        self.menubar = Menu(self)
        self.option_add('*tearOff', FALSE)
        self.resizable(FALSE,FALSE)
        self.link = StringVar()
        self.filename = StringVar()
        self.perc = StringVar()
        self.MENUmouse = Menu(self, tearoff=0)
        self.MENUmouse.add_command(label="Recortar")
        self.MENUmouse.add_command(label="Copiar")
        self.MENUmouse.add_command(label="Colar")
        self.config(menu=self.menubar)
        self.bind("<Button-3><ButtonRelease-3>", self.show_mouse_menu)
        ttk.Label(self, text='URL: ').grid(row=1, column=1)
        ttk.Label(self, text='Save as: ').grid(row=2, column=1)
        self.url_entry = ttk.Entry(self, width=50, textvariable=self.link)
        self.url_entry.grid(row=1, column=2)
        self.file_entry = ttk.Entry(self, width=50, textvariable=self.filename)
        self.file_entry.grid(row=2, column=2)
        self.browse = ttk.Button(self, text='Save as', command=self.save).grid(row=3, column=1)
        self.download_button = ttk.Button(self, text='DOWNLOAD', command=self.download).grid(row=4, column=1)
        self.queue = queue.Queue()
        self.progressbar = ttk.Progressbar(self, orient='horizontal', length=400, mode='determinate')
        self.progressbar["maximum"] = 100.0
        self.progressbar["value"] = 0
        self.progressbar.grid(row=4, column=2)
        ttk.Label(self, textvariable=self.perc).grid(row=3, column=2)
        self.url_entry.focus()
    
    def show_mouse_menu(self, e):
        w = e.widget
    
        self.MENUmouse.entryconfigure("Recortar", command=lambda: w.event_generate("<<Cut>>"))
        self.MENUmouse.entryconfigure("Copiar", command=lambda: w.event_generate("<<Copy>>"))
        self.MENUmouse.entryconfigure("Colar", command=lambda: w.event_generate("<<Paste>>"))
        self.MENUmouse.tk.call("tk_popup", self.MENUmouse, e.x_root, e.y_root)
    
    def save(self):
        self.filename.set(asksaveasfilename())
        
    def download(self):
        self.url = self.link.get()
        self.arq = self.filename.get()
        
        if len(self.url) == 0:
            messagebox.showerror(message='Please insert download link', title='Error')
            return
            
        if len(self.arq) == 0:
            self.arq = os.path.basename(self.url)
            self.filename.set(self.arq)
            
        self.thread = ThreadedClient(self.queue, self.url, self.arq)
        self.thread.start()
        self.periodiccall()
        
    def periodiccall(self):
        self.checkqueue()
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.progressbar["value"] = 0.0
            messagebox.showinfo(message='Download finished', title='Info')
            self.destroy()
    
    def checkqueue(self):
        while self.queue.qsize():
            try:
                self.percent = self.queue.get()
                self.perc.set('Progress: ' + str(self.percent)[0:5] + '%')
                self.progressbar["value"] = self.percent
            except:
                pass
    
class ThreadedClient(threading.Thread):
    def __init__(self, queue, url, arq):
        threading.Thread.__init__(self)
        self.queue = queue
        self.url = url
        self.arq = arq
    
    def reporthook(self, blocknum, blocksize, totalsize):
        self.percent =  blocknum * blocksize * 100 / totalsize
        self.queue.put(self.percent)
    
    def run(self):
        try:
            urlretrieve(self.url, self.arq, self.reporthook)
        except ValueError:
            messagebox.showerror(message='Please insert valid download link', title='Error')
    
app = App()
app.mainloop()