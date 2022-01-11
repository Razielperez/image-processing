import io
import os
import PySimpleGUI as sg
from clearColor import clearColor
from camScanner import camScanner
from Panorama import panorama
from PIL import Image
from pathlib import Path

size_of_image = (1000, 660)
def update_image(image_element, filename,size=size_of_image):
    if not Path(filename).is_file():
        return
    try:
        im = Image.open(filename)
    except:
        return
    width, height = size
    scale = max(im.width/width, im.height/height)

    if scale > 1:
        w, h = int(im.width/scale), int(im.height/scale)
        im = im.resize((w, h), resample=Image.CUBIC)

    with io.BytesIO() as output:
        im.save(output, format="PNG")
        data = output.getvalue()
    image_element.update(data=data)

def camScannerApp():
    sg.theme('DarkGrey2')
    layout = [
        [
            sg.Image(key="-IMAGE-",size=size_of_image,expand_x=True, expand_y=True)
        ],

        [
            sg.Text("Image File",font=("Ariel", 20)),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.Button('Browse',font=("Ariel", 12))
        ],

        [
            sg.Button("camScanner",font=("Ariel", 12))
        ]

    ]
    window = sg.Window('CamScanner App', layout,finalize=True)
    update_image(window['-IMAGE-'], 'example/clear color/image.png')

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Browse":
            filename = sg.popup_get_file("", no_window=True)
            if filename:
                update_image(window['-IMAGE-'], filename)
                window['-FILE-'].update(filename)

        if event == "camScanner":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                newFilename=camScanner(filename)
                update_image(window['-IMAGE-'], newFilename)

    window.close()

def clearColorApp():
    file_types = [("JPEG (*.jpg)", "*.jpg"),
                 ("All files (*.*)", "*.*")]
    colors=['yellow','blue','red','green','cyan','violet','gray','black','white']
    layout = [
        [
            sg.Image(key="-IMAGE-",size=size_of_image,expand_x=True, expand_y=True)
        ],

        [
            sg.Text("Image File",font=("Ariel", 20)),
            sg.Input(size=(25, 20), key="-FILE-"),
            sg.Button('Browse',font=("Ariel", 12))
        ],

        [
            sg.Text("color",font=("Ariel", 20)),
            sg.Listbox(colors,size=(10,7),disabled=False,key='-LISTBOX-',select_mode='multiple',font=("Ariel", 12))

        ],

        [
            sg.Button("clear color",font=("Ariel", 12))
        ]

    ]
    window = sg.Window("Clear Color App", layout,finalize=True)
    update_image(window['-IMAGE-'], 'example/clear color/image.png')
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Browse":
            filename = sg.popup_get_file("", no_window=True)
            if filename:
                update_image(window['-IMAGE-'], filename)
                window['-FILE-'].update(filename)
        if event == "clear color":
            filename = values["-FILE-"]
            colors=values["-LISTBOX-"]
            if os.path.exists(filename)and colors:
                newFilename=clearColor(filename,colors)
                update_image(window['-IMAGE-'], newFilename)

    window.close()

def panoramaApp():
    file_types = [("JPEG (*.jpg)", "*.jpg"),
                 ("All files (*.*)", "*.*")]

    layout = [
        [
            sg.Image(key="-IMAGE_LEFT-", size=(500,330), expand_x=True, expand_y=True),
            sg.Image(key="-IMAGE_RIGHT-", size=(500,330), expand_x=True, expand_y=True)

        ],

        [
            sg.Text("Image left File",font=("Ariel", 20)),
            sg.Input(size=(25, 40), key="-FILE_LEFT-"),
            sg.Button('Browse1', font=("Ariel", 12))

        ],

        [
            sg.Text("Image right File",font=("Ariel", 20)),
            sg.Input(size=(25, 40), key="-FILE_RIGHT-"),
            sg.Button('Browse2', font=("Ariel", 12))


        ],

        [
            sg.Button("panorama",font=("Ariel", 12))
        ]

    ]
    window = sg.Window("Panorama App", layout,finalize=True)
    update_image(window['-IMAGE_LEFT-'], 'example/clear color/image.png')
    update_image(window['-IMAGE_RIGHT-'], '.example/clear color/image.png')
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Browse1":
            filename = sg.popup_get_file("", no_window=True)
            if filename:
                update_image(window['-IMAGE_LEFT-'], filename,(500, 330))
                window['-FILE_LEFT-'].update(filename)

        if event == "Browse2":
            filename = sg.popup_get_file("", no_window=True)
            if filename:
                update_image(window['-IMAGE_RIGHT-'], filename,(500, 330))
                window['-FILE_RIGHT-'].update(filename)


        if event == "panorama":
            filenameLeft = values["-FILE_LEFT-"]
            filenameRight = values["-FILE_RIGHT-"]
            if os.path.exists(filenameLeft)and os.path.exists(filenameRight):
                newFilename=panorama(filenameLeft,filenameRight)
                window['-IMAGE_RIGHT-'].update(size=size_of_image)
                window['-IMAGE_LEFT-'].update('')
                update_image(window['-IMAGE_RIGHT-'], newFilename)

    window.close()

def init():
    if not os.path.exists('./output'):
        os.makedirs('./output')

def homePage():
    init()
    sg.theme('DarkGrey2')

    layout = [
        [
            sg.Text("\n\nWelcome to my area\n\n",font=("CASTELLAR", 28),justification='center', pad=(650, 0))
        ],

        [
            sg.Text('The features we have here:\n',font=("MingLiU_HKSCS-ExtB", 20))

        ],
        [
            sg.Text('1) clear color - Does color bother you in the picture? This is not a problem just select it and we will remove it from your image\n',font=("MingLiU_HKSCS-ExtB", 20))
        ],
        [
            sg.Text('2) camScanner- Do you have a photo that contains a document and only it interests you? Let us do the work for you!\n',font=("MingLiU_HKSCS-ExtB", 20))
        ],
        [
            sg.Text('3) panorama - Do you have a pair of photos that contain a common area? Let us turn them into one perfect panorama for you!\n\n\n',font=("MingLiU_HKSCS-ExtB", 20))
        ],
        # [
        #     sg.Text('4) for next app- bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla\n\n\n',font=("MingLiU_HKSCS-ExtB", 20))
        # ],


        [
            sg.Button("clear color",font=("Ariel", 20),pad=((540,50), 0)),
            sg.Button("camScanner",font=("Ariel", 20),pad=(50, 0)),
            sg.Button("panorama",font=("Ariel", 20),pad=(50, 0))
            #sg.Button("next app",font=("Ariel", 20),pad=(50, 0))
        ],
        [
            sg.Text('\n\n\n',font=("Luxurious Roman", 10))
        ],
    ]
    window = sg.Window('Image processing by Raziel Peretz', layout,grab_anywhere=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "clear color":
            clearColorApp()
        elif event == "camScanner":
            camScannerApp()
        elif event == "panorama":
            panoramaApp()
        # elif event == "next app":
        #     continue
    window.close()


homePage()
