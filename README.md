# smart-attendance-system
facial recognition using raspberry pi 3


The present day attendance system is manual. It wastes a considerable amount of time both for teachers and students. The waiting time of the students is increased if attendance is taken manually. There are still chances for proxies in the class when attendance is taken manually. Manual attendance always a have a cost of human error. Face is the essential recognizable proof for any human. So automating the attendance process will increase the productivity of the class. To make it available for every platform we have chosen the Raspberry pi 3 model B for face recognition. Webcam is associated with the Raspberry Pi module. Face identification separates faces from non-faces and those countenances that can be perceived. This module can be utilized for different applications where face acknowledgment can be utilized for validation. In this proposed system we take the attendance using face recognition which recognizes the face of each student in front of it while entering the class.   In this paper, Face Recognition-based Lecture Attendance System [2], the system marks attendance using face  recognition by taking pictures of whole class. As it will be difficult to estimate the attendance accurately using individual results of the face recognition system as the rate of face detection is usually low. Here the system proposes a method of estimation using the results of the face recognition system by continuous training. Continuous training improves the performance of the system. This system uses a capturing camera to capture and monitor the class continuously which sends the data to the face recognition module. This system considers the seating arrangement of the class is unaltered so that the positions of the seats is used to fetch student faces for marking attendance.  
In Student Monitoring by Face Recognition [4] the camera is fixed at a position where the entry and exit of the class room is clear and is used to capture the image of the entering student and leaving student. 3D Face recognition algorithm is used in the system. Detected student faces are stored as the test images in the database and compares the existing student images using Eigen faces technique. If any entering student is matched with any image in the student database attendance is marked for that particular student for that day.  


# Hardware and software requirements
Software Requirements:
On the development end, following software components were used:
Operating system: Raspbian (Debian), Windows 10
Language: Python2.7, Python 3.5
Platform: OpenCV (Linux-library) 
Software Used: VNC Viewer

The operating system under which the proposed project is executed is Raspbian which is derived from the Debian operating system. The algorithms are written using the python language which is a script language. The functions in algorithm are called from the OpenCV library. OpenCV is an open source computer vision library, which is written under C and C++ and runs under Linux, Windows and Mac OS X. OpenCV was designed for computational efficiency and with a strong focus on real-time applications. OpenCV is written in optimized C and can take advantage of multi-core processors. Also contains a full, general-purpose Machine Learning Library (MLL).



 # PROPOSED APPROACH
 
The total system is divided into 3 modules- Database creation, Training the dataset, Testing, sending alert messages as an extension.

1. Database creation 
a) Initialize the camera and set an alert message to grab the attention of the students.  
b) Get user id as input 
c) Convert the image into gray scale, detect the face 
d) Store it in database by using given input as label 
up to 20 frames.
 




2. Training
a) Initialize LBPH face recognizer. 
b) Get faces and Id’s from database folder to train
the LBPH face recognizer. 
c) Save the trained data as xml or yml file.
 


3. Testing
Load Haar classifier, LBPH face recognizer and trained 
data from xml or yml file.
a) Capture the image from camera, 
b) Convert it into gray scale, 
c) Detect the face in it and
d) Predict the face using the above recognizer. 


# Software Modules
 
  ALGORITHMS 

Python IDE 
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an
ideal language for scripting and rapid application  development in many areas on most platforms. The Python interpreter is easily extended with new functions
and data types implemented in C or C++ (or otherlanguages callable from C). Python is also suitable as an extension language for customizable applications.

OpenCV

OpenCV is a library of programming functions mainlyaimed at real-time computer vision. It has a modular structure, which means that the package includes several shared or static libraries. We are using image processing module that includes linear and non-linear image filtering, geometrical image transformations (resize, affine and perspective warping, and generic table-based remapping), color space conversion, histograms, and so on. Our project includes libraries such as Viola-Jones or Haar classifier, LBPH (Lower Binary Pattern histogram) face recognizer,Histogram of oriented gradients (HOG).
 
Image processing module
 
Image processing is a method to perform some operations on an image, in order to get an enhanced image (simply to highlight certain features of interest in an image) or to extract some useful information from it. It is a type of signal processing in which input is an image and output may be image or characteristics/features associated with that image. 


Purpose of Image processing

The purpose of image processing is divided into 5 groups.
They are:

1. Visualization- Observe the objects that are not visible.
2. Image sharpening and restoration- To create a better
image.
3. Image retrieval- Seek for the image of interest.
4. Measurement of pattern– Measures various objects in
an image.
5. Image Recognition– Distinguish the objects in an image.

Haar Classifier
 
This object detection framework is to provide competitive object detection rates in real-time like detection of faces in an image. A human can do this easily, but a computer needs precise instructions and constraints. To make the task more manageable, Viola–Jones requires full view frontal upright faces. Thus in order to be detected, the entire face must point towards the camera and should not be tilted to either side. While it seems these constraints could diminish the algorithm's utility somewhat, because the detection step is most often followed by a recognition step, in practice these limits on pose are quite acceptable


