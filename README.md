## Design module to emulate PT2248 infrared signal decoding IC


### Table of Content
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Learning Objective](#Learning-Objective)
  * [Data Visualizations](#Data-Visualizations)
  * [CorrelationMatrix](#CorrelationMatrix)
  * [Model Evaluation](#Model-Evaluation)
  


### Overview 
Infrared light:
- Cannot be seen with the naked eye
- Frequency: 430 THz – 300 GHz
- Wavelength: 700 nm – 1 mm
- Very safe for the human body → long wavelength measurement
- Easily susceptible to interference: every object with a temperature greater than 0 degrees K emits infrared light

### IC PT2248 

IC PT2248 is an infrared transmitter using CMOS technology, the power supply voltage range is 2.2V~5V. Because it uses CMOS technology to manufacture, the power consumption is extremely low. It can hold down multiple keys at the same time (up to 6 keys), with very few external components.

![alt text](<https://github.com/minhAI2045/Design-module-to-emulate-PT2248-infrared-signal-decoding-IC/blob/main/Resource/IC%20PT2248%20pinout.png>)


### Learning Objective
The following points were the objective of the project . If you are looking for all the following points in this repo then i have not covered all in this repo. I'm working on blog about this mini project and I'll update the link of blog about all the points in details later . (The main intention was to create an end-to-end ML project.)  
- Data gathering 
- Descriptive Analysis 
- Data Visualizations 
- Data Preprocessing 
- Data Modelling 
- Model Evaluation 


### Data Visualizations
- Histogram
![alt text](<https://github.com/minhAI2045/Predicting-diabetes1/blob/main/Data%20Visualization/Histogram.png>)
- Density plot
![alt text](<https://github.com/minhAI2045/Predicting-diabetes1/blob/main/Data%20Visualization/Density_pilot.png>)
- Looking at the graphs, we see that "Glucose", "Blood Pressure", "BMI" have a normal distribution; "Tricep skin" exponential distribution


### CorrelationMatrix
<img target="_blank" src="https://github.com/minhAI2045/Predicting-diabetes1/blob/main/Correlation%20Matrix/Correlation_Matrix.png" width=570>







###  Model Evaluation 
- RandomForestClassifier

<img target="_blank" src="https://github.com/minhAI2045/Predicting-diabetes1/blob/main/Model%20Evaluation/RandomForestClassifier.png" width=370>

                     precision    recall   f1-score   support

    Not Diabetic         0.79      0.79      0.79        99
    Diabetic             0.62      0.62      0.62        55
           
    accuracy                                 0.73       154
    macro avg            0.70      0.70      0.70       154
    weighted avg         0.73      0.73      0.73       154


- Support Vector Machine

<img target="_blank" src="https://github.com/minhAI2045/Predicting-diabetes1/blob/main/Model%20Evaluation/SVC.png" width=370>



                 precision    recall  f1-score   support

    Not Diabetic     0.77      0.82      0.79        99
    Diabetic         0.63      0.56      0.60        55

    accuracy                             0.73       154
    macro avg        0.70      0.69      0.70       154
    weighted avg     0.72      0.73      0.72       154


- KNeighborsClassifier 

<img target="_blank" src="https://github.com/minhAI2045/Predicting-diabetes1/blob/main/Model%20Evaluation/KNeighborsClassifier.png" width=370>

                 precision    recall   f1-score   support

    Not Diabetic     0.76      0.80      0.78        99
    Diabetic         0.60      0.55      0.57        55

    accuracy                             0.71       154
    macro avg        0.68      0.67      0.67       154
    weighted avg     0.70      0.71      0.70       154















