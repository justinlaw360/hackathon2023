# Hackathon2023
Problem statment:  There are incidents that passengers and unaurthorised persson will fall into the rail track and caused injuries or fatal incidents.  It requires a systematic method to detect, analysis and alerts platform operation staff and train driver.

Traditional method uses CCTV and surveillance devices requires intensive man-power to perform monitor.

Therefore, it is proposed to use AI (Artifical Intekkigence) technology to improve the monitoring in terms of (1) reduce man-power involved and (2) improve the performance by shorten the alert time and focus on the real alert cases (reduce false positive cases).  We use Convolutional Neural Netowrk (CNN) model as the underlying technology to analysis whether unexpected object appeared in an image (or series of image frames).  if it is detected with over 85% confident, it will alert the operator in the form of email, sound and/or LED light.

Computer vision (CV) technology is also one of the enablement technology adopted, it capture the image frame in convert the image into suitable format for CNN model.  CNN model analsysis and inference the result and then feed back to the CV, finally CV combine the original image frame and the inference result for the operators.

# Risk in Bowtie model
Below is the "falling object into track" bowtie model

![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/bowtie-hackathon.jpg)

# Our solution - Proof of Concept (PoC)

Input - HD Webcam
![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/hdwebcam.jpg)

Processing - Analysis image using CNN model

![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/cnn.jpg)

Processing - Control LED based on CNN inference

![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/arduino-cli.jpg)

Output - LED controlled by Arduino board
![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/arduino-LED.jpg)

# 5 mins video

[![Watch the video](https://img.youtube.com/vi/T-D1KVIuvjA/maxresdefault.jpg)](https://youtu.be/T-D1KVIuvjA)
