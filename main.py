import tkinter as tk
import requests

# Не понял как делать поиск по id поэтому решил сделать по параметру posts





window = tk.Tk()
window.minsize(500,500)
entr = tk.Entry(
    window,
    fg="black",
    bg="white",
    font=("Arial Bold", 18),
    width=25)

label = tk.Label(
    window,
    fg="black",
    bg="white",
    font=("Arial Bold",20),
    width=40,
    height=20)
def get_info_from_entry():
    global entr
    global label
    if entr.get()!="":
        try:
            post_num=int(entr.get())
            answer=requests.get(f"https://jsonplaceholder.typicode.com/posts/",params=str(post_num))
            print(answer.json())
            label["text"]=answer.text
        except:
            print(entr.get())
            print("Error!")




label_info=tk.Label(window,text="Enter index:",fg="black",font=("Arial Bold",18))
label_info.grid(row=0,column=0)
entr.grid(row=1,column=0,columnspan=3,sticky="EW")
button_search=tk.Button(
    window,
    text="OK",
    fg="white",
    background="green",
    font=("Arial Bold",18),
    width=5,
    height=1,
    command=get_info_from_entry)
button_search.grid(row=1,column=5)
label.grid(row=3,column=0)


window.mainloop()