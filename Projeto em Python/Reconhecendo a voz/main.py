import speech_recognition as sp
import pyaudio
rec = sp.Recognizer()

#for index, name in enumerate(sp.Microphone.list_microphone_names()):
  #  print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
print("="*20)

with sp.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Estou escultando!")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
