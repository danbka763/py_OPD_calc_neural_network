import tkinter as tk
from tkinter import *
from tkinter import messagebox
import neural


# neural.start()


height = 800
width = 700


Window = Tk()
Window.geometry(f"1000x700")
Window.title('Калькулятор')
Window.resizable(1, 1)
Window.config()
Window['bg'] = 'green'

def add_digit(digit):
	value = Calc.get()
	if value[0] == '0' and len(value) == 1:
		value = value[1:]
	Calc['state'] = tk.NORMAL
	Calc.delete(0, tk.END)
	Calc.insert(0, value + digit)
	Calc['state'] = tk.DISABLED


def add_operation(operation):
	value = Calc.get()
	if value[-1] in '+-/*':
		value = value[:-1]
	elif '+' in value or '-' in value or '/' in value or '*' in value:
		calculate()
		value = Calc.get()
	Calc['state'] = tk.NORMAL
	Calc.delete(0, tk.END)
	Calc.insert(0, value + operation)
	Calc['state'] = tk.DISABLED


def calculate():
	value = Calc.get()
	if value[-1] in '+-/*':
		value += value[:-1]
	Calc['state'] = tk.NORMAL
	Calc.delete(0, tk.END)
	try:
		Calc.insert(0, eval(value))
	except (NameError, SyntaxError):
		messagebox.showinfo('ВНИМАНИЕ!!!','Введите только цифры!!!')
		Calc.insert(0, 0)
	except ZeroDivisionError:
		messagebox.showinfo('ВНИМАНИЕ!!!','На ноль делить нельзя!!!')
		Calc.insert(0, 0)
	Calc['state'] = tk.DISABLED



def Clear():
	Calc['state'] = tk.NORMAL
	Calc.delete(0, tk.END)
	Calc.insert(0, 0)
	Calc['state'] = tk.DISABLED



def press_key(event):
	if event.char.isdigit():
		add_digit(event.char)
	elif event.char in '+-/*':
		add_operation(event.char)
	elif event.char == '\r':
		calculate()


def make_button(digit):
	return tk.Button(text = digit, bd = 5, font = ('Arial', 13), command = lambda : add_digit(digit))

def simple_operation(operation):
	return tk.Button(text = operation, bd = 5, font = ('Arial', 13), command = lambda : add_operation(operation))


def make_equal(operation):
	return tk.Button(text = operation, bd = 5, font = ('Arial', 13), command = calculate)


def make_clear(operation):
	return tk.Button(text = operation, bd = 5, font = ('Arial', 13), command = Clear)

# Picture_Back_Ground = PhotoImage(file = 'image/1.png')
# Picture_Label = Label(Window, image = Picture_Back_Ground)

# canvas = Canvas(Window, width = width, height = height)
# canvas.pack(fill = 'both', expand = True)
# canvas.create_image(0, 0, image = Picture_Back_Ground, anchor = 'nw')



Window.bind('<Key>', press_key)
Calc = tk.Entry(Window, justify = tk.RIGHT, font = ('Arial', 50), width = 15)
Calc.insert(0, '0')
Calc['state'] = tk.DISABLED
Calc.grid(row = 0, column = 0, columnspan = 4)

make_button('0').grid(row = 1, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('1').grid(row = 1, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('2').grid(row = 1, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('3').grid(row = 2, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('4').grid(row = 2, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('5').grid(row = 2, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('6').grid(row = 3, column = 0, stick = 'wens', padx = 5, pady = 5)
make_button('7').grid(row = 3, column = 1, stick = 'wens', padx = 5, pady = 5)
make_button('8').grid(row = 3, column = 2, stick = 'wens', padx = 5, pady = 5)
make_button('9').grid(row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)

simple_operation('+').grid(row = 1, column = 3, stick = 'wens', padx = 5, pady = 5)
simple_operation('-').grid(row = 2, column = 3, stick = 'wens', padx = 5, pady = 5)
simple_operation('*').grid(row = 3, column = 3, stick = 'wens', padx = 5, pady = 5)
simple_operation('/').grid(row = 4, column = 3, stick = 'wens', padx = 5, pady = 5)
make_equal('=').grid(row = 4, column = 2, stick = 'wens', padx = 5, pady = 5)
make_clear('C').grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5)

Window.grid_columnconfigure(0, minsize = 100)
Window.grid_columnconfigure(1, minsize = 100)
Window.grid_columnconfigure(2, minsize = 100)

Window.grid_rowconfigure(1, minsize = 100)
Window.grid_rowconfigure(2, minsize = 100)
Window.grid_rowconfigure(3, minsize = 100)
Window.grid_rowconfigure(4, minsize = 100)


Window.mainloop()