import random

print("Selamat datang di Tes Kecocokan Pasangan")
print("Pilih menu :")
print("1. Uji Berdasarkan Nama")
print("2. Uji Berdasarkan Zodiak")
answer=input("Inputkan pilihan anda : ")

if answer=='1':
  loop=True
  while loop:
      pria=input("Masukkan Nama Pria : ")
      wanita=input("Masukkan Nama Wanita : ")
      print("===========")
      print("Nama Pria : ", pria)
      print("Nama Wanita : ", wanita)

      confirm = input("Apakah nama yang anda masukkan sudah benar? y/n : ")
      if confirm=='y':
        loop=False
  match = random.randrange(0,100)
  print("Presentase kecocokaan:", match,"%")

  if match >80:
    print("Ndang rabi!")
  elif match >60:
    print("Pikir - pikir!")
  elif match >40:
    print("Yakin ga nih?!")
  elif match >20:
    print("Cari lagi deh!")
  else:
    print("Putusin aja!")

elif answer=='2':
  loop=True
  while loop:
      pria=input("Masukkan Zodiak Pria : ")
      tglpria=input("Inputkan tanggal lahir pria (dd-mm-yyy) : ")
      wanita=input("Masukkan Zodiak Wanita : ")
      tglwanita=input("Inputkan tanggal lahir wanita (dd-mm-yyy) : ")
      print("===========")
      print("Tanggal Lahir Pria : ", tglpria)
      print("Zodiak Pria : ", pria)
      print("Tanggal Lahir Wanita : ", tglwanita)
      print("Zodiak Wanita : ", wanita)

      confirm = input("Apakah tanggal lahir dan zodiak yang anda masukkan sudah benar? y/n : ")
      if confirm=='y':
        loop=False
  match = random.randrange(0,100)
  print("Presentase kecocokaan:", match,"%")

  if match >80:
    print("Ndang rabi!")
  elif match >60:
    print("Pikir - pikir!")
  elif match >40:
    print("Yakin ga nih?!")
  elif match >20:
    print("Cari lagi deh!")
  else:
    print("Putusin aja!")
else:
  print("Inputan Anda Salah!")
