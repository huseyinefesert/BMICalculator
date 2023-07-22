import tkinter

height = 0
weight = 0
result = 0
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=500,height=500)

kgLabel = tkinter.Label(text="Enter your weight (kg)")
kgLabel.pack()

kgEntry = tkinter.Entry()
kgEntry.pack()

cmLabel = tkinter.Label(text="Enter your height (cm)")
cmLabel.pack()

cmEntry = tkinter.Entry()
cmEntry.pack()
result_label = tkinter.Label()
def take_input():
    global height
    global weight
    global result
    try:
        height = (int)(cmEntry.get())
        weight = (int)(kgEntry.get())
        result = weight / ((height/100) * (height/100))
        result = round(result,1)
        if result < 18.5:
            result_label.config(text=f"Your BMI is {result}. You are Underweight")
        elif result>=18.5 and result<25:
            result_label.config(text=f"Your BMI is {result}. You are Normal")
        elif result>=25 and result<30:
            result_label.config(text=f"Your BMI is {result}. You are Overweight")
        else:
            result_label.config(text=f"Your BMI is {result}. You are Obesity")
        result_label.pack()
    except:
        print("Please enter valid numbers!!!")
button = tkinter.Button(text="Calculate", command=take_input)
button.pack()

window.mainloop()
