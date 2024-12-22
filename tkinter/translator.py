from tkinter import*
from googletrans import Translator #googletrans-4.0.0rc1

translator = Translator()
root = Tk()

E = Entry(root, width='40')
F = Frame(root)
B1 = Button(F,text='translate', width='27', height='2')
B2 = Button(F,text='<->',width='9',height='2')
L1 = Label(root, text="Result", height='2')
L2 = Label(root,text='origin language', height='2')
variable = StringVar(root)
variable.set("english")
menu = OptionMenu(root, variable, "africaan", "albanian", "amharic","arabic","armenian","azerbaijani","basque","belarusian","bengali","bosnian","bulgarian","catalan","cebuano","chichewa","chinese (simplified)","chinese (traditional)","corsican","croatian","czech","danish","dutch","english","esperanto","estonian","filipino","finnish","french","frisian","galician","georgian","german","greek","gujarati","haitian creole","hausa","hawaiian","hebrew","hindi","hmong","hungarian","icelandic","igbo","indonesian","irish","italian","japanese","javanese","kannada","kazakh","khmer","korean","kurdish","kyrgyz","lao","latin","latvian","lithuanian","luxembourgish","macedonian","malagasy","malay","malayalam","maltese","mayori","marathi","mongolian","myanmar","nepali","norwegian","odia","pashto","persian","polish","portuguese","punjabi","romanian","russian","samoan","scots gaelic","serbian","sesotho","shona","sindhi","sinhala","slovak","slovenian","somali","spanish","sundanese","swahili","swedish","tajik","tamil","telugu","thai","turkish","ukrainian","urdu","uyghur","uzbek","vietnamese","welsh","xhosa","yiddish","yoruba","zulu")
variable2 = StringVar(root)
variable2.set("english")
menu2 = OptionMenu(root, variable2,"africaan", "albanian", "amharic","arabic","armenian","azerbaijani","basque","belarusian","bengali","bosnian","bulgarian","catalan","cebuano","chichewa","chinese (simplified)","chinese (traditional)","corsican","croatian","czech","danish","dutch","english","esperanto","estonian","filipino","finnish","french","frisian","galician","georgian","german","greek","gujarati","haitian creole","hausa","hawaiian","hebrew","hindi","hmong","hungarian","icelandic","igbo","indonesian","irish","italian","japanese","javanese","kannada","kazakh","khmer","korean","kurdish","kyrgyz","lao","latin","latvian","lithuanian","luxembourgish","macedonian","malagasy","malay","malayalam","maltese","mayori","marathi","mongolian","myanmar","nepali","norwegian","odia","pashto","persian","polish","portuguese","punjabi","romanian","russian","samoan","scots gaelic","serbian","sesotho","shona","sindhi","sinhala","slovak","slovenian","somali","spanish","sundanese","swahili","swedish","tajik","tamil","telugu","thai","turkish","ukrainian","urdu","uyghur","uzbek","vietnamese","welsh","xhosa","yiddish","yoruba","zulu")
a={'af': 'afrikaans','sq': 'albanian','am': 'amharic','ar': 'arabic','hy': 'armenian','az': 'azerbaijani','eu': 'basque','be': 'belarusian','bn': 'bengali','bs': 'bosnian','bg': 'bulgarian','ca': 'catalan','ceb': 'cebuano','ny': 'chichewa','zh-cn': 'chinese (simplified)','zh-tw': 'chinese (traditional)','co': 'corsican','hr': 'croatian','cs': 'czech','da': 'danish','nl': 'dutch','en': 'english','eo': 'esperanto','et': 'estonian','tl': 'filipino','fi': 'finnish','fr': 'french','fy': 'frisian','gl': 'galician','ka': 'georgian','de': 'german','el': 'greek','gu': 'gujarati','ht': 'haitian creole','ha': 'hausa','haw': 'hawaiian','iw': 'hebrew','he': 'hebrew','hi': 'hindi','hmn': 'hmong','hu': 'hungarian','is': 'icelandic','ig': 'igbo','id': 'indonesian','ga': 'irish','it': 'italian','ja': 'japanese','jw': 'javanese','kn': 'kannada','kk': 'kazakh','km': 'khmer','ko': 'korean','ku': 'kurdish','ky': 'kyrgyz','lo': 'lao','la': 'latin','lv': 'latvian','lt': 'lithuanian','lb': 'luxembourgish','mk': 'macedonian','mg': 'malagasy','ms': 'malay','ml': 'malayalam','mt': 'maltese','mi': 'maori','mr': 'marathi','mn': 'mongolian','my': 'myanmar (burmese)','ne': 'nepali','no': 'norwegian','or': 'odia','ps': 'pashto','fa': 'persian','pl': 'polish','pt': 'portuguese','pa': 'punjabi','ro': 'romanian','ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho','sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali','es': 'spanish','su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu','th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu','ug': 'uyghur','uz': 'uzbek','vi': 'vietnamese','cy': 'welsh','xh': 'xhosa','yi': 'yiddish','yo': 'yoruba','zu': 'zulu'}
def translate():
    txt = E.get()
    result=translator.translate(text = txt, dest = variable2.get())
    d=result.src
    L1['text'] = result.text
    if d!=a.setdefault(variable.get()):
        L2['text'] = 'original language: '+a[d]
    else:
        L2['text'] = 'original language: '+a[variable.get()]
B1['command'] = translate
def change():
    rest=variable.get()
    rest2 = variable2.get()
    variable.set(rest2)
    variable2.set(rest)
B2['command'] = change
E.pack()
F.pack()
L1.pack()
L2.pack()
B1.pack(side='left')
B2.pack(side='right')
menu.pack(side='left')
menu2.pack(side='right')
root.mainloop()