from tkinter import *
from tkinter import ttk
from sorts.bubble_sort import bubble_sort
from sorts.selection_sort import selection_sort
from sorts.shell_sort import shell_sort
from sorts.insertion_sort import insertion_sort
from sorts.hoare_sort import quick_sort
from sorts.shaker_sort import shaker_sort
from sorts.gnome_sort import gnome_sort
from sorts.merge_sort import merge_sort
from sorts.heap_sort import heap_sort
from sorts.tim_sort import tim_sort
import random


COLOR_1 = '#56b389'
COLOR_2 = '#cab4ac'
COLOR_3 = '#b88689'

window = Tk()
window.title("Sorts Visualization")
window.maxsize(1000, 700)
window.config(bg=COLOR_3)

algorithm_name = StringVar()
algo_list = ['Bubble Sort',
             'Selection Sort',
             'Shell Sort',
             'Insertion Sort',
             'Hoare\'s Sort',
             'Shaker Sort',
             'Gnome Sort',
             'Merge Sort',
             'Heap Sort',
             'Timsort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow', 'No delay']

data = []
is_random = False
amount_of_nums = 35


def set_random():
    global is_random
    if is_random is False:
        is_random = True
    else:
        is_random = False


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]
    arr = colorArray
    colorArray = []
    for i in arr:
        if i == 'green':
            colorArray.append(COLOR_1)
        else:
            colorArray.append('yellow')
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline=COLOR_1)

    window.update_idletasks()


def generate():

    global data
    global is_random
    data = []
    if not is_random:
        data = [x for x in reversed(range(1, amount_of_nums))]
    else:
        for i in range(0, amount_of_nums):
            random_value = random.randint(1, amount_of_nums)
            data.append(random_value)

    drawData(data, ['green' for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    elif speed_menu.get() == 'Fast':
        return 0.001
    else:
        return 0


def set_scale(val):
    global amount_of_nums
    amount_of_nums = scale.get()


def sort():
    global data
    timeTick = set_speed()
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Shell Sort':
        shell_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Hoare\'s Sort':
        quick_sort(data, 0, len(data) - 1, drawData, timeTick)
    elif algo_menu.get() == 'Shaker Sort':
        shaker_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Gnome Sort':
        gnome_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Timsort':
        tim_sort(data, drawData, timeTick)


style = ttk.Style()
style.theme_use('alt')
style.map('custom.TCombobox', fieldbackground=[('readonly', COLOR_3)])
style.map('custom.TCombobox', foreground=[('readonly', COLOR_3)])

UI_frame = Frame(window, width=900, height=300, bg=COLOR_3)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=COLOR_3)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list, state='readonly')
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=COLOR_3)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame,
                          textvariable=speed_name,
                          values=speed_list,
                          state='readonly',
                          background=COLOR_3,
                          )
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

l3 = Label(UI_frame, text="Amount of numbers", bg=COLOR_3)
l3.grid(row=0, column=2, padx=10, pady=5)

scale = Scale(UI_frame, from_=35, to=800, command=set_scale, orient='horizontal', bg=COLOR_3)
scale.grid(row=1, column=2, padx=5, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg=COLOR_3, highlightbackground=COLOR_3)
b1.grid(row=2, column=1, padx=5, pady=5)

b2 = Checkbutton(UI_frame, text='Randomize Array', bg=COLOR_3, command=set_random, highlightbackground=COLOR_3)
b2.grid(row=2, column=2, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=COLOR_3, highlightbackground=COLOR_3)
b3.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg=COLOR_2)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
