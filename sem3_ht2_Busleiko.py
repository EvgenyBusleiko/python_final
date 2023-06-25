# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку

text = 'Magnus es, domine, et laudabilis valde: magna virtus tua et sapientiae tuae non est numerus. Et laudare te vult' \
       ' homo, aliqua portio creaturae tuae, et homo circumferens mortalitatem suam, circumferens testimonium peccati' \
       ' sui et testimonium, quia superbis resistis: et tamen laudare te vult homo, aliqua portio creaturae tuae.' \
       ' Tu excitas, ut laudare te delectet, quia fecisti nos ad te et inquietum est cor nostrum, donec requiescat in te.' \
       ' Da mihi, domine, scire et intellegere, utrum sit prius invocare te an laudare te et scire te prius sit an invocare te.' \
       ' Sed quis te inuocat nesciens te? Aliud enim pro alio potest inuocare nesciens. An potius inuocaris, ut sciaris?' \
       ' Quomodo autem inuocabunt, in quem non crediderunt? Aut quomodo credunt sine praedicante?' \
       ' Et laudabunt dominum qui requirunt eum. Quaerentes enim inueniunt eum et inuenientes laudabunt eum.' \
       ' Quaeram te, domine, inuocans te et inuocem te credens in te: praedicatus enim es nobis.' \
       ' Inuocat te, domine, fides mea, quam dedisti mihi, quam inspirasti mihi per humanitatem filii tui, per ministerium praedicatoris tui.'
text_new=''
list_of_text = ()
new_dict = {}
final_dict={}
key = None
for i in text:
    if i.isalpha() or i == ' ':
        text_new += i
text_new = text_new.upper()
print(text_new)
list_of_text = text_new.split(' ')
print(list_of_text)
for i in list_of_text:
    if i not in new_dict.keys():
        new_dict[i] = 1
    else:
        new_dict[i] += 1
print(new_dict)
for j in range(0, 10, 1):
    max = 0
    for item in new_dict.keys():
        if new_dict[item] > max:
            max = new_dict[item]
            key=item
    final_dict[key]=max
    new_dict[key]=0
print(final_dict)

