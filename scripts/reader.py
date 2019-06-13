from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter , PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
import pyttsx3
from gtts import gTTS
import os







def audio_return(text,gender):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    return obj
  
