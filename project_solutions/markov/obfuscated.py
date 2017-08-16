import random;import urllib.request;import turtle;nonword = '\n';w1 = nonword;w2 = nonword;____________________AAJEHBJTOEHBJNOJMAONTMQAONMQAONJBAONJMARTKEONTKMOSETKMONEKMBOEBKTOEXKHOEDUXAETUDXAOBETHABOHJQTABOQAMQANOTJMENOKBOETKHBOTKHBOTKHXEOTKXOETUXBOETHBU = {};request = urllib.request.urlopen('http://gutenberg.ca/ebooks/harec-magicbottle/harec-magicbottle-00-t.txt');text = request.read();oetohtbotkhbojojhtbOETHBOETHBoknmtjnm = str(text).replace("\\n", " ");oetohtbotkhbojojhtbOETHBOETHBoknmtjnm = oetohtbotkhbojojhtbOETHBOETHBoknmtjnm.replace("\\'", "'")
for word in oetohtbotkhbojojhtbOETHBOETHBoknmtjnm.split():____________________AAJEHBJTOEHBJNOJMAONTMQAONMQAONJBAONJMARTKEONTKMOSETKMONEKMBOEBKTOEXKHOEDUXAETUDXAOBETHABOHJQTABOQAMQANOTJMENOKBOETKHBOTKHBOTKHXEOTKXOETUXBOETHBU.setdefault((w1, w2), []).append(word);w1, w2 = w2, word

____________________AAJEHBJTOEHBJNOJMAONTMQAONMQAONJBAONJMARTKEONTKMOSETKMONEKMBOEBKTOEXKHOEDUXAETUDXAOBETHABOHJQTABOQAMQANOTJMENOKBOETKHBOTKHBOTKHXEOTKXOETUXBOETHBU.setdefault((w1, w2), []).append(nonword);w1 = nonword;w2 = nonword;maxwords = 1000;sentencePool = [];sentence = '';c = 0
for i in range(maxwords):
    oejoejothkbthboothbotehoethoeuthoenuhtonhteunhoteokhbtoekthboekbhoenonehoneuhoenh = random.choice(____________________AAJEHBJTOEHBJNOJMAONTMQAONMQAONJBAONJMARTKEONTKMOSETKMONEKMBOEBKTOEXKHOEDUXAETUDXAOBETHABOHJQTABOQAMQANOTJMENOKBOETKHBOTKHBOTKHXEOTKXOETUXBOETHBU[w1, w2])
    if oejoejothkbthboothbotehoethoeuthoenuhtonhteunhoteokhbtoekthboekbhoenonehoneuhoenh == nonword: break
    sentence += oejoejothkbthboothbotehoethoeuthoenuhtonhteunhoteokhbtoekthboekbhoenonehoneuhoenh + ' '
    if oejoejothkbthboothbotehoethoeuthoenuhtonhteunhoteokhbtoekthboekbhoenonehoneuhoenh[-1] in ['.', '!', '?']: sentencePool.append(sentence);sentence = ''
    w1, w2 = w2, oejoejothkbthboothbotehoethoeuthoenuhtonhteunhoteokhbtoekthboekbhoenonehoneuhoenh

output = []
for i in range(5): output.append(random.choice(sentencePool))
_OETJ_OENTJHEONTJHONETJNTEOJHNTOEJHNTOEJHNOET = turtle.Turtle();_OETJ_OENTJHEONTJHONETJNTEOJHNTOEJHNTOEJHNOET.hideturtle();_OETJ_OENTJHEONTJHONETJNTEOJHNTOEJHNTOEJHNOET.penup()
for i in range(5):_OETJ_OENTJHEONTJHONETJNTEOJHNTOEJHNTOEJHNOET.setpos((-400, (25 * i) - 50));_OETJ_OENTJHEONTJHONETJNTEOJHNTOEJHNTOEJHNOET.write(output[i], True);_OETJ_OENTJHEONTJHONETJNTEOJHNTOEJHNTOEJHNOET.update()