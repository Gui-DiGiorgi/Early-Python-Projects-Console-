import os

os.chdir(r'location of this script')

def count_words():

# the "Reader.txt" will have the text which will be treated on this script and it needs to be on the same location as this script

	txt=open("Reader.txt","r", encoding="utf-8")
	print(txt.read())
	txt.close()
	txt=open("Reader.txt","r", encoding="utf-8")
	txt_data=txt.read().replace('\n', ' ')
	b=txt_data.split()
	txt.close()
	c=[".",":","(",")","\"","\'","\u201c","\u201d","!","?",",",";","\u2014","-"]
	
	for f in c:
		new_b=[]
		for i in b:
			new_b+=[i.replace(f,"")]
		b=new_b
        
	new_b=[]
	for i in b:
		new_b+=[i.lower()]
	b=new_b
	total=len(b)
        
	repeated_words=[]
	higher_number=0
	total_unique_words=0
	for i in b:
		if i not in repeated_words:
			number=b.count(i)
			repeated_words+=[i]
		if number>higher_number:
			higher_number=number
            
	for i in range(higher_number):
		words=[]
		repeated_words=[]
		for f in b:
			if f not in repeated_words:
				number=b.count(f)
				repeated_words+=[f]
				if number==i+1:
					words+=[f]
		total_unique_words+=len(words)
		if len(words)!=0:
			print("\nThere are",len(words),"words used",i+1,"time(s):",words)
		for word in words:
			for i in range(i+1):
				b.remove(word)
	print("\nIn total,",total,"words were used from",total_unique_words,"unique words.")

count_words()

exit=input("\nPress any key to exit.")
