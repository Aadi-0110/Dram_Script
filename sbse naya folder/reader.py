from ibm_watson import TextToSpeechV1
import json
import os
text_to_speech = TextToSpeechV1(
    iam_apikey='Ao1fYL9rUFmyeqUnH-OA5JDLSN2v1ujEi3rBHKomeJ9-',
    url= 'https://gateway-lon.watsonplatform.net/text-to-speech/api'
)



def Voice_Box(text_input,emotion,gender):
    
    print(text_input , emotion ,gender)
    
    if gender=='male':
        
        
        text=""
        
        if emotion=='angry':
            
            x='<voice-transformation type="Custom" rate="60%" breathiness="100%">{}</voice-transformation>'
            y=text_input
            text=x.format(y)
            
        elif emotion=='happy' or emotion=='joy':
            
            x='<voice-transformation type="Custom" rate="-20%" pitch_range="100%" breathiness="100%" pitch="100%">{} </voice-transformation>'
            y=text_input
            text=x.format(y)
            
        elif emotion=='sad':
            x='<voice-transformation type="Custom"  pitch="80%"  rate="-70%" breathiness="100%">{}</voice-transformation>'
            y=text_input
            text=x.format(y)
            
        
        with open('hello_world.mp3', 'wb') as audio_file:audio_file.write(
        text_to_speech.synthesize(
            text,
            voice='en-US_MichaelVoice',
            accept='audio/mp3'        
        ).get_result().content)
            
            
            
        os.system("mpg321 hello_world.mp3")
    


        
     
        
    elif gender=='female':
        
        
        
        
        text=""
        
        
        if emotion=='happy' or emotion=='joy':
            
            x='<express-as type="GoodNews">{}</express-as>'
            y=text_input
            text=x.format(y)
            
            
            
            
        elif emotion=='apology':
            
            x='<express-as type="Apology">{}</express-as>'
            y=text_input
            text=x.format(y)
            
            
        elif emotion=='uncertainty':
            x='<express-as type="Uncertainty">{}</express-as>'
            y=text_input
            text=x.format(y)
        
        elif emotion=='angry':
            x=' <voice-transformation type="Custom" glottal_tension="100%" breathiness="0%" pitch="67%" pitch_range="0%" timbre_extent="100%" rate="38%" hoarseness="0%" growl="0%" tremble="0%" timbre="map{400_522.5_1200_1200.0_3000_3000.0_4000_4000}"><express-as type="Excitement" level="74%"> {} </express-as></voice-transformation>'

            y=text_input
            text=x.format(y)
            
            
            
            
            
        with open('hello_world.mp3', 'wb') as audio_file:audio_file.write(
        text_to_speech.synthesize(
            text,
            voice='en-US_AllisonVoice',
            accept='audio/mp3'        
        ).get_result().content)
            
            
            
        
        os.system("mpg321 hello_world.mp3")
    return
        
        
        
        
        
Voice_Box('hello hottie I am too soryy for this behaviour','apology','female')


            
            

        