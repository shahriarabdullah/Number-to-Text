#Number to text converter
#Abdullah Shahriar
#25.10.2017

#Unique values and suffix are placed in list and dictionary for further use
suffix=["crore","lakh","thousand","hundred",""]
digit_one={'00':'','0':'','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty'}
digit_two={"1":"","2":"twenty","3":"thirty","4":"fourty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninety"}


number=raw_input() #Input from user
length=len(number) #Calculating length of input
start_index=0 #Initializing variables
end_index=start_index+2
x=0

splitted_number=[] #A list to hold splitted numbers

#This loop adds 0 before the given number until it's length reaches 9
#For example- If 1234 is the input then this loops converts the input
#to 000001234
while x<9-length:
	number="0"+number
	x=x+1

#Re-counting the length. This can be replaced with length=9
length=len(number)
x=0

#Splitting given input for the ease of calculation
#For example- If the input is 000012345 this function will split
#the number and store in splitted_number list as ["00","00","12","3","45"]
while end_index<=length-1:
	if end_index==length-1:
		end_index-=1
	splitted_number.append(number[start_index:end_index])

	start_index=end_index
	end_index+=2

splitted_number.append(number[length-2::])


#Replace each element of splitted_number list with it's text and suffix
while x<len(splitted_number):
	if int(splitted_number[x])<=20 and int(splitted_number[x])!=0:
		splitted_number[x]=digit_one[str(int(splitted_number[x]))] + " " + suffix[x]
	elif int(splitted_number[x])>20:
		splitted_number[x]=digit_two[str(int(splitted_number[x])/10)] + " " + digit_one[str(int(splitted_number[x])%10)] + " " + suffix[x]
		
	x=x+1

#Displaying final result
#The line if y!="00" and y!="0": is used to avoid displaying elements with
#an entry of "00" and "0"
for y in splitted_number:
	if y!="00" and y!="0":
		print y,

