from tkinter import *
import tkinter.font as font
root = Tk()
root.geometry("500x500")
label1 = Label(root)
label1.pack()
label1_list = []
myFont = font.Font(size=30)
myFont1 = font.Font(size=40)


def click_button1():
    label1_list.append(1)


def click_button2():
    label1_list.append(2)


def click_button3():
    label1_list.append(3)


def click_button4():
    label1_list.append(4)


def click_button5():
    label1_list.append(5)



def click_add_button():
    label1_list.append("+")


def click_subtract_button():
    label1_list.append("-")


def click_multiply_button():
    label1_list.append("*")


def click_button6():
    label1_list.append(6)


def click_button7():
    label1_list.append(7)


def click_button8():
    label1_list.append(8)


def click_button9():
    label1_list.append(9)


def convert_list_to_string():
    string1 = ""
    for i in label1_list:
        string1 += str(i)
    label1.configure(text=str(string1))
    global calculation
    calculation = list(str(string1).split(" "))
    calculation[0:] = string1


def compound_calculation():
    for num in label1_list:
        if num == "+":
            z = label1_list.index(num)
            var2 = label1_list[:z]
            var2_list = list(var2)
            var3 = [str(var) for var in var2_list]
            number1 = "".join(var3)
            var4 = label1_list[z:]
            var5 = [str(random_number) for random_number in var4]
            number2 = "".join(var5)
            answer = int(number1) + int(number2)
            label1_list.clear()
            label1_list.append(int(answer))
        if num == "-":
            b = label1_list.index(num)
            var6 = label1_list[:b]
            var6_list = list(var6)
            var7 = [str(random_number1) for random_number1 in var6_list]
            number3 = "".join(var7)
            var8 = label1_list[b:]
            var9 = [str(random_number2) for random_number2 in var8]
            number4 = int("".join(var9))
            answer1 = int(number3) + int(number4)
            print(answer1)
            label1_list.clear()
            label1_list.append(int(answer1))
        if num == "*":
            p = label1_list.index(num)
            var10 = label1_list[:p]
            var10_list = list(var10)
            var11 = [str(random_number3) for random_number3 in var10_list]
            var12 = "".join(var11)
            var13 = label1_list[p:]


button1 = Button(root, text="1", command=lambda: [click_button1(), convert_list_to_string()])
button1.place(x=150, y=90)
button2 = Button(root, text="2", command=lambda: [click_button2(), convert_list_to_string()])
button2.place(x=170, y=90)
button3 = Button(root, text="3", command=lambda: [click_button3(), convert_list_to_string()])
button3.place(x=190, y=90)
button4 = Button(root, text="4", command=lambda: [click_button4(), convert_list_to_string()])
button4.place(x=210, y=90)
button5 = Button(root, text="5", command=lambda: [click_button5(), convert_list_to_string()])
button5.place(x=150, y=110)
button6 = Button(root, text="6", command=lambda: [click_button6(), convert_list_to_string()])
button6.place(x=170, y=110)
button6 = Button(root, text="7", command=lambda: [click_button7(), convert_list_to_string()])
button6.place(x=190, y=110)
button7 = Button(root, text="8", command=lambda: [click_button8(), convert_list_to_string()])
button7.place(x=210, y=110)
button8 = Button(root, text="+", command=lambda: [click_add_button(), convert_list_to_string()])
button8.place(x=230, y=90)
button9 = Button(root, text="-", command=lambda: [click_subtract_button(), convert_list_to_string()])
button9.place(x=230, y=130)
button10 = Button(root, text="=", command=lambda: [compound_calculation(), convert_list_to_string()])
button10.place(x=230, y=170)
button8["font"] = myFont
button9["font"] = myFont1
button10["font"] = myFont
root.mainloop()
