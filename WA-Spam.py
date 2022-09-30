#!/usr/bin/python
import requests,random,json,time,sys,os,re

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italic = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

class spam:
		
	def __init__(self, number):
		self.number = number
            
	def agent(self):
		A1=random.choice(open('file.txt').readlines()).split('\n')[0]
		details = {
			'User-Agent' : A1,
			'Accept-Encoding' : 'gzip, deflate',
			'Connection' : 'keep-alive',
			'Origin' : 'https://accounts.tokopedia.com',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With' : 'XMLHttpRequest',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		v1 = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.number+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fv1er%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = details).text
		Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', v1).group(1)
		otp_gt = {
			"otp_type" : "116",
			"msisdn" : self.number,
			"tk" : Token,
			"email" : '',
			"original_param" : "",
			"user_id" : "",
			"signature" : "",
			"number_otp_digit" : "6"
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = details, data = otp_gt).text
		if 'spam' in req:
			return f''+red+'Spamm sent {self.number} Fail!'+end
		else:
			return f''+green+'Spamm sent {self.number} Success!'+end

def again():
	while True:
		ag_input=str(input(blue+'\t\nWant more? y/n : '+end))
		if( ag_input == 'y' or ag_input == 'Y'):
			defeat()
		elif(ag_input == 'n' or ag_input == 'N'):
			print(red+"Bye..!"+end)
			break
		else:
			continue

def single():
	number=str(input(bold+blue+'\tPhone number : '+end))
	sg_input=int(input(bold+blue+'\tTotal spam : '+end))
	delay=int(input(bold+blue+'\tDelay : '+end))
	for oo in range(sg_input):
		run=spam(number)
		if s_p == 'tkpd':
			print('\t'+run.agent())
		elif s_p == 'all':
			print('\t'+run.agent())
		else:
			print()
	again()

def multi():
	number=[]
	mt_input=int(input(bold+blue+'\tTotal number :- '+end))
	for i in range(mt_input):
		number.append(str(input(f''+bold+blue+'\tNumber - {i+1} :- '+end)))
	total_spam=int(input(bold+blue+'\tTotal spam :- '+end))
	delay=int(input(bold+blue+'\tDelay : '+end))
	le_nm=len(number)
	for i in range(total_spam):
		for ss in range(le_nm):
			run=spam(number[ss])
			if s_p == 'tkpd':
				print('\t'+run.agent())
			elif s_p == 'all':
				print('\t'+run.agent())
			else:
				print()
	again()

def logo():
	os.system('clear')
	s_s="[+]--{Hello}--[+]"
	return ''''''

def main():
	print(logo())
	print(bold+italic+"""
		1. Single Number
		2. Multi Number
	"""+end)
	mn_input=str(input(red+'[+]--{Mode}-->'+end))
	if( mn_input == '1' or mn_input == '01'):
		single()
	elif( mn_input == '2' or mn_input == '02'):
		multi()
	elif( mn_input == 'exit' or mn_input == 'Exit'):
		defeat()
	else:
		print(red+'[!]--{Invaid Input}--[!]'+end)
		time.sleep(2)
		main()
def defeat():
	os.system('clear')
	global s_p
	print(logo())
	print(bold+green+"[+]--{.WhatsApp Spam.}--[+]\n"+end)
	while True:
		dt_input=str(input(blue+"[+]--{Spam}--[select_option]"+end+bold+"\n"+"""
	1.Send Spam
	[+]--{exit}--[+]
		"""+"\n Enter Your choice :- "+end))
		if( dt_input == '0' or dt_input == '' ):
			s_p='all'
			break
		elif( dt_input == '1' or dt_input == '01' ):
			s_p='tkpd'
			break
		elif( dt_input == 'exit' or dt_input == 'Exit' ):
			print(green+"Bye..!"+end)
			sys.exit()
		else:
			print(red+'[!]--{Invaid Input}--[!]'+end)
			time.sleep(1)
			os.system('clear')
			continue
	main()
if __name__ == '__main__':
	defeat()
