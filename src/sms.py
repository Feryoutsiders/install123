
RawBlameHistory
  
MAS-FERY🔯
#🔯jombang_beriman🔯

from requests import Session
import re, sys
s = Session()

try:
	print(" esemes gratis dan gak mbayar%s
 ,_     _‚
 |\\\___//|	%sAuthor: 🔯MAS-FERY🔯%s
 |=6   6=|	%sContact: https://085330175310%s
 \=._Y_.=/	%sGithub: https://github.com/Feryoutsiders%s
  )  `  (    ,	%sALAMAT: Gedangan_sumobito_jombang%s
 /       \  ((
 |       |   ))
/| |   | |\_//	%sKAREK_NGAWE_AE_KAKEAN_COCOT_COK%s
\| |._.| |/-`
 '"'   '"'
	 %skere_ta_cok_kok_ngawe_sms_Gratis%s
	 
	 Gunakan kode negara (ex: 62xxxxx29)")
	
	 
	 no = int(input("No    : "))
	msg = input("Pesan : ")
except:
	print("\n\t* Cek nomermu atau pesanmu! *")
	sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}

bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
	'nohp':no,
	'pesan':msg,
	'captcha':captcha,
	'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'SMS Gratis Telah Dikirim' in send:
	print(f"\nSukses dikirim! \n[{no}] => {msg}")
elif 'MAAF....!' in send:
	print("\n\t* Mohon Tunggu 15 Menit Lagi Untuk Pengiriman Pesan Yang Sama *")
else:
	print("\n\t* Gagal dikirim! *")
