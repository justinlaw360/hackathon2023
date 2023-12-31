# Hackathon 2023
Ensuring the safety of rail passengers and staff is of utmost importance for train operators. However, there are occasional incidents where unauthorized individuals accidentally fall onto the rail tracks from platforms, resulting in severe injuries or even fatalities.

The conventional approach of relying on Close Circuit Television (CCTV) cameras and human surveillance personnel to monitor rail platforms is resource-intensive. It requires round-the-clock monitoring with multiple staff members diligently observing live video feeds from numerous cameras across stations and platforms. This manual process is susceptible to human error and often leads to delayed response times. Valuable seconds or minutes can be lost between the detection of an incident and the initiation of emergency actions.

To enhance the existing monitoring capabilities, there is a need for an automated computer vision-based solution that can analyze camera feeds in real-time and swiftly detect any unauthorized individuals or objects on the rail tracks. Such a system should reduce the reliance on human resources for monitoring while significantly improving response times through automated alerts. Moreover, it should minimize false alarms by accurately distinguishing between genuine safety incidents and normal activities.

Our proposed solution involves the development of an AI-based platform monitoring system utilizing Convolutional Neural Network (CNN) models and computer vision (CV) technology. CV will continuously capture image frames from cameras and feed them into a CNN model for analysis and inference. The CNN will be trained to classify whether the frames depict unexpected objects on the tracks or empty tracks. Upon detecting an incident with over 85% confidence, the system will promptly send alerts via email, sounds, and/or LED lights to operational staff and train drivers, enabling an immediate emergency response.

This proposed solution aims to enhance rail safety by leveraging automated AI-based computer vision, real-time incident detection, and rapid alert generation, effectively addressing the limitations associated with manual monitoring methods.

# Falling into permanent way incidents

### Full List

![image](https://github.com/justinlaw360/hackathon2023/assets/4946026/7c24f093-4265-4907-b4ee-e1a494a53b35)

### Analysis

Year	| Number of incident
--- | ---
2017 |	4
2018 |	12
2019 |	11
2020 |	1
2021 |	6
2022 |	3
2023 |	6
Total |	43




Depot	| Number of falling to Permanent way | Deaths	| Percent
--- | --- | --- | --- 
上水站	 | 4	| 3 |	75.00%
九龍塘站	| 5 |	3	| 60.00%
元朗輕鐵站 | 	3 | 	0 | 	0.00%
大圍站	 | 6	 | 3	 | 50.00%
大埔墟站	 | 2	 | 2	 | 100.00%
太和站	 | 4	 | 3	 | 75.00%
旺角東站	 | 3	 | 1	 | 33.33%
沙田站	 | 3	 | 1	 | 33.33%
火炭站	 | 1	 | 1	 | 00.00%
粉嶺站 | 	7	 | 5	 | 71.43%
羅湖站	 | 2	 | 0	 | 0.00%
落馬洲站	 | 1	 | 0	 | 0.00%
西九龍站	 | 1	 | 0	 | 0.00%
觀塘站	 | 1	 | 1	 | 100.00%
Total |  43 |  23 | 

## Recent incidents
### 2023-10-05 

### [Man dies after falling onto Hong Kong railway track at Tai Wo MTR station on East Rail line](https://www.scmp.com/news/hong-kong/law-and-crime/article/3157601/man-dies-after-falling-hong-kong-railway-track-tai-wo)
![alt text](https://cdn.i-scmp.com/sites/default/files/styles/1200x800/public/d8/images/canvas/2021/11/27/b9edd83c-91b0-47ff-8968-477a62e47f62_bd8092c1.jpg?itok=cSCLupUv&v=1637998699)

### 2021-11-06

### [Elderly man dies in suicide fall on tracks at Mong Kok East MTR station in Hong Kong](https://www.scmp.com/news/hong-kong/transport/article/3155096/elderly-man-dies-after-falling-tracks-mong-kok-east-mtr?campaign=3155096&module=perpetual_scroll_0&pgtype=article)
![alt text](https://cdn.i-scmp.com/sites/default/files/styles/1200x800/public/d8/images/methode/2021/11/06/783b95b0-3ea7-11ec-a1b3-e785d5c8830c_image_hires_143513.JPG?itok=m0v3ZN3U&v=1636180520)


# Risk in Bowtie model
Below is the "falling object into track" bowtie model

![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/bowtie.jpg)

# Our solution - Proof of Concept (PoC)

##### Installing webcam in high risk area, real-time video will be captured continuously around the clock.

Input - HD Webcam
![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/hdwebcam.jpg)

##### Real-time video will be analysised by a convolutional neural network (CNN) that is a type of artificial neural network used primarily for image recognition and processing.

Processing - Analysis image using CNN model

![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/cnn.jpg)

Processing - Control LED based on CNN inference

![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/arduino-cli.jpg)

##### if hunman object is detected in the high risk area, LED light that controlled by an Arduino board, will be turned on to alert operational staff.  Sound alert, Email and SMS of course could be triggered.

Output - LED controlled by Arduino board
![alt text](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/arduino-LED.jpg)

# Advantage of our solution

1. Adoption of cutting edge solution.  The core part of the solution is Convolutional neural network, there are models design to anaylsis images, object detection, objection classification, semantic segmentation, face recognition, etc..., that makes the solutions is scalable to adopt new function and features.

2. The whole solution could be run off-line.  Like the PoC, the CNN is saved on my laptop PC, the Webcam and Ardunio board are connected to the laptop directly.  It is suitable to run on closed network environment, such as the OT network and highly secured network.

3. The solution is home-made by our team, knowledge and skillset could be maintained by us.  Further R&D cost and maintainence cost may be reduced substantially, compared to buy from external vendors.

# Cost

This is the estimated cost of equipment for 1 station
Equipment	| Unit | Price (HK$)	| Sub-total
--- | --- | --- | --- 
 |  | | 
#Hardware cost for 1 depot
Server with GPU	 | 1	| $500,000 | $500,000
Webcam	| 10 |	$100	| $1,000
MCU (Arduino board) | 	1 | 	$200 | 	$200
Total	 |   	 |  	 | $501,200
 |  | | 
Software development cost
Development service | 1	 | $1,000,000	 | $1,000,000
 |  | | 
Total	 |   	 |  	 | $1,501,200

   

# 5 mins video

[![Watch the video](https://raw.githubusercontent.com/justinlaw360/hackathon2023/main/videocover.jpg)](https://www.youtube.com/watch?v=isGNl6OgB5U)

# Further developent / opportunity

We can add the face recognition capability into the model, so that it can identify whether the captured object is MTR staff.  Clock-in and clock-out staff attendance.

![alt text](https://xailient.com/wp-content/uploads/2022/08/AI-is-at-the-Edge.-What-does-this-mean-for-Face-Recognition-technology.jpg)

## Incident
### [2 Hong Kong workers killed by suspected biogas leak at MTR Corp-managed construction site; victims’ families complain of negligence](https://www.scmp.com/news/hong-kong/society/article/3235611/2-hong-kong-workers-dead-after-suspected-biogas-leak-construction-site-west-kowloon-cultural)

![alt text](https://cdn.i-scmp.com/sites/default/files/styles/1200x800/public/d8/images/canvas/2023/09/24/c45a0510-42dd-496b-b84a-87af5cb479b0_8b174091.jpg?itok=U8RQ--ol&v=1695532494)

## Our Solution
##### Staff attendance could be recorded automatically by installing webcam in the door exit area, in case staff "disappeared", alerts could be sent out.
