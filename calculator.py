from tkinter import *
from math import pi, tan, sin, cos


root = Tk()


# variables 
HEIGHT = 350
WIDTH = 200
result = [""]
after_equal = False
value_error = False
result_display = StringVar()	


# functions 


def set_variable(input, isresult, display, error, result_list):
	if error:  # if display is an error, clear result list and display a new input
		result_list.clear()
		result_list.append(input)
		display.set(result_list[-1])
		error = False
	elif (input in "/+-*Cos(Sen(Tan(Abs(√)^"): # if button "=" was pressed and an operator was pressed afterwards, concactenate the operator
		isresult = False
		new_result = result_display.get() + input
		result_list.append(new_result)
		display.set(result[-1])
	elif isresult: # if button "=" was pressed and a number was pressed afterwards, remove the result and display a new string
		isresult = False
		new_result = input
		result_list.append(new_result)
		display.set(result[-1])
	else: # concat a number to the string 
		new_result = result_display.get() + input
		result_list.append(new_result)
		display.set(result[-1])


def clear_result(result_list):
	"""clear the result list, display an empty string and make the ind var -1 again"""
	result_list.clear()
	result_list.append("")
	result_display.set(result_list[-1])
	


def operation(input_list, output_list):  # function that interprets operation from a string list and converts them to values 
 # remove +s as we will add everything up in the end anyway
	index = 0  # artificial index in case there are repeated elements
	for element in input_list:
		if element == "-":
			input_list[index + 1] = "-" + input_list[index + 1]  # make the next number negative
		elif "^" in element:
			subele_list = element.split("^")
			subele_result = float(subele_list[0]) ** float(subele_list[1])
			output_list.append(subele_result)
		elif "√" in element:
			element = element.strip("√")
			element = element ** (1/2)
			output_list.append(element)
		elif "Abs(" in element:  # strip the string, do the corresponding operation and append to a total list
			element = element.strip("Abs()")
			element = float(element)
			element = abs(element)
			output_list.append(element)
		elif "Sin(" in element:
			element = element.strip("Sin()")
			element = float(element)
			element = sin(element)
			output_list.append(element)
		elif "Cos(" in element:
			element = element.strip("Cos()")
			element = float(element)
			element = sos(element)
			output_list.append(element)
		elif "Tan(" in element:
			element = element.strip("Tan()")
			element = float(element)
			element = tan(element)
			output_list.append(element)
		elif "π" in element:
			element = pi
			output_list.append(pi)
		else:
			try:  
				  # if its just a positive or negative number
				element = float(element)
				output_list.append(element)
			except ValueError:
				output_list.append("Invalid Input")
		index += 1 	# increase index by one

	

def equal_func(display, isresult, result_list, error):
	current_display = display.get()  # get current display
	string_list = current_display.split(" ")  # split the string in fragments whenever there is a space
	if "+" in string_list:
		string_list.remove("+")
	total_list = []
	total = 0
	list_1 = []
	list_2 = []
	
	for element in string_list:
		if ("*" in element) or ("/" in element):
			list_1.append(element)
		else:
			list_2.append(element)
	operation(list_2, total_list)
	for subelement in list_1:
		list_3 = []
		if "*" in subelement:	
			components_list = subelement.split("*")  # split the string in fragments whenever there is a *
			operation(components_list, list_3)
			multiplication_result = list_3[0] * list_3[1]
			total_list.append(multiplication_result)
		elif "/" in subelement:
			components_list = subelement.split("/")  # split the string in fragments whenever there is a /
			operation(components_list, list_3)
			division_result = list_3[0] / list_3[1]
			total_list.append(division_result)
	for numbers in total_list:
		try:
			total += numbers
		except TypeError:
			total = "Invalid Input"
			value_error = True
		except OverflowError:
			total = "Could Not Perform Operation"
			value_error = True
	isresult = True
	result_list.append(total)
	display.set(result_list[-1])


	 
def but_back(result_list, display):
	current_result = display.get()
	prev_result = result_list.index(current_result) -1
	prev_result = str(result_list[prev_result])
	display.set(prev_result)	


# widgets

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
frame = Frame(root, bg="#F29327")
label = Label(root, textvariabl=result_display ,bg="#ED491D", relief=GROOVE, bd=3)
button_1 = Button(root, text="1", bg="#101139", command=lambda: set_variable('1', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_2 = Button(root, text="2", bg="#101139", command=lambda: set_variable('2', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_3 = Button(root, text="3", bg="#101139", command=lambda: set_variable('3', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_4 = Button(root, text="4", bg="#101139", command=lambda: set_variable('4', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_5 = Button(root, text="5", bg="#101139", command=lambda: set_variable('5', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_6 = Button(root, text="6", bg="#101139", command=lambda: set_variable('6', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_7 = Button(root, text="7", bg="#101139", command=lambda: set_variable('7', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_8 = Button(root, text="8", bg="#101139", command=lambda: set_variable('8', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_9 = Button(root, text="9", bg="#101139", command=lambda: set_variable('9', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_0 = Button(root, text="0", bg="#101139", command=lambda: set_variable('0', after_equal, result_display, value_error, result), fg="#C8C8D3")
button_pi = Button(root, text="π",bg="#101139", command=lambda: set_variable("π", after_equal, result_display, value_error, result), fg="#C8C8D3")
button_dot = Button(root, text=".", bg="#101139", command=lambda: set_variable(".", after_equal, result_display, value_error, result), fg="#C8C8D3")
button_add = Button(root, text="+", bg="#1F849A", command=lambda: set_variable("+", after_equal, result_display, value_error, result))
button_subtract = Button(root, text="-", bg="#1F849A", command=lambda: set_variable("-", after_equal, result_display, value_error, result))
button_multiply = Button(root, text="*", bg="#1F849A", command=lambda: set_variable("*", after_equal, result_display, value_error, result))
button_divide = Button(root, text="/", bg="#1F849A", command=lambda: set_variable("/", after_equal, result_display, value_error, result))
button_cos = Button(root, text="Cos(", bg="#1F849A", command=lambda: set_variable("Cos(", after_equal, result_display, value_error, result))
button_sin = Button(root, text="Sin(", bg="#1F849A", command=lambda: set_variable("Sin(", after_equal, result_display, value_error, result))
button_tan = Button(root, text="Tan(", bg="#1F849A", command=lambda: set_variable("Tan(", after_equal, result_display, value_error, result))
button_back = Button(root, text="Back", bg="#B58DC3", command=lambda: but_back(result, result_display))
button_clear = Button(root, text="Clear", bg="#B58DC3", command=lambda: clear_result(result))
button_space = Button(root, text="Space", bg="#B58DC3", command=lambda: set_variable(" ", after_equal, result_display, value_error, result))
button_equal = Button(root, text="=", bg="#1DA1ED", command=lambda: equal_func(result_display, after_equal, result, value_error))
button_sqrroot = Button(root, text="√", bg="#1F849A", command=lambda: set_variable("√", after_equal, result_display, value_error, result))
button_power = Button(root, text="^", bg="#1F849A", command=lambda: set_variable("^", after_equal, result_display, value_error, result))
button_bracket = Button(root, text="Abs(", bg="#1F849A", command=lambda: set_variable("Abs(", after_equal, result_display, value_error, result))
button_abs = Button(root, text=")", bg="#1F849A", command=lambda: set_variable(")", after_equal, result_display, value_error, result))


# position of each widget in program
canvas.pack()
frame.place(relx=0.01, rely= 0.01, relwidth=0.98, relheight=0.98)
button_1.place(relx=0.02, rely= 0.88, relwidth=0.24, relheight=0.10)
button_2.place(relx=0.26, rely= 0.88, relwidth=0.24, relheight=0.10)
button_3.place(relx=0.50, rely= 0.88, relwidth=0.24, relheight=0.10)
button_equal.place(relx=0.74, rely= 0.88, relwidth=0.24, relheight=0.10) 
button_4.place(relx=0.02, rely= 0.78, relwidth=0.24, relheight=0.10) 
button_5.place(relx=0.26, rely= 0.78, relwidth=0.24, relheight=0.10) 
button_6.place(relx=0.50, rely= 0.78, relwidth=0.24, relheight=0.10)
button_add.place(relx=0.74, rely= 0.78, relwidth=0.24, relheight=0.10)
button_7.place(relx=0.02, rely= 0.68, relwidth=0.24, relheight=0.10) 
button_8.place(relx=0.26, rely= 0.68, relwidth=0.24, relheight=0.10)
button_9.place(relx=0.50, rely= 0.68, relwidth=0.24, relheight=0.10) 
button_subtract.place(relx=0.74, rely= 0.68, relwidth=0.24, relheight=0.10)
button_pi.place(relx=0.02, rely= 0.58, relwidth=0.24, relheight=0.10)
button_0.place(relx=0.26, rely= 0.58, relwidth=0.24, relheight=0.10)
button_dot.place(relx=0.50, rely= 0.58, relwidth=0.24, relheight=0.10)
button_multiply.place(relx=0.74, rely= 0.48, relwidth=0.24, relheight=0.10)
button_divide.place(relx=0.74, rely= 0.58, relwidth=0.24, relheight=0.10)
button_sqrroot.place(relx=0.02, rely= 0.48, relwidth=0.24, relheight=0.10)
button_power.place(relx=0.26, rely= 0.48, relwidth=0.24, relheight=0.10)
button_abs.place(relx=0.50, rely= 0.48, relwidth=0.24, relheight=0.10)
button_cos.place(relx=0.02, rely= 0.38, relwidth=0.24, relheight=0.10)
button_sin.place(relx=0.26, rely= 0.38, relwidth=0.24, relheight=0.10)
button_tan.place(relx=0.50, rely= 0.38, relwidth=0.24, relheight=0.10)
button_bracket.place(relx=0.74, rely= 0.38, relwidth=0.24, relheight=0.10)
button_back.place(relx=0.02, rely= 0.28, relwidth=0.32, relheight=0.10)
button_clear.place(relx=0.34, rely= 0.28, relwidth=0.32, relheight=0.10)
button_space.place(relx=0.66, rely= 0.28, relwidth=0.32, relheight=0.10)
label.place(relx=0.02, rely= 0.02, relwidth=0.96, relheight=0.26)


root.mainloop()
