# from book import string
import re
# chars=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","  ","   ","\n\n\n","     ","(  )"]
string=""
with open("textinput.txt","r") as file:
    string=file.read()
__lines= re.split('\n',string)
n=70
list_of_lines=[[line[i:i+n] for i in range(0,len(line),n) ] for line in __lines if line.__len__()>n]
_lines=[]
for each in list_of_lines:
    _lines+=each

lines=[ line for line in _lines if line.__len__()>60 ]


# for char in chars:
#     string=string.replace(char,"")

# with open("textinput.txt","w") as file:
#     file.write(string)
#     file.close()