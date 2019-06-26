""" Text to speech using one of the standard Windows voices """
import pyttsx3

class Text2Speech:
    """ Text to speech using one of the standard Windows voices """
    def __init__(self, verbose: bool = False):
        self.engine = pyttsx3.init('sapi5') # object creation
        self.verbose = verbose

    def set_rate(self, rate: int = 150):
        """ Speaking rate. Default is 200 """
        self.engine.setProperty('rate', rate)       # setting up new voice rate
        # (Takes a little while before property can be read back)

    def set_volume(self, volume: float = 1.0):
        """ Volume. 0.0 to 1.0 """
        if volume > 1.0:
            volume = 1.0
        if volume < 0.0:
            volume = 0.0
        self.engine.setProperty('volume', volume)    # setting up volume level  between 0 and 1
        # (Takes a little while before property can be read back)

    def select_voice(self, voice_name: str = 'Hazel'):
        """
        Set the voice to be used
        (Use Documentation/<name>VoiceEnable.reg
        to add the other standard UK voices)
        """
        voices = self.engine.getProperty('voices')  #getting details of current voice
        for voice in voices:
            if voice_name in voice.name:
                # Microsoft Hazel Desktop - English (Great Britain)
                # Microsoft George - English (United Kingdom)      after registry hack, see
                #                                       Documentation\GeorgeVoiceEnable.reg
                #pylint: disable=line-too-long
                #  https://www.ghacks.net/2018/08/11/unlock-all-windows-10-tts-voices-system-wide-to-get-more-of-them/
                # Microsoft Zira Desktop - English (United States)
                self.engine.setProperty('voice', voice.id)
                if self.verbose:
                    self.say(f'Voice set to, {voice_name:s}.')
                return
        # default to voice 0 - Hazel
        self.engine.setProperty('voice', voices[0].id)
        if self.verbose:
            # Extract the voice name from "Microsoft Hazel Desktop - English (Great Britain)"
            voice_name = voices[0].name.split()[1]
            self.say(f'Voice set to default, {voice_name:s}.')

    def get_volume(self):
        """ Volume """
        _vol = self.engine.getProperty('volume')
        if self.verbose:
            self.say(f'Volume is, {_vol:.1f}.')

    def get_rate(self):
        """ Speech rate """
        _rate = self.engine.getProperty('rate')
        if self.verbose:
            self.say(f'Speech rate is, {_rate:d}.')

    def say(self, phrase: str):
        """
        Say the phrase.
        . and , introduce a pause.
        """
        self.engine.say(phrase)
        self.engine.runAndWait()

def main():
    """ demo """
    tts_o = Text2Speech(verbose=True)
    tts_o.set_rate(180)
    tts_o.set_volume(0.9)
    tts_o.select_voice('George')
    tts_o.get_volume()
    tts_o.get_rate()

    for phrase in ['r Factor', 'Crew Chief', 'Discord', 'Gear shift', \
                    '10%', '50%', 'Full volume', 'Seven Smiles', 'Wrighty']:
        tts_o.say(phrase)

if __name__ == "__main__":
    main()
