import json
import os
text_to_speech = TextToSpeechV1(
    iam_apikey='Ao1fYL9rUFmyeqUnH-OA5JDLSN2v1ujEi3rBHKomeJ9-',
    url= 'https://gateway-lon.watsonplatform.net/text-to-speech/api'
)
text = """<speak>I have been assigned to handle your order status request.<express-as type="GoodNews">
I am sorry to inform you that the items you requested are back-ordered. We apologize for the inconvenience.
</express-as><express-as type="Uncertainty"> We don\'t know when those items will become available. Maybe next
 week but we are not sure at this time.</express-as><express-as type="GoodNews">Because we want you to be a happy
 customer, management has decided to give you a 50% discount! </express-as></speak>"""

text1 = """<voice-transformation type="Custom" timbre="Sunrise" timbre-extent="0%" glottal_tension="0%"
  pitch="0%" pitch_range="0%" rate="0%" breathiness="-100%">
  Do you have more information?
</voice-transformation>"""

text2 = """<voice-transformation type="Custom" glottal_tension="100%" pitch="100%"
  rate="-100%" breathiness="60%">
  Do you have more information?
</voice-transformation>
"""

text3 = """<voice-transformation type="Custom" timbre="Sunrise" pitch="40%">
  Do you have more information?
</voice-transformation>

<voice-transformation type="Custom" timbre="Breeze" timbre_extent="30%"
  pitch="-30%">
  Do you have more information?
</voice-transformation>
"""

text4 = """<voice-transformation type="Custom" timbre="Sunrise" pitch="-30%"
  pitch_range="80%" rate="60%" glottal_tension="-80%">
  Do you have more information?
</voice-transformation>
"""
text0 = """<voice-transformation type="Young" strength="10%">
  Could you provide us with new information?
</voice-transformation>

<voice-transformation type="Soft" strength="10%">
  Could you provide us with new information?
</voice-transformation>
"""
text = text0 + text1 + text2 + text3 + text4

voices = text_to_speech.list_voices().get_result()
print(json.dumps(voices, indent=2))

with open('hello_world.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text,
            voice='en-US_AllisonVoice',
            accept='audio/mp3'        
        ).get_result().content)
    
os.system("mpg321 hello_world.mp3")
