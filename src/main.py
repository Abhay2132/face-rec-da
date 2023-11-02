import customtkinter as ctk
import ui_

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("800x400")
		self.title("Abhay")
		# self.resizable(False, False)
		
		self.mainFrame = ui_.MainFrame(self)
		self.leftFrame = ui_.LeftFrame(self)
		self.rightFrame = ui_.RightFrame(self)
		
		self.grid_columnconfigure((0,2), minsize=150);
		self.grid_columnconfigure(1, weight=1, minsize=500);
		self.grid_rowconfigure(0, minsize=150, weight=1);
		
		padx = 3
		pady = 6
		
		self.mainFrame.grid(padx=padx, pady=pady,row=0, column=1, sticky="nswe")
		self.leftFrame.grid(row=0, padx=padx, pady=pady,column=0, sticky="nswe")
		self.rightFrame.grid(row=0, padx=padx, pady=pady,column=2, sticky="nswe")
		
		self.bind("<Configure>", self.on_resize)
		
	def on_resize(self, event):
		screen_height = event.height
		screen_width = event.width
		width = screen_width - 300
		h = 9/16*width
		self.mainFrame.label.configure(text=("width :" +str(event.width)+"px"))
		
if __name__ == "__main__":
	# ctk.set_default_color_theme("green")
	ctk.set_appearance_mode("light")
	app = App()
	app.mainloop()