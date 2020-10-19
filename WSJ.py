import tkinter as tk
import requests
import urllib.request as urllib
import json

print('Reason for this project was to: \n Read through an API\n Displaying part I wanted in an API\n Displaying all this on a GUI\n Making a Keyword finder within the APIs')

API = '41fef4ed44fa4b5589b074bbc9b8b6c8'
url = 'http://newsapi.org/v2/everything?domains=wsj.com&apiKey=41fef4ed44fa4b5589b074bbc9b8b6c8'
json_object = requests.get(url=url)
data = json_object.json()



Height = 700
Width = 900

def listToString(s):  
    str1 = " " 
    return (str1.join(s))

def get_title(entry):
    lst = []
    url_lst = []
    descrip_lst = []
    for i in data['articles']:
        titles = i['title'].split()
        urls = i['url']
        description = i['author']
        for x in titles:
            if entry.lower() in x.lower():
                str_title = listToString(titles)
                lst.append(str_title)
                url_lst.append(urls)
                descrip_lst.append(description)
    dictionary = zip(lst, url_lst)
    dictionary_two = zip(lst, descrip_lst)
    dict_url = dict(dictionary)
    dict_des = dict(dictionary_two)
    info_label = tk.Label(lower_frame, bg='#94b8b8')
    for key in dict_url:
        for key in dict_des:
            info_label['text'] = 'Title: ' + key + '\n\n' + 'URL: ' + dict_url[key] + '\n\n' + 'Author: ' + dict_des[key] + '\n'
        info_label.place(relx=.025, rely=.175, relwidth=.95, relheight=.8)
    # --------------------------------------------------------------------------
    # more_button = tk.Button(lower_frame, bg='grey',)




root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root, bg='black', bd=10)
frame.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#9999ff')
lower_frame.place(relx=.1, rely=.1, relwidth=.8, relheight=.8)

instruc = tk.Label(lower_frame, bg='#94b8b8', text='This is the Wall Street Journal news finder program.', font='Arial', fg='red')
instruc.place(relx=.15, rely=.01, relwidth=.7, relheight=.05)

entry = tk.Entry(lower_frame, bg='#94b8b8', text='Enter text here please: ', fg='Red', font='Arial')
entry.place(relx=.18, rely=.09, relwidth=.7, relheight=.05)

entry_label = tk.Label(lower_frame, bg='#94b8b8', text='Enter text: ', font='Arial', fg='red')
entry_label.place(relx=.01, rely=.09, relwidth=.15, relheight=.05)

button = tk.Button(lower_frame, bg='#94b8b8', text='Search', command=lambda: get_title(entry.get()))
button.place(relx=.89, rely=.09, relwidth=.1, relheight=.05)

info_label = tk.Label(lower_frame, bg='#94b8b8')
info_label.place(relx=.025, rely=.175, relwidth=.95, relheight=.8)


root.mainloop()

