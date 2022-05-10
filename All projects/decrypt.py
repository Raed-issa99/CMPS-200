def cipher(shift):
	dict={}
	upperCase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lowerCase='abcdefghijklmnopqrstuvwxyz'
	for i in range(26):
		dict[upperCase[(i+shift)%26]]=upperCase[i]
		dict[lowerCase[(i+shift)%26]]=lowerCase[i]
	return dict
def decrypt(message,cipher):
	text=''
	for i in message:
		for j in i:
			if j in cipher :
				text+=cipher[j]
			else:
				text+=j
	return text
def group(message):
	messages=[]
	for i in range(26):
		decrypted=decrypt(message,cipher(i))
		messages.append(decrypted)
	return messages
words=open("words.txt",'r').read().split()
def words_in_message(message,words):
	nbofwords={}
	for i in group(message):
		number_of_words=0
		s=i.split(' ')
		for j in s :
			if j in words:
				number_of_words+=1
		nbofwords[i]=number_of_words
	return( nbofwords)
def get_message(message):
	max=0
	correctmessage=''
	xwords=words_in_message(message,words)
	for i in xwords:
		if int(xwords[i])>max:
			max=xwords[i]
			correctmessage=i
	return correctmessage
print(get_message('R uftkfi, r tzmzc vexzevvi reu r gifxirddvi riv uzjtljjzex nyfjv gifwvjjzfe zj kyv fcuvjk.“Jlivcp dvuztzev zj kyv fcuvjk gifwvjjzfe,” jrpj kyv uftkfi. “Xfu kffb r izs wifd Rurd reu tivrkvu Vmv reu zw kyzj zje’k dvuztzev Z’cc sv…”Kyv tzmzc vexzevvi sivrbj ze:“Slk svwfiv kyrk Yv tivrkvu kyv yvrmvej reu kyv vriky wifd tyrfj. Efn kyrk’j tzmzc vexzevvizex kf dv.”Kyv gifxirddvi kyzebj r szk reu kyve jrpj:“Reu nyf uf pfl kyzeb tivrkvu tyrfj?” '))
