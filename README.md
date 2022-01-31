# image-processing

This project is a system that presents some image processing operations.
This system is displayed by Peyton's GUI for user convenience
The main purpose of this project is to present the features found in it.

# The features in the system

## Clear color
In this featur we will remove colors from an image by the HSV model.
You can select several colors that we want to remove 
and thus we get an image that contains only the colors we want.

## Cam Scanner
In the featur we will make changes to an image by getting an image
that contains a document and the program will take the document and isolate it
from the rest of the image and it will be displayed in full size of the image

### assumptions on the input
- A page is the main object in the image
- The photographed page is a rectangular page
- The height of the page is greater than its width
- The page is lighter than the background on which it was filmed.

## Panorama
In the featur we will "sew" two images that contain a common area to one image that shows
both in thesame plane.
This is done by finding key points in both images and finding a match by describing them.

### assumptions on the input
- The two images should share some common area.

# Technologies:
- python(3.9)
- PySimpleGUI
- CV2
	
# Why this project?

I chose to develop this project because the subject of image processing was very appealing to me and I wanted to try it out.
I wanted to learn about how software sees an image and how it can be manipulated to achieve any results.
I also wanted to show some of my ability in this project.

# Running steps:
1. Opening a new project in the work environment
2. Open CMD in the folder where the project is located
3. Installing all extensions:
```python
python -m pip install -r requirements.txt
```
4. Running the project:
```python
python gui.py
```
