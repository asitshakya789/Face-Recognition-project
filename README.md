
#Face recognition 

This repository contains a Python script for face recognition using OpenCV and face_recognition libraries. The script captures real-time video from a camera, detects faces in the stream, and compares them with previously loaded images to identify known faces.

Installing Face Recognition on Windows 
Step 1: Download python(I use python 3.8 version) Check if pip and python are correctly installed.
      
        python --version
        
Step 2: Enter the following command to install dlib and cmake using pip
        Python 3.8:
        
        pip install dlib-19.19.0-cp38-cp38-win_amd64.whl  
        
Run Command Prompt as an administrator  as same foldor you want to insall  face recognition
        
         pip install cmake

Step 3: If you face some error then  Upgrade your pip to avoid errors during installation.
        
        pip install --upgrade pip

Step 4: Enter the following command to install Face Recognition using pip3.
        
        pip install face-recognition

Step 5 :  Install OpenCV
        pip install opencv-python

        python -m pip install --upgrade pip 
        
  // to upgread your  pip 


Features:

Dynamic Loading: Quickly load multiple facial images for identification.
Real-time Face Recognition: Identify faces in live video feeds.
Multiple Person Support: Identify and distinguish between multiple people.
Conditions:

Face recognition in OpenCV Application: Install the necessary libraries using pip install opencv-python face_recognition.
In the script, provide the paths to each person's picture files and corresponding names.
Execute the script: python Face-detect-vdo.py. Press 'q' to end the video broadcast.
Contributions:

Configuration: To improve recognition accuracy, tweak the tolerance option in compare_faces.
Contributing: We appreciate your contributions! Please open pull requests and issues.
Permission: For further information, refer to the LICENCE file. This project is licensed under the MIT License.
