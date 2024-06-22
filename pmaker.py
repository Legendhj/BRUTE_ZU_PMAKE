import os

os.system('clear')

def main():
	print(f'[+] Example: Mr. ZUYAN')
	px = input(f'[+] Enter File Name : ')
	namg = input(f'[+] ENTER FULL NAME: ')
	for yuzong in range(2):
		frs = namg.split(' ')[0].lower()
		frst = namg.split(' ')[0]
		nmg = namg.split(' ')[1]
		nmf = namg.split(' ')[1].lower()
		pwv = []
		if len(nmf)<6:
			if len(frs)<3:
				pass
			else:
				pwv.extend([frs+'112', frs+'12', frs+'123', frs+'1234', frs+'12345', frs+'123456',nmf, nmg, 'i love you', frs+'@123', frs+'@', frs+'@@', frs+'@@@', frs+'@@@@',frs+'@#', frs+'@1', frs+'@12', frs+'@#123', frs+'143', frs+'1111', frs+'1122', frs+'11', frs+'111'])
				pwv.extend([frst+'@123', frst+'@1', frst+'@#123', nmf, nmg, frst+'12', frst+'123', frst+'1122', frst+'@#@#@#', frst+'11', frst+'112233', frst+'143', frst+'404', frst+'10', frst+'00', frst+'111',frs+'@#$','###'+frs,'123'+frs])
				print(pwv)
		else:
			if len(frs)<3:
				pwv.append(nmf)
				pwv.append(nm)
				print(pwv)
			else:
				pwv.extend([frs+'112', frs+'12', frs+'123', frs+'1234', frs+'12345', frs+'123456',nmf, nmg, 'i love you', frs+'@123', frs+'@', frs+'@@', frs+'@@@', frs+'@@@@',frs+'@#', frs+'@1', frs+'@12', frs+'@#123', frs+'143', frs+'1111', frs+'1122', frs+'11', frs+'111'])
			if len(frst)<3:
				pass
			else:
				pwv.extend([frst+'@123', frst+'@1', frst+'@#123', nmf, nmg, frst+'12', frst+'123', frst+'1122', frst+'@#@#@#', frst+'11', frst+'112233', frst+'143', frst+'404', frst+'10', frst+'00', frst+'111'])
		for passx in pwv:
			open(f'/sdcard/{px}.txt','a').write(passx+'\n')
			
		
			#print(pwv)
				
                       
main()
