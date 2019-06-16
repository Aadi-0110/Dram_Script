from ibm_watson import TextToSpeechV1
import os

text_to_speech = TextToSpeechV1(
    iam_apikey='Hgvj7pBH6CUuJ9ry3wFthFqK77Ufm-PowPHXg1rmfl2N',
    url='https://gateway-lon.watsonplatform.net/text-to-speech/api'
)


def Voice_Box(text_input, emotion, gender):
    
    
    print(text_input, emotion, gender)
    text = ""
    if gender == 'male':
        text = ""
        if emotion == 'angry' or emotion=='anger':
            #x = '<voice-transformation type="Custom" rate="60%" breathiness="100%">{}</voice-transformation>'
            x='<voice-transformation type="Custom" glottal_tension="100%" breathiness="99%" pitch="70%" pitch_range="70%" timbre="Sunrise" rate="30%" hoarseness="99%" growl="99%">{}</voice-transformation>'
            y = text_input
            text = x.format(y)

        elif emotion == 'happy' or emotion == 'joy' or emotion =='surprise' or emotion =='love' or emotion=='surprise':
            x = '<voice-transformation type="Custom" rate="-20%" pitch_range="100%" breathiness="100%" pitch="100%">{} </voice-transformation>'
            y = text_input
            text = x.format(y)

        elif emotion == 'sadness':
            x = '<voice-transformation type="Custom"  pitch="80%"  rate="-70%" breathiness="100%">{}</voice-transformation>'
            y = text_input
            text = x.format(y)
        elif emotion == 'fear':
            
            x='<voice-transformation type="Custom" glottal_tension="-99%"  pitch_range="5%"  rate="10%">{}</voice-transformation>'
            y = text_input
            text = x.format(y)
        
        else:
            text=text_input

#         with open('hello_world.mp3', 'wb') as audio_file:
#             audio_file.write(
#                 text_to_speech.synthesize(
#                     text,
#                     voice='en-US_MichaelVoice',
#                     accept='audio/mp3'
#                 ).get_result().content)

#         os.system("mpg321 hello_world.mp3")

    elif gender == 'female':
        text = ""
        if emotion == 'happy' or emotion == 'joy' or emotion =='excitement' or emotion =='love' or emotion=='surprise':
            #x='<voice-transformation type="Custom" glottal_tension="-100%" pitch_range="100%" rate="50%"><express-as type="Good-News" >{}</express-as></voice-transformation>'

            x = '<express-as type="GoodNews">{}</express-as>'
            y = text_input
            text = x.format(y)

        elif emotion == 'apology' or emotion=='sadness':
            x = '<express-as type="Apology">{}</express-as>'
            y = text_input
            text = x.format(y)

        elif emotion == 'uncertainty' or emotion=='fear':
            x='<voice-transformation type="Custom" glottal_tension="-100%" pitch_range="-20%" tremble ="10%" rate="15%" breathiness="100%">{}</voice-transformation>'

            #x = '<express-as type="Uncertainty">{}</express-as>'
            y = text_input
            text = x.format(y)

        elif emotion == 'angry' or emotion=='anger':
            x='<voice-transformation type="Custom" glottal_tension="100%" breathiness="-30%" pitch="45%" pitch_range="90%" timbre="Sunrise" rate="60%" hoarseness="0%" growl="0%">{}</voice-transformation>'

            y = text_input
            text = x.format(y)
        else:
            text=text_input

#         with open('hello_world.mp3', 'wb') as audio_file:
#             audio_file.write(
#                 text_to_speech.synthesize(
#                     text,
#                     voice='en-US_AllisonVoice',
#                     accept='audio/mp3'
#                 ).get_result().content)

#         os.system("mpg321 hello_world.mp3")
    return text


#female sample

#Voice_Box('I am really very very sorry for this','sad', 'female')
#Voice_Box('I am really too excited and happy about this','happy', 'female')
#Voice_Box('I fear too much from ghosts','fear', 'female')
#Voice_Box('I am really very very angry','anger', 'female')
#Voice_Box('I am okay this is my neutral voice','neutral', 'female')

#male samples

#Voice_Box('I am really very very sorry for this','sadness', 'male')
#Voice_Box('I am really too excited about this','happy', 'male')
#Voice_Box('I am really very angry about this and I am not gonna pardon you for this You liar','anger', 'male')
#Voice_Box('This is my normal voice folks!','neutral', 'male')










