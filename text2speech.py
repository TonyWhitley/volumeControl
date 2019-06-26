import pyttsx3
engine = pyttsx3.init('sapi5') # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
for voice in voices:
    print(voice.name)
    # Microsoft Hazel Desktop - English (Great Britain)
    # Microsoft George - English (United Kingdom)      after registry hack, see
    #                                       Documentation\GeorgeVoiceEnable.reg
    #  https://www.ghacks.net/2018/08/11/unlock-all-windows-10-tts-voices-system-wide-to-get-more-of-them/
    # Microsoft Zira Desktop - English (United States)
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for Hazel
#engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for George
#engine.setProperty('voice', voices[2].id)   #changing index, changes voices. 1 for Zira

#engine.say("Hello World!")
rate = engine.getProperty('rate') # always reports 200 even though rate changes
#engine.say('My current speaking rate is ' + str(rate))

for program in ['r Factor', 'Crew Chief', 'Discord', 'Gear shift', '10%', '50%', 'Full volume', 'Seven Smiles', 'Wrighty']:
    engine.say(program)
engine.runAndWait()
engine.stop()

