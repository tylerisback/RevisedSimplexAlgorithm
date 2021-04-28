import tkinter as tk
from tkinter import Grid, ttk
from tkinter import font
from tkinter.constants import BOTH, X
import numpy as np
import sys 

#Tkinter GUI Implementation. You don't need to setup anything as tkinter package comes as default.
#Implementation by Emre Uzel
#GUI Part
#Function for optimality Check
def opt_check(C_b, B_inv, N_C, C_n, initial_solution):
    w = np.matmul(C_b, B_inv)
    red_costs = np.matmul(w, N_C) - C_n
    
    neg_count = 0
    for i in range(len(red_costs)):
        if red_costs[i] <  0:
            neg_count +=1

    if neg_count == 0 :
        print('We reached an optimum solution.', '\n')
        print('The B inverse is', B_inv , '\n')
        print('The solution is', z - initial_solution , '\n')
        print('Basis variables are ', basis_vars, 'and their values are respectively', X_b.T)
        sys.exit()
    else:
        print("We haven't reached an optimal solution. Continue iterating.")
#Function to find E
def find_E(y,i, entering_variable):
    new_A = np.zeros(len(y))
    pivot = y[i]
    for j in range(len(y)):
        if j == i:
            new_A[j] =  1 / pivot
        else:
            new_A[j] =  - y[j] / pivot
    E = np.identity(count_slack)
    E[:, i] = new_A
    return E


root = tk.Tk()

root.title('Linear Programming')

root.geometry("800x600")
root.resizable(False, False)



main = ttk.Frame(root)
main.columnconfigure(0, weight = 1)
main.grid(row= 0 ,column =0, sticky= 'EW')

label1 = ttk.Label(main, background= 'yellow', font='Helvetica', text = 'Welcome to our program! The aim of this program is to find optimal solution to a problem specified by user.', padding =5,foreground='blue').grid(row = 0, column = 0, sticky= 'EW', )
label2 = ttk.Label(main,font='Helvetica',  text = 'The program accepts 3 constraints and you can specificy if the equality constraint is  = or >= or <= on the program.', padding =5, ).grid(row = 1, column = 0, sticky= 'EW')
label3 = ttk.Label(main,font='Helvetica', text = 'This program accepts maximization problems therefore you need to convert the problem to maximization problem.', padding =5, ).grid(row = 2, column = 0, sticky= 'EW')
label4 = ttk.Label(main,font='Helvetica', text = 'As you can see below, you need to input c , A , b values to the program and select equality constraints.', padding =5, ).grid(row = 3, column = 0, sticky= 'EW')
label5 = ttk.Label(main,font='Helvetica', text = 'After that results will be printed on the window. If you have only 3 x variables then left x4 to x10 empty. Do not fill with 0.', padding =5, ).grid(row = 4, column = 0, sticky= 'EW')
label6 = ttk.Label(main,font='Helvetica', text = '', padding =5, ).grid(row = 5, column = 0, sticky= 'EW')
label7 = ttk.Label(main,font='Helvetica', text = '                                                  x1      x2      x3      x4      x5      x6      x7      x8      x9      x10                 Solution', padding =5, ).grid(row = 6, column = 0, sticky= 'EW')

valuess = ttk.Frame(root, )
valuess.grid(row= 1 ,column =0, sticky= 'EW', )

#######################
#Objective Function values Start
#######################


c1 = tk.StringVar()
label8 = ttk.Label(valuess,  font='Helvetica', text = ' Objective Function Values: ', padding =5, ).grid(row = 0, column = 0, padx = (0,10) )
name_entry = ttk.Entry(valuess, width = 2, textvariable= c1)
name_entry.grid(row = 0, column = 1)

c2 = tk.StringVar()
name_entry2 = ttk.Entry(valuess, width = 2,textvariable=c2)
name_entry2.grid(row = 0, column = 2, padx =12)

c3 = tk.StringVar()
name_entry3 = ttk.Entry(valuess, width = 2, textvariable= c3)
name_entry3.grid(row = 0, column = 3,)

c4 = tk.StringVar()
name_entry4 = ttk.Entry(valuess, width = 2, textvariable= c4)
name_entry4.grid(row = 0, column = 4, padx =8.5)

c5 = tk.StringVar()
name_entry5 = ttk.Entry(valuess, width = 2, textvariable= c5)
name_entry5.grid(row = 0, column = 5, padx =3)

c6 = tk.StringVar()
name_entry6 = ttk.Entry(valuess, width = 2, textvariable= c6)
name_entry6.grid(row = 0, column = 6, padx =5)

c7 = tk.StringVar()
name_entry7 = ttk.Entry(valuess, width = 2, textvariable= c7)
name_entry7.grid(row = 0, column = 7, padx =8)

c8 = tk.StringVar()
name_entry8 = ttk.Entry(valuess, width = 2, textvariable= c8)
name_entry8.grid(row = 0, column = 8, padx =3)

c9 = tk.StringVar()
name_entry9 = ttk.Entry(valuess, width = 2, textvariable= c9)
name_entry9.grid(row = 0, column = 9, padx =6)

c10 = tk.StringVar()
name_entry10 = ttk.Entry(valuess, width = 2, textvariable= c10)
name_entry10.grid(row = 0, column = 10, padx =7)





#######################
#Constraints 1
#######################

x1_1 = tk.StringVar()
label8 = ttk.Label(valuess,  font='Helvetica', text = ' Constraint 1 values: ', padding =5, ).grid(row = 1, column = 0, padx = (0,10) )
name_entry = ttk.Entry(valuess, width = 2, textvariable= x1_1)
name_entry.grid(row = 1, column = 1)


x1_2 = tk.StringVar()
name_entry2 = ttk.Entry(valuess, width = 2,textvariable= x1_2)
name_entry2.grid(row = 1, column = 2, padx =12)

x1_3 = tk.StringVar()
name_entry3 = ttk.Entry(valuess, width = 2, textvariable= x1_3)
name_entry3.grid(row = 1, column = 3,)

x1_4 = tk.StringVar()
name_entry4 = ttk.Entry(valuess, width = 2, textvariable= x1_4)
name_entry4.grid(row = 1, column = 4, padx =8.5)

x1_5 = tk.StringVar()
name_entry5 = ttk.Entry(valuess, width = 2, textvariable= x1_5)
name_entry5.grid(row = 1, column = 5, padx =3)

x1_6 = tk.StringVar()
name_entry6 = ttk.Entry(valuess, width = 2, textvariable= x1_6)
name_entry6.grid(row = 1, column = 6, padx =5)

x1_7 = tk.StringVar()
name_entry7 = ttk.Entry(valuess, width = 2, textvariable= x1_7)
name_entry7.grid(row = 1, column = 7, padx =8)

x1_8 = tk.StringVar()
name_entry8 = ttk.Entry(valuess, width = 2, textvariable= x1_8)
name_entry8.grid(row = 1, column = 8, padx =3)

x1_9 = tk.StringVar()
name_entry9 = ttk.Entry(valuess, width = 2, textvariable= x1_9)
name_entry9.grid(row = 1, column = 9, padx =6)

x1_10 = tk.StringVar()
name_entry10 = ttk.Entry(valuess, width = 2, textvariable= x1_10)
name_entry10.grid(row = 1, column = 10, padx =7)

equ1 = tk.StringVar()
equ_cons = ttk.Combobox(valuess, width=2, textvariable= equ1)
equ_cons['values'] = ('<=' , '=', '>=')
equ_cons['state'] = 'readonly'
equ_cons.grid(row = 1, column = 11, padx = 5)

sol_2 = tk.StringVar()
name_entry11 = ttk.Entry(valuess, width = 5, textvariable= sol_2)
name_entry11.grid(row = 1, column = 12, padx =10)

#######################
#Constraints 2
#######################

x2_1 = tk.StringVar()
label8 = ttk.Label(valuess,  font='Helvetica', text = ' Constraint 2 values: ', padding =5, ).grid(row = 2, column = 0, padx = (0,10) )
name_entry = ttk.Entry(valuess, width = 2, textvariable= x2_1)
name_entry.grid(row = 2, column = 1)


x2_2 = tk.StringVar()
name_entry2 = ttk.Entry(valuess, width = 2,textvariable= x2_2)
name_entry2.grid(row = 2, column = 2, padx =12)

x2_3 = tk.StringVar()
name_entry3 = ttk.Entry(valuess, width = 2, textvariable= x2_3)
name_entry3.grid(row = 2, column = 3,)

x2_4 = tk.StringVar()
name_entry4 = ttk.Entry(valuess, width = 2, textvariable= x2_4)
name_entry4.grid(row = 2, column = 4, padx =8.5)

x2_5 = tk.StringVar()
name_entry5 = ttk.Entry(valuess, width = 2, textvariable= x2_5)
name_entry5.grid(row = 2, column = 5, padx =3)

x2_6 = tk.StringVar()
name_entry6 = ttk.Entry(valuess, width = 2, textvariable= x2_6)
name_entry6.grid(row = 2, column = 6, padx =5)

x2_7 = tk.StringVar()
name_entry7 = ttk.Entry(valuess, width = 2, textvariable= x2_7)
name_entry7.grid(row = 2, column = 7, padx =8)

x2_8 = tk.StringVar()
name_entry8 = ttk.Entry(valuess, width = 2, textvariable= x2_8)
name_entry8.grid(row = 2, column = 8, padx =3)

x2_9 = tk.StringVar()
name_entry9 = ttk.Entry(valuess, width = 2, textvariable= x2_9)
name_entry9.grid(row = 2, column = 9, padx =6)

x2_10 = tk.StringVar()
name_entry10 = ttk.Entry(valuess, width = 2, textvariable= x2_10)
name_entry10.grid(row = 2, column = 10, padx =7)

equ2 = tk.StringVar()
equ_cons = ttk.Combobox(valuess, width=2, textvariable= equ2)
equ_cons['values'] = ('<=' , '=', '>=')
equ_cons['state'] = 'readonly'
equ_cons.grid(row = 2, column = 11, padx = 5)

sol_3 = tk.StringVar()
name_entry11 = ttk.Entry(valuess, width = 5, textvariable= sol_3)
name_entry11.grid(row = 2, column = 12, padx =10)

#######################
#Constraints 3
#######################

x3_1 = tk.StringVar()
label8 = ttk.Label(valuess,  font='Helvetica', text = ' Constraint 3 values: ', padding =5, ).grid(row = 3, column = 0, padx = (0,10) )
name_entry = ttk.Entry(valuess, width = 2, textvariable= x3_1)
name_entry.grid(row = 3, column = 1)


x3_2 = tk.StringVar()
name_entry2 = ttk.Entry(valuess, width = 2,textvariable= x3_2)
name_entry2.grid(row = 3, column = 2, padx =12)

x3_3 = tk.StringVar()
name_entry3 = ttk.Entry(valuess, width = 2, textvariable= x3_3)
name_entry3.grid(row = 3, column = 3,)

x3_4 = tk.StringVar()
name_entry4 = ttk.Entry(valuess, width = 2, textvariable= x3_4)
name_entry4.grid(row = 3, column = 4, padx =8.5)

x3_5 = tk.StringVar()
name_entry5 = ttk.Entry(valuess, width = 2, textvariable= x3_5)
name_entry5.grid(row = 3, column = 5, padx =3)

x3_6 = tk.StringVar()
name_entry6 = ttk.Entry(valuess, width = 2, textvariable= x3_6)
name_entry6.grid(row = 3, column = 6, padx =5)

x3_7 = tk.StringVar()
name_entry7 = ttk.Entry(valuess, width = 2, textvariable= x3_7)
name_entry7.grid(row = 3, column = 7, padx =8)

x3_8 = tk.StringVar()
name_entry8 = ttk.Entry(valuess, width = 2, textvariable= x3_8)
name_entry8.grid(row = 3, column = 8, padx =3)

x3_9 = tk.StringVar()
name_entry9 = ttk.Entry(valuess, width = 2, textvariable= x3_9)
name_entry9.grid(row = 3, column = 9, padx =6)

x3_10 = tk.StringVar()
name_entry10 = ttk.Entry(valuess, width = 2, textvariable= x3_10)
name_entry10.grid(row = 3, column = 10, padx =7)

equ3 = tk.StringVar()
equ_cons = ttk.Combobox(valuess, width=2, textvariable= equ3)
equ_cons['values'] = ('<=' , '=', '>=')
equ_cons['state'] = 'readonly'
equ_cons.grid(row = 3, column = 11, padx = 5)

sol_4 = tk.StringVar()
name_entry12 = ttk.Entry(valuess, width = 5, textvariable= sol_4)
name_entry12.grid(row = 3, column = 12, padx =10)

########### 
# Button and Solution Finder
###########

global C
global A 
global b
 

C= []
A = []
b = []
equ_cons = []


def calc(C, A, b, equ_cons): 

    b.append(sol_2.get())
    b.append(sol_3.get())
    b.append(sol_4.get())
    b = np.array(b)

    C.append(c1.get())
    C.append(c2.get())
    C.append(c3.get())
    C.append(c4.get())
    C.append(c5.get())
    C.append(c6.get())
    C.append(c7.get())
    C.append(c8.get())
    C.append(c9.get())
    C.append(c10.get())
    C = np.array(C)

    A.append(x1_1.get())
    A.append(x1_2.get())
    A.append(x1_3.get())
    A.append(x1_4.get())
    A.append(x1_5.get())
    A.append(x1_6.get())
    A.append(x1_7.get())
    A.append(x1_8.get())
    A.append(x1_9.get())
    A.append(x1_10.get())


    A.append(x2_1.get())
    A.append(x2_2.get())
    A.append(x2_3.get())
    A.append(x2_4.get())
    A.append(x2_5.get())
    A.append(x2_6.get())
    A.append(x2_7.get())
    A.append(x2_8.get())
    A.append(x2_9.get())
    A.append(x2_10.get())


    A.append(x3_1.get())
    A.append(x3_2.get())
    A.append(x3_3.get())
    A.append(x3_4.get())
    A.append(x3_5.get())
    A.append(x3_6.get())
    A.append(x3_7.get())
    A.append(x3_8.get())
    A.append(x3_9.get())
    A.append(x3_10.get())

    equ_cons.append(equ1)
    equ_cons.append(equ2)
    equ_cons.append(equ3)

    A = np.array(A)
    A = A.reshape(3,10)

    print(A),
    print(C),
    print(b)
    print(equ_cons)
    return A, C, b, equ_cons




button_frame = ttk.Frame(root, padding= (20,20,20,20))
button_frame.grid(row = 2, column = 0, sticky = 'EW')

submit_but = ttk.Button(button_frame, text= 'Submit and Solve.', command = calc(C,A,b, equ_cons))
submit_but.grid(row = 4, column=0)

root.mainloop()



