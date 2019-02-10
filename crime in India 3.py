import pandas as pd
import numpy as np
import matplotlib.pyplot as pt   
import plotly.graph_objs as go
import plotly.offline as ply
import tkinter       # importing all my modules


window = tkinter.Tk()


window.title("MURDER")

window.geometry('700x400')

# Defining all my Butttons and my Entries

lbl_state = tkinter.Label(window, text="State", bg="#a1dbcd")
lbl_state.config(height=2, width=10, font = ('italic bold', 20, 'underline italic'))


ent_state = tkinter.Entry(window)
ent_state.config(width = 10,font=("Calibri",20))


lbl_year = tkinter.Label(window, text="Year", bg="#a1dbcd")                                                                     ##By Siddharth Pathania
lbl_year.config(height=2, width=10, font = ('italic bold', 20, 'underline italic'))  

                      
ent_year = tkinter.Entry(window)
ent_year.config(width = 10,font=("Calibri",20))                             


state = ent_state.get()
year = ent_year.get()
######                              By Siddharth Pathania 



# Packing all my buttons 
lbl_state.pack()
ent_state.pack()
lbl_year.pack()
ent_year.pack()



# Funtion for reading the data

def State():

  # Getting the values inside the function
    state = ent_state.get()
    year = ent_year.get()
    state = state.upper()       #   To make it convenient for the user to input value of certain state without worrying about text.
    
    
  # Reading the data 
    data = pd.read_csv('01_District_wise_crimes_committed_IPC_2001_2012.csv')
    df = pd.DataFrame(data)
    total = df.loc[(df.STATE_UT == state)&(df.YEAR == int(year)),
                   ['STATE_UT','DISTRICT','YEAR','MURDER']]
    print(total.head())
    
    
  # Dropping the 'total' row in District which will give us better view of graph
    i = total[( total.DISTRICT == 'TOTAL')].index
    total = total.drop(i)
    print(total.head())
    
  # Plotting using plotly
    trace1 = go.Bar(x = total['DISTRICT'],
                y = total['MURDER'],
                name = 'Murder in: {}'.format(state))
    layout = dict(
        title = 'Murder in : {}'.format(state),
        xaxis = dict(title = 'District'),
        yaxis = dict(title = 'No. of people')
        )
    data = [trace1]
    fig = dict(data = data ,layout = layout)
    ply.plot(fig,filename = 'Murder in India DistrictWise in 2012.html')


    
#   Defining the button and giving function:- State as command
btn = tkinter.Button(window, text="Graph", command=State) 
btn.config(height=2, width=10, font = ('italic bold', 20, 'underline italic') )  


# packing the button
btn.pack()   
    

window.mainloop()





