# Hackathon2023
Ensuring the safety of rail passengers and staff is of utmost importance for train operators. However, there are occasional incidents where unauthorized individuals accidentally fall onto the rail tracks from platforms, resulting in severe injuries or even fatalities.

The conventional approach of relying on Close Circuit Television (CCTV) cameras and human surveillance personnel to monitor rail platforms is resource-intensive. It requires round-the-clock monitoring with multiple staff members diligently observing live video feeds from numerous cameras across stations and platforms. This manual process is susceptible to human error and often leads to delayed response times. Valuable seconds or minutes can be lost between the detection of an incident and the initiation of emergency actions.

To enhance the existing monitoring capabilities, there is a need for an automated computer vision-based solution that can analyze camera feeds in real-time and swiftly detect any unauthorized individuals or objects on the rail tracks. Such a system should reduce the reliance on human resources for monitoring while significantly improving response times through automated alerts. Moreover, it should minimize false alarms by accurately distinguishing between genuine safety incidents and normal activities.

Our proposed solution involves the development of an AI-based platform monitoring system utilizing Convolutional Neural Network (CNN) models and computer vision (CV) technology. CV will continuously capture image frames from cameras and feed them into a CNN model for analysis and inference. The CNN will be trained to classify whether the frames depict unexpected objects on the tracks or empty tracks. Upon detecting an incident with over 85% confidence, the system will promptly send alerts via email, sounds, and/or LED lights to operational staff and train drivers, enabling an immediate emergency response.

This proposed solution aims to enhance rail safety by leveraging automated AI-based computer vision, real-time incident detection, and rapid alert generation, effectively addressing the limitations associated with manual monitoring methods.

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

