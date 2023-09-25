import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END
import sys

# DON'T CREATE PYCACHE FILES
sys.dont_write_bytecode = True

class UIScreens():
    def __init__(self):
        self.splash_time = 5000
        self.splash = tk.Tk()
        # WINDOW SETTINGS
        self.splash.withdraw() # HIDE WINDOW WHILE CALCULATING
        self.splash.update_idletasks()

        # CENTER WINDOW
        x = (self.splash.winfo_screenwidth() - 850) / 2
        y = (self.splash.winfo_screenheight() - 500) / 2
        self.splash.geometry("850x500+%d+%d" % (x, y))
        self.splash.deiconify() # SHOW THE WINDOW AFTER CALCULATE
        # HIDE THE PERMISSON TO REDIRECT THE WINDOW
        self.splash.overrideredirect(True) 

        # LOGO SPLASH ROOT IMAGE
        _image = tk.PhotoImage(file="C:/Users/conta/proj1_topicos_avancados/tap-analisador/python/img/splash_main.png") 

        # SETTING IMAGE
        self.img = tk.Label(self.splash)
        self.img.place(x=0, y=0, width=850, height=500)
        self.img.configure(image=_image)

        # CALL MAIN WINDOW AFTER SOME MILISECONDS
        self.splash.after(self.splash_time, self.main_screen)
        self.splash.mainloop()

    def main_screen(self):
        self.splash.destroy()

        self.bg_color = "#A073FA"
        self.white = "#FFFFFF"
        self.black = "#000000"

        self.main = tk.Tk()

        self.main.title('Analisador de Frequência')
        self.main.iconbitmap("C:/Users/conta/proj1_topicos_avancados/tap-analisador/python/img/ads.ico")
         # CENTER WINDOW
        x = (self.main.winfo_screenwidth() - 500) / 2
        y = ((self.main.winfo_screenheight() - 200) / 2)
        self.main.geometry("1000x500+%d+%d" % (x, y))
        self.main.deiconify() # SHOW THE WINDOW AFTER CALCULATE
        self.main.configure(background=self.bg_color) #CHANGE BACKGROUND COLOR
        # HIDE THE PERMISSON TO REDIRECT THE WINDOW
        self.main.minsize(500, 200)
        self.main.maxsize(500, 200)


        self.label = tk.Label(self.main)
        self.label.place(x=30, y=15, width=500, height=50)
        self.label.configure(
            background=self.bg_color,
            foreground=self.black,
            text='Informe o path:',
            font='-family {Tw Cen MT} -size 18 -weight bold',
            anchor='w'
        )

        self.entry = tk.Entry(self.main)
        self.entry.place(x=30, y=75, width=440, height=30)
        self.entry.configure(
            background = self.white,
            foreground = self.black,
            font = '-family {Tw Cen MT} -size 14',
            relief='flat'   
        )

        self.button_send = tk.Button(self.main)
        self.button_send.place(x=170, y=130, width=75, height=30)
        self.button_send.configure(
            background=self.black,
            foreground=self.bg_color,
            relief='flat',
            activebackground=self.white,
            activeforeground=self.bg_color,
            font='-family {Seoge UI} -size 14 -weight bold',
            text='ok',
            anchor='center',
            cursor='hand2',
            command=self.on_click_send
        )

        self.button_clear = tk.Button(self.main)
        self.button_clear.place(x=260, y=130, width=75, height=30)
        self.button_clear.configure(
            background=self.black,
            foreground=self.bg_color,
            relief='flat',
            activebackground=self.white,
            activeforeground=self.bg_color,
            font='-family {Seoge UI} -size 14 -weight bold',
            text='clear',
            anchor='center',
            cursor='hand2',
            command=self.on_click_clear
        )


    def on_click_clear(self) -> None:
        """
        Função clear limpa o que foi digitado no campo 
        de entrada self.entry
        """
        self.entry.delete(0, END)


    def on_click_send(self) -> None:
        """
        Função send chama o arquivo de leitura para realizar 
        a operação leitura e escrita 
        """
        # TODO mostar as pessoas o conceito de privado em python
        # from read_files 
        from read_files import readf_by_extension 
        try:
            if readf_by_extension(self.entry.get(), ".srt"):
                messagebox.showinfo("Operação concluída", "Operação bem sucedida!\nConfira a pasta ./resultados");
        except:
            messagebox.showerror("Path iválido", "Você deve seguir o padrão\nC:/path/path...");



        self.main.mainloop()



if __name__ == '__main__':
    app = UIScreens()
    sys.exit(0)