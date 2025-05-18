from tkinter import *
from tkinter import messagebox
root = Tk()

root ['bg'] = '#fafafa'
root.title('Кафе мороженного')
root.geometry('1280x720')
root.resizable(width = False, height = False)


canvas = Canvas(root, height=1280, width=720)
canvas.pack()

frame = Frame(root, bg = '#fafafa', bd = 5)
frame.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.7)



class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        if self.flavors:
            print("В наличии следующие сорта мороженого:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        else:
            print("К сожалению, в наличии пока нет сортов мороженого.")

Ice1 = IceCreamStand('опа', 'мороженное')
Ice1.flavors = ['Шоколадное','Ванильное','фруктовый лед','Аче']
def btn_click():
    str_fl = str(Ice1.flavors)
    messagebox.showinfo(title='ассортимент', message= str_fl)
btn = Button(frame, text = 'Узнать ассортимент', bg = 'white', command= btn_click)
btn.pack()

root.mainloop()

