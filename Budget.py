gelir = int(input("Aylıq gəliri daxil edin: "))
xerc = int(input("Ümumi xərci daxil edin: "))
if gelir >0 and xerc >=0:
    if xerc > gelir:
        print("Büdcə kəsiri var!")
    elif xerc >= gelir * 0.8:    
        print("Xərclərə diqqət et!")
    elif xerc > (gelir * 0.5) and xerc < (gelir * 0.8):
        print("Büdcə normaldır!")
    elif xerc < (gelir*0.5):
        print("Yaxşı qənaət edirsiniz!")   
else:
    print("Gəlir 0 və ya az ola bilməz!")
qalan = gelir - xerc
qenaet = (qalan * 100) // gelir
print("Qalan pulu: ", qalan , "AZN")
print("Qənaət faizi: ", qenaet , "%")
#100 - 100
#75 - x