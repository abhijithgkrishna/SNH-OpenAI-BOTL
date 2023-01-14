![Github](https://user-images.githubusercontent.com/64391274/211215734-bbc57b92-9a71-496d-873e-3eedc7523916.png)


# BOTL Assistant
A simple voice assistant model using OpenAI API
## Team members
1. Abhijith G [https://github.com/abhijithgkrishna]
2. Javeed Ahmad [https://github.com/JaVD054]
3. Rahul Das P [https://github.com/RAHUL-DAS-P]
## Team Id
2avJUrwvsBErEyeoAZfa
## Link to product walkthrough
[link to video]
## How it Works ?
1. It works with the OpenAI REST API with a simple but powerful TKinter GUI
2. We take the input audio using speech_recognition library and convert it into a String
3. This string serves as the prompt for the OpenAI API request
4. The response is then converted to an audio file using gTTS library
5. The resulting audio is played
6. Link to video demo
## Libraries used
openai==0.26.1
PyAudio==0.2.13
gTTS==2.3.0
SpeechRecognition==3.9.0
## How to configure
pip install requirements.txt
## How to Run
Instructions for running
##Clone the repo and run following commands in the directory : 
pip install -r requirements.txt &&
python main.py
