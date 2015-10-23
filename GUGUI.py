from Tkinter import *
from GuitarUltimater import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	

		
		self.button.bind('<Button-1>', self.getTab)
	def createWidgets(self):
		self.search_bar = Entry(self, width=50)
		self.search_bar.insert(0, "Enter Song Title")
		self.search_bar.grid(row = 0, column = 0, pady=10, padx=5)
		

		
		self.button = Button(self, text="Go!")
		self.button.grid(row=0, column=1, pady=5, padx=5)
		
		self.text = Text(self, width=100, height=50)
		self.text.grid(row=1, pady=5, padx=5, columnspan=2)
		
	def getTab(self, event):
		self.text.delete('1.0', END)
		song = self.search_bar.get()
		url = search(song)
		tab = readUG(url)
		self.text.insert('1.0', tab)
		

		
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
