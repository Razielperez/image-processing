# image-processing

This project is a system that presents some image processing operations.
This system is displayed by Peyton's GUI for user convenience
The main purpose of this project is to present the features found in it.
This project contains a "Examples" folder divided according to the various 
features in order to give examples of the system results.

# The features in the system

#### Clear color
```
In this featur we will remove colors from an image by the HSV model.
You can select several colors that we want to remove 
and thus we get an image that contains only the colors we want.
```
#### Cam Scanner
```
In the featur we will make changes to an image by getting an image
that contains a document and the program will take the document and isolate it
from the rest of the image and it will be displayed in full size of the image.
```

:exclamation: assumptions on the input
  - [x] A page is the main object in the image\740
  - [x] The photographed page is a rectangular page
  - [x] The height of the page is greater than its width
  - [x] The page is lighter than the background on which it was filmed.

#### Panorama
```
In the featur we will "sew" two images that contain a common area to one image that shows
both in thesame plane.
This is done by finding key points in both images and finding a match by describing them.
```
:exclamation: assumptions on the input
  - [x] The two images should share some common area.

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

# Examples

- **home page** 

	![homePage](https://user-images.githubusercontent.com/58634656/151966802-ffcc091c-deaa-4fea-ae22-42bb7a4c555a.jpeg)

- **Clear color**

  - Initial window
  
 	<img src="https://user-images.githubusercontent.com/58634656/151971134-53301353-c7d8-431b-bd13-235117da31cd.jpeg" width="400" height="450" />
 
 
  
  - Upload an image and select a colors
  
  	<img src="https://user-images.githubusercontent.com/58634656/151967105-eac4c021-2616-4f82-81dd-9bd43cebbfee.jpeg" width="400" height="450" />
  
  	<img src="https://user-images.githubusercontent.com/58634656/151967107-346517a8-5297-49f7-ab38-7cd12436eafe.jpeg" width="400" height="450" />
 

  - The results after removing the colors
  
  	<img src="https://user-images.githubusercontent.com/58634656/151967106-ed2b84b7-83b2-4f27-9d83-7bdf6fa37e5b.jpeg" width="400" height="450" />
  
  	<img src="https://user-images.githubusercontent.com/58634656/151967070-99a4e586-4651-446f-a445-cefb2812c666.jpeg" width="400" height="450" />
	
- **Cam Scanner**

  - Initial window
  
 	<img src="https://user-images.githubusercontent.com/58634656/151971123-c712146b-9c4c-4e99-be10-78dece0689f6.jpeg" width="300" height="450" />
 
 
  
  - Upload an image 
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971158-0a0eddac-08c7-42ff-9430-28a4db6d218e.jpeg" width="600" height="450" />
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971163-8e9b2bb2-2f4e-4f6f-b937-d3f8cc7199fe.jpeg" width="600" height="450" />
 

  - The results 
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971161-9b9f074e-9e92-40d2-896c-56a8cfacb46b.jpeg" width="300" height="450" />
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971121-9ecf4070-3dfb-460f-b1fc-cbefb3a90b08.jpeg" width="300" height="450" />
	

- **Panorama**

  - Initial window
  
 	<img src="https://user-images.githubusercontent.com/58634656/151971151-79819f2b-ffb9-413e-a843-9acbe1470504.jpeg" width="800" height="450" />
 
 
  
  - Upload an images 
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971137-211b2e51-6f5e-4b06-a228-afa9f5a5c97a.jpeg" width="850" height="450" />
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971149-16b3534e-0c5a-4686-8015-cc7dcbcd11c5.jpeg" width="850" height="450" />
 

  - The results 
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971139-7f81c40f-d325-4f27-8ac7-9fd14fffbfe5.jpeg" width="850" height="450" />
  
  	<img src="https://user-images.githubusercontent.com/58634656/151971152-3bb49c8e-ad59-42d2-a6c6-72008726b49a.jpeg" width="850" height="450" />
	


