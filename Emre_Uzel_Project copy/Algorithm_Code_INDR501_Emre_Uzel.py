#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import sys as sys
import tkinter as tk


# In[19]:


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


# In[20]:


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


# In[22]:


# You can comment here and initialize like  in the below cell. If you find it complicated.

V = int(input("Enter the number of variables:")) 
C = []
for i in range(V):
    C.append(int(input('Please Enter C values respectively: ')))
print('C values are as follows: ' , C)
A = []
for i in range(V):
    for i in range(3):
        A.append(int(input('Please Enter A values(row wise): ')))

A = np.array(A)

if V > 1:
    A = A.reshape(3,V)
elif V ==1:
    A= A.reshape(3,1)
    
b= []
for i in range(3):
    b.append(int(input('Please Enter b values respectively: ')))
    
equ_cons =[]
for i in range(3):
    equ_cons.append(input("Please Enter equality constraints respectively ('=' or '>='  or '<='): "))


# In[23]:


## Algoritm Code Implementation by Emre_Uzel
## In this step we look at if we need to add any artificial variables,
## If yes, we add them to code and do row operations 
## to have initial B to make problem ready for revised simplex
## You can just change C , A and b values and implement algorithm to see the results

#C = [5, 2, 9]
#A = [[2,4,1],
#     [3,3,1],
#     [-1,5,1]]


x_vars= []
for i in range(len(C)):
    x_vars.append('x' + str(i+1))




#b = [150, 90, 120]
initial_solution = 0
#equ_cons = ['<=', '<=', '>=']
M=100
count_s = 0

count_big = []# Count of >= constraints
count_eq = []# Count of = constraints
count_low = []# Count of <= constraints

for i in range(len(equ_cons)):
    if equ_cons[i] == '=':
        count_s += 1
        count_eq.append(i)
    elif equ_cons[i] == '>=':
        count_s += 2
        count_big.append(i)
    elif equ_cons[i] == '<=':
        count_s += 1
        count_low.append(i)


# In[26]:


s_vars = []
for i in range(count_s):
    s_vars.append('s' + str(i+1))
s_vars


# In[27]:


add_A =np.zeros((3,count_s))
add_C = np.zeros((count_s))


# In[28]:


# Determining positions of Slack and Artifical Variable to add first problem.

if len(count_big) == 3:
    for i in (count_big):
        if i == 0:
            add_A[i,0] = -1
            add_A[i,3] =  1
            add_C[0] = 0
            add_C[3] = -M
        elif i == 1:
            add_A[i,1] = -1
            add_A[i,4] =  1
            add_C[1] = 0
            add_C[4] = -M
        elif i == 2:
            add_A[i,2] = -1
            add_A[i,5] =  1
            add_C[2] = 0
            add_C[5] = -M
            
if len(count_big) == 2:
    if count_big == [0,1]:
        add_A[0,0] = -1
        add_C[0] = 0
        add_A[0,2] =  1
        add_C[2] = -M
        add_A[1,1] = -1
        add_C[1] = 0
        add_A[1,3] =  1
        add_C[3] = -M
        add_A[2,4] = 1
        if count_eq == [2]:
            add_C[4] = -M
        elif count_low == [2]:
            add_C[4] = 0
            
    elif count_big == [0,2]:
        add_A[0,0] = -1
        add_C[0] = 0
        add_A[0,2] =  1
        add_C[2] = -M
        if count_eq == [1]:
            add_A[1,3] = 1
            add_C[3] = -M
        elif count_low == [1]:
            add_A[1,3] = 1
            add_C[3] = 0
        add_A[2,1] = -1
        add_C[1] = 0
        add_A[2,4] =  1
        add_C[4] = -M
        
    elif count_big == [1,2]:
        if count_eq == [0]:
            add_A[0,2] = 1
            add_C[2] = -M
        elif count_low == [0]:
            add_A[0,2] = 1
            add_C[2] = 0
        add_A[1,0] = -1
        add_C[0] = 0
        add_A[1,3] =  1
        add_C[3] = -M
        add_A[2,1] = -1
        add_C[1] = 0
        add_A[2,4] =  1
        add_C[4] = -M
        
if len(count_big) == 1:
    if count_big == [0]:
        add_A[0,0] = -1
        add_A[0,1] =  1
        add_C[0] = 0
        add_C[1] = -M
        if count_eq == [1,2]:
            add_A[1,2] = 1
            add_A[2,3] = 1
            add_C[2] = -M
            add_C[3] = -M
        elif count_low == [1,2]:
            add_A[1,2] = 1
            add_A[2,3] = 1
            add_C[2] = 0
            add_C[3] = 0
            
    if count_big == [1]:
        add_A[1,0] = -1
        add_A[1,2] =  1
        add_C[0] = 0
        add_C[2] = -M
        if count_eq == [0,2]:
            add_A[0,1] = 1
            add_A[2,3] = 1
            add_C[1] = -M
            add_C[3] = -M
        elif count_low == [0,2]:
            add_A[0,1] = 1
            add_A[2,3] = 1
            add_C[1] = 0
            add_C[3] = 0
            
    if count_big == [2]:
        add_A[2,0] = -1
        add_A[2,3] =  1
        add_C[0] = 0
        add_C[3] = -M
        if count_eq == [0,1]:
            add_A[0,1] = 1
            add_A[1,2] = 1
            add_C[1] = -M
            add_C[2] = -M
        elif count_low == [0,1]:
            add_A[0,1] = 1
            add_A[1,2] = 1
            add_C[1] = 0
            add_C[2] = 0
        


# In[29]:


# Addition of Slack and Artifical Variables to add first problem.
new_C= np.append(C, add_C)
new_A = np.concatenate((A,add_A), axis =1)


# In[32]:


## Row operations to get first shape before revised simplex

min_val = np.min(new_C)
arg_mins= []
for i in range(len(new_C)):
    if new_C[i] == min_val:
        arg_mins.append(i)
        

for i in arg_mins:
    if list(new_A[:,i]) == [1, 0, 0]:
        print('First')
        new_C += new_A[0,:] * (- min_val)
        initial_solution += b[0] * (- min_val)
    elif list(new_A[:,i]) == [0, 1, 0]:
        print('Second')
        new_C += new_A[1,:] * (- min_val)
        initial_solution += b[1] * (- min_val)
    elif list(new_A[:,i]) == [0, 0, 1]:
        print('Third')
        new_C += new_A[2,:] * (- min_val)        
        initial_solution += b[2] * (- min_val)


# In[38]:


non_basis_vars = np.append(x_vars, s_vars[:-3])


# In[42]:


#Iteration 0 for revised simplex method.
#we get standard form of the variables.
c = new_C
A = new_A
z= 0
b = np.array(b)
b = b.reshape(3,1)
C_n = []
N_C = []
count_slack = 0
count_x = 0

basis_vars = s_vars[-3:].copy()

for i in range(len(c)):
    if c[i] == 0:
        count_slack+= 1
    else: 
        count_x += 1
        C_n.append(c[i])
        N_C.append(A[:,i])


     
C_n = np.array(C_n)
C_nx = np.arange(1, count_x +1)

B = np.identity(count_slack)

B_inv = np.linalg.inv(B)

C_b = np.zeros(count_slack)
C_bx = np.arange(1, count_slack+1)

X_b = np.matmul(B_inv, b)

z = np.matmul(np.matmul(C_b, B_inv), b)

N_C = np.vstack(N_C)
N_C = N_C.T

N_B = B


# In[43]:


while True:
    
    print('C_b is', C_b)
    print('C_n is', C_n)
    
    
    w = np.matmul(C_b, B_inv)
    red_costs = np.matmul(w, N_C) - C_n
    
    opt_check(C_b, B_inv, N_C, C_n, initial_solution)
    
    sel_cost = np.min(red_costs)
    entering_variable = red_costs.argmin()
    y = np.matmul(B_inv, A[:,entering_variable])
    y = y.reshape(3,1)
    if np.max(X_b)< 0:
        print('There is infeasible solution. All right hand side values are negative.')
        sys.exit()

    pos_leav_vars = (X_b / y) # unbounded or infeasible
    if np.max(pos_leav_vars) <0:
        print("There is unbounded solution. So we can't continue iterating.")
    
    for i in range(len(pos_leav_vars)):
        if pos_leav_vars[i] <= 0:
            pos_leav_vars[i] = 100000
    leav_var = np.argmin(pos_leav_vars)
    
    
    E = find_E(y,leav_var, entering_variable)
    B_inv = np.matmul(E, B_inv)
    print('The new B inverse is i' , B_inv, '\n')
    
    C_b[leav_var] = C_n[entering_variable]
    C_n[entering_variable] = 0
    tempx = non_basis_vars[entering_variable].copy()
    non_basis_vars[entering_variable] = basis_vars[leav_var]
    basis_vars[leav_var] = tempx
    
    X_b = np.matmul(B_inv, b)
    z = np.matmul(np.matmul(C_b, B_inv), b)
    print('For this iteration,  basis variables and basic feasible solution as follows: ')
    print('Z is ', z - initial_solution )
    print('Basis variables are ', basis_vars, 'and their values are respectively,', X_b.T)
    temp = N_C[:,entering_variable].copy()
    N_C[:,entering_variable] = N_B[:,leav_var]
    N_B[:,leav_var] = temp
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




