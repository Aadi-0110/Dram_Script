from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter , PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
import pyttsx3
from gtts import gTTS
import os



document = open('/home/manish/drama.pdf', 'rb')
#Create resource mana
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
text = ''
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
# receive the LTPage object for the page.
    layout = device.get_result()
    for element in layout:https://buildmedia.readthedocs.org/media/pdf/gtts/latest/gtts.pdf
        try:
            text = text+ element.get_text()
        except:
            pass
        
        
    
text=re.sub(r'\([^)]*\)', '', text)   

# print(text)


  
# # Language in which you want to convert 
# language = 'en'
  

# myobj = gTTS(text=text, lang=language, slow=False) 
  

# myobj.save("welcome.mp3") 
  

# os.system("mpg321 welcome.mp3") 


c=0;
t="Let us start"

dic={}
piche='test'

dic['test']=[]

objects=[]


counter=0
for k in text.split():
    if k.isupper() and len(k)>2:
        myobj=gTTS(text=t,lang='en', slow=False) 
        name=piche+"_"+str(counter)+'.mp3'
        myobj.save(name)
        objects.append(name)
        piche=k
        t=""
        counter+=1
    else:
        t+=" "+k
myobj=gTTS(text=t,lang='en', slow=False) 
name=piche+"_"+str(counter)+'.mp3'
myobj.save(name)
objects.append(name)
        

    
    


for ele in objects:
    print(ele)
    os.system("mpg321 "+ele)
    
