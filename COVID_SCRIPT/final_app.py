import requests
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from PIL import ImageTk, Image


### First Function
def get_data(entry):
	page = 'https://www.mygov.in/corona-data/covid19-statewise-status'
	res = requests.get(page)
	source = res.text
	soup = BeautifulSoup(source,'html.parser')
	head_list = []
	head = soup.find_all('div',class_='field-label')[0:6]
	for x in head:
		head_list.append(x.text)
	cont_list = []
	for z in soup.find_all('div',class_='field-item even')[0:6]:
		cont_list.append(z.text)
	states_List = []
	head = soup.find_all('div',class_='field-label')[12:16]
	for x in head:
		states_List.append(x.text)
	temp = []
	for z in soup.find_all('div',class_='field-item even')[8:500]:
		temp.append(z.text.strip())

	clean = []
	for x in temp:
		clean.append(list(x.split('State Name')))

	clean_data = []
	for a in clean:
		clean_data.append(a[0])

	samp_data = []
	samp_data = ([x for x in clean_data if x])
	samp_data = [samp_data[i:i + 4] for i in range(0, len(samp_data), 4)]
	cols = ['State Name','Confirmed Cases','Cured/Discharged/Migrated','No of Deaths']
	df = pd.DataFrame(data=samp_data,columns=cols)
	df['State Name'] = df['State Name'].str.lower()

	# state_check(entry,df)
	capt= entry.replace(" ",'')
	capt = capt.lower()
	print(capt)

	for x,y,z,s in zip(df['State Name'],df['Confirmed Cases'],df['Cured/Discharged/Migrated'],df['No of Deaths']):
		if x == capt: 
			data = "State Name: {} \n Confirmed Cases: {} \n Cured/Discharged/Migrated {} \n No of Deaths: {}".format(x,y,z,s)
			lower_label['text'] = data
		# else:
		# 	lower_label['text'] =  "Enter correct spelling of states"
	
		





# def state_check(entry,df):
# 	print(entry)
# 	for x,y,z,s in zip(df['State Name'],df['Confirmed Cases'],df['Cured/Discharged/Migrated'],df['No of Deaths']):
# 		if x == entry:
# 			print("No of Confirmed Cases : {} " .format(y))
# 			print("No of Cured cases : {} " .format(z))
# 			print("No of Deaths: : {} " .format(s))


# corono_data,ind_head,ind_data = get_data()
# state_check('Delhi',corono_data)
# print(ind_data)


# root directory for the app
root = tk.Tk()

# Creating a standard canvas look
canvas = tk.Canvas(root,height=500,width=800)
canvas.pack()

#### backgrounf Image
bg_image = ImageTk.PhotoImage(Image.open("image.png"))
bg_label = tk.Label(root,image=bg_image)
bg_label.place(relwidth=1,relheight=1)

# Creating Frames
frame = tk.Frame(root,bg='#ffff4d',bd=10)
frame.place(relx=0.5,rely=0.1,relwidth=0.8,relheight=0.15,anchor='n')


### Creating Labels in Frames
label = tk.Label(frame,text='CORONA VIRUS LIVE STATUS UPDATE IN INDIA',bg='yellow')
label.place(relx=0,rely=0,relwidth=1,relheight=0.2)

#### Creating Entry in the Frames
entry = tk.Entry(frame,bg='white',font=50)
entry.place(relx=0.01,rely=0.45,relwidth=0.3,relheight=0.5)


# Creating Buttons
button = tk.Button(frame,text='Get Data',bg='#00e600',font=('Courier',12),command=lambda: get_data(entry.get()))
button.place(relx=0.35,rely=0.45,relwidth=0.15,relheight=0.5)

#### Creating a lower Frame
lower_frame = tk.Frame(root,bg='#ffff4d',bd=100)
lower_frame.place(relx=0.5,rely=0.3,relwidth=0.8,relheight=0.65,anchor='n')

lower_label = tk.Label(lower_frame,bg='#ffff4d',bd=10,font=('Courier',15),anchor='nw',justify='left')
lower_label.place(relwidth=1,relheight=1)


root.mainloop()





# print(ind_data)