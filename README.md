
Real-Time Face Recognition

This repository contains a Python script for face recognition using OpenCV and face_recognition libraries. The script captures real-time video from a camera, detects faces in the stream, and compares them with previously loaded images to identify known faces.


Installing Face Recognition on Windows Here  are some following steps 


Step 1: Install Python

Download and install Python 3.8 (or the latest version) from the official Python website.
Verify that Python and pip are correctly installed by running the following command:

      python --version
        
Step 2: Install dlib and cmake

Note: Make sure to run the Command Prompt as an administrator and navigate to the same folder where you want to install face recognition.
     
        pip install dlib-19.19.0-cp38-cp38-win_amd64.whl  
        
Run the following command to install cmake using pip:
        
         pip install cmake

Step 3: Upgrade pip (if necessary)

If you encounter any errors during installation, upgrade your pip to the latest version using the following command:
        
        pip install --upgrade pip

Step 4: Install Face Recognition

Run the following command to install Face Recognition using pip:
      
        pip install face-recognition

Step 5: Install OpenCV

Run the following command to install OpenCV using pip:

        pip install opencv-python 
        
Additional Step: Upgrade pip (optional)

To ensure you have the latest version of pip, run the following command:

      python -m pip install --upgrade pip 


Features and Conditions:

The features and conditions of this Real-Time Face Recognition repository remain the same:

Features:
Dynamic Loading: Quickly load multiple facial images for identification.
Real-time Face Recognition: Identify faces in live video feeds.
Multiple Person Support: Identify and distinguish between multiple people.

Conditions:
Face recognition in OpenCV Application: Install the necessary libraries using pip install opencv-python face_recognition.
In the script, provide the paths to each person's picture files and corresponding names.
Execute the script: python Face-detect-vdo.py. Press 'q' to end the video broadcast.

Contributions and Permissions:

The contributions and permissions for this project remain the same:

Contributions:
Configuration: To improve recognition accuracy, tweak the tolerance option in compare_faces.
Contributing: We appreciate your contributions! Please open pull requests and issues.


Permission:
For further information, refer to the LICENCE file. This project is licensed under the MIT License.
