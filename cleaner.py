import csv
import re
import random
import ast

inpute = open("american-election-tweets.csv","r")
output = open("output.csv","wb")
output2 = open("Hastag.csv","wb")
#Erstellen eines Cleaner, welcher eine neue Output Datei erstellet, womit wir zu einem spaeteren Zeitpunkt die verschiedenen Tabellen erstellt haben. Der Cleaner beinhaltet, dass wir alle Tweets, welche gekuerzt sind, rausgefilter & entfernt wurden. Desweiteren haben wir alle fehlerhaften Textzeichen & die source url entfernt. 
reader = csv.reader(inpute,delimiter=";")
writer = csv.writer(output,delimiter=";")
writer2 = csv.writer(output2,delimiter=";")
count = 1
TNR = ["TNR"]
test = []
for row in reader:
	row[1] = re.sub(r'[^\x00-\x7f]',r'',row[1]) #Entfernt alle fehlerhaften Textzeichen
	pat = re.compile(r"#(\w+)")
	hashtag = pat.findall(row[1]) #Sammelt die Hashtags des betreffenden Text und haengt diesen in ein Global Array an, welches letztendlich alle Hashtags beinhaltet. 
	if not not hashtag:
		for i in range(len(hashtag)):
			hashtag[i] = ''.join(('#',hashtag[i]))
		global test
		test += hashtag
	if row[10] != "True": #Nur Zeilen, in denen nicht gekuerzt Tweets vorkommen, werden in unsere Output Datei geschrieben.
		row[4] = row[4].replace('T',' ') 
		writer.writerow([row[0],TNR[len(TNR)-1],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],hashtag]) 
#Beschreibt die neue Datei, hinzugefuegt wurden noch die Spalte TNR, welche als Indice fuer die Tweets dient.
	TNR.append(count)
	count += 1
def quicksort(a):
	if len(a)<2:
		return a
	else:
		x=random.randint(0,len(a)-1)
		pivo=a[x]
		ls=list(filter(lambda x:x<pivo,a))
		rs=list(filter(lambda x:x>pivo,a))
		y=quicksort(ls)+[pivo]+quicksort(rs)
		return y
test = quicksort(test) #Sortiert unsere Global Liste, die nun alphabetisch sortiert ist und duplicate entfernt wurden.Desweiteren haben wir fuer jeden einzelnen Hashtag die Tweetnummern gespeichert, fuer die Tweets in denen er vorkommt. Wir ueberlegen, ob wir diese Arrays zu einem spaeteren Zeitpunkt noch nutzen koennen.

inpute.close()
output.close()
#Erstellen der verschiedenen Tabellen im csv Format
#Hashtag 
momo = 1
for i in range(len(test)):
	indice=[]
	inpute2 = open("output.csv","r")
	reader2 = csv.reader(inpute2,delimiter=";")
        if momo == 1:
		writer2.writerow(["HtNR","Text"])
		momo = momo+1
	for row in reader2:
		if row[2].find(test[i])>=0:
			indice.append(row[1])
	inpute2.close()
	writer2.writerow([i+1,test[i]])
output2.close()	
				
#Handle 
output3 =open("Handle.csv","wb")
handle = ["HillaryClinton","TheRealDonaldTrump"]
for i in range(len(handle)):
	writer3 = csv.writer(output3,delimiter=";")
	writer3.writerow([handle[i]])
output3.close()

#tweet 
output4 =open("Tweet.csv","wb")
inputee1=open("output.csv","r")
writer4 = csv.writer(output4,delimiter=";")
readeer = csv.reader(inputee1,delimiter=";")
for row in readeer:
	if row[0] == "HillaryClinton":
		k = 1
	elif row[0] =="realDonaldTrump":
		k = 2
	else:
		k ="HNR"
	writer4.writerow([row[1],row[9],row[8],row[5],k,row[2]])
output4.close()
inputee1.close()

#retweet
retweet = open("retweet.csv","wb")
writer6 = csv.writer(retweet,delimiter=";")
kunt = open("output.csv","r")
reader8 = csv.reader(kunt,delimiter=";")
kacke = 1
for row in reader8:
	if row[3] == "True" or kacke==1:
		if row[0] == "HillaryClinton":
			k = 1
		elif row[0] == "realDonaldTrump":
			k = 2
		else:
			k ="HNR"
			kacke = kacke+1
		writer6.writerow([k,row[1],row[4]])
kunt.close()
retweet.close()

#relations
rela = open("USEDIN.csv","wb")
writer9 = csv.writer(rela,delimiter=";")
cunt = open("output.csv","r")
reader9 =csv.reader(cunt,delimiter=";")
counter = 1
for row in reader9:
	if counter == 1:
		writer9.writerow(["TNR","HtNR"])
		counter = counter + 1
	elif not row[10] == '[]':
		x = ast.literal_eval(row[10])
		for i in range(len(x)):
			HtNR = test.index(x[i]) + 1
			writer9.writerow([row[1],HtNR])
cunt.close()
rela.close()



#reply
reply = open("reply.csv","wb")
writer6 = csv.writer(reply,delimiter=";")
kunt = open("output.csv","r")
reader8 = csv.reader(kunt,delimiter=";")
kacke = 1
for row in reader8:
        if not row[6] == "" or kacke==1:
                if row[0] == "HillaryClinton":
                        k = 1
                elif row[0] == "realDonaldTrump":
                        k = 2
                else:
                        k ="HNR"
                        kacke = kacke+1
                writer6.writerow([k,row[1],row[6]])
kunt.close()

