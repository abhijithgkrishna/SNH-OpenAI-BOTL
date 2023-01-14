# importing required module
from playsound import playsound
from tkinter import *
import speech_recognition as sr
import os
import openai
from gtts import gTTS

root = Tk()
root.title('BOTL assistant')  # giving the title for our window
root.geometry("700x600")
prompt = "Click on the button"
openai.api_key = "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"
r = sr.Recognizer()


# making function


def play():
    with sr.Microphone() as source:
        print("start")
        audio_data = r.record(source, duration=5)
        print("Record")
        text = r.recognize_google(audio_data, show_all=False)
        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            max_tokens=40,
            temperature=1
        )
        print(resp)
        answer = resp["choices"][0]["text"]
        # prompt = answer
        final = gTTS(text=answer, lang='en', slow=False)
        EX = os.path.exists("result.mp3")
        print(EX)
        if (EX == True):
            os.remove("result.mp3")
        EX = os.path.exists("result.mp3")
        print(EX)
        final.save("result.mp3")
        playsound('result.mp3')


# title on the screen you can modify it
title = Label(root, text="Ask Me Anything !!", bd=9, relief=GROOVE,
              font=("times new roman", 50, "bold"), bg="white", fg="black")
title.pack(side=TOP, fill=X)

# making a button which trigger the function so sound can be playeed
play_button = Button(root, text="Voice search", font=("Helvetica", 32),
                     relief=GROOVE, command=play)
play_button.pack(pady=20)

info = Label(root, text=prompt,
             font=("times new roman", 10, "bold")).pack(pady=20)
root.mainloop()
