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

<img target="_blank" src="https://github.com/minhAI2045/Design-module-to-emulate-PT2248-infrared-signal-decoding-IC/blob/main/Resource/IC%20PT2248%20pinout.png" width=370>


### Functional block diagram
<img target="_blank" src="https://github.com/minhAI2045/Design-module-to-emulate-PT2248-infrared-signal-decoding-IC/blob/main/Resource/Function_diagram.png" width=670>



#### Broadcast principle
Function block and coding block:
- Converts the control signal into the corresponding binary number in the form of a digital signal command code

Modulation block:
- Pair the command code into the carrier with frequency from 38KHz - 100KHz
- Helps increase transmission distance

Transmitter block:
- It is an infrared LED
#### Revenue principles
Receiver block:
- The infrared rays from the emitter are received by the photodiode

Amplifier and detector block:
- Amplify the received signal and then pass it through the parallel separation circuit to eliminate the carrier waves and extract the necessary data, which is the command code

Decoding block:
- Convert command code from binary number to corresponding decimal number

### NEC PROTOCOL
A protocol that uses pulse distance coding
The two logic levels 0 and 1 in the NEC protocol are defined as:
Logic level 1: is a HIGH pulse with a period of 562.5𝜇𝑠 and a LOW level with a period of 1687𝜇𝑠
Logic level 0: is a HIGH pulse with a period of 562.5𝜇𝑠 and a LOW level with a period of 562.5𝜇𝑠

### Design control circuit on ALTIUM

<p align="left">

   <img target="_blank" src="https://github.com/minhAI2045/Design-module-to-emulate-PT2248-infrared-signal-decoding-IC/blob/main/Resource/Design%20a%20control%20circuit%20on%20Altium.png" width=470>
   <img target="_blank" src="https://github.com/minhAI2045/Design-module-to-emulate-PT2248-infrared-signal-decoding-IC/blob/main/Resource/Control%20circiut%20on%20Altium.png" width=270>
  
   














