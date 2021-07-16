import PyPDF2
from tika import parser
import re

data= parser.from_file('(For Dummies Math & Science) Steven Holzner-Physics Essentials For Dummies (2010).pdf')
string=data['content']

k=str(string)
def countdata(str):
    upper=0
    lower=0
    number=0
    special=0

    for i in range(len(str)):                       
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
        elif str[i].isdigit():
            number += 1
        else:
            special += 1
    print('upper case letters are:', upper)
    print('lower case letters are:', lower)
    print('number to be :', number)
    print('special characters to be:', special)

countdata(k)
pdfObj = open('(For Dummies Math & Science) Steven Holzner-Physics Essentials For Dummies (2010).pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)
print("Number of pages is ",pdfReader.numPages,"\n")


def countwords(Str):
     
    
    if(Str == None or len(Str) == 0):
        return 0
     
    wordCount = 0
    isWord = False
    endOfLine = len(Str) - 1
     
    
    ch = list(Str)
    for i in range(len(ch)):
         
       
        if(ch[i].isalpha() and i != endOfLine):
            isWord = True
         
        
        elif(not ch[i].isalpha() and isWord):
            wordCount += 1
            isWord = False
         
        
        elif(ch[i].isalpha() and i == endOfLine):
            wordCount += 1
     

    return wordCount
 

 
print("No of words :", countwords(k))
 


white_space = k.count(" ")

print("no of white spaces : ",white_space)

paragraphs = k.count("\n\n")

print("no of paragraphs : ",paragraphs)




