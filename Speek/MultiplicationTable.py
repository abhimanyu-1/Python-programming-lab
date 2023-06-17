import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

n = int(input("Enter the number: "))
for i in range(1, 10):
    s = i * n
    print(i, "*", n, "=", s)
    engine.say(f"{i} times {n} equals {s}")

engine.runAndWait()



