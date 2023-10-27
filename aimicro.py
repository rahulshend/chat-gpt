import openai
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
listner = sr.Recognizer()
openai.api_key = "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"

while True:
    with sr.Microphone() as source:
        print("speak now...")
        voice = listner.listen(source)
        data = listner.recognize_google(voice)
        model = "text-davinci-003"
    
        if 'exit' in data:
            break

    completion = openai.Completion.create(model= "text-davinci-003",
      prompt= data,
      max_tokens= 1027,
      temperature= 0.5,
      n = 1,
      stop= None)
    
    response = completion.choices[0].text
    print(response)
    engine.say(response)
    engine.runAndWait()


  

