gelir = int(input("Aylıq gəliri daxil edin: "))
xerc = int(input("Ümumi xərci daxil edin: "))
if gelir >0 and xerc >=0:
    qalan = gelir - xerc
    qenaet = (qalan * 100) // gelir
    if xerc > gelir:
        print("Büdcə kəsiri var!")
        print("Qalan pulu: ", qalan , "AZN")
        print("Qənaət faizi: ", qenaet , "%")
    elif xerc >= gelir * 0.8:    
        print("Xərclərə diqqət et!")
        print("Qalan pulu: ", qalan , "AZN")
        print("Qənaət faizi: ", qenaet , "%")
    elif xerc > (gelir * 0.5) and xerc < (gelir * 0.8):
        print("Qalan pulu: ", qalan , "AZN")
        print("Qənaət faizi: ", qenaet , "%")
        print("Büdcə normaldır!")
    elif xerc < (gelir*0.5):
        print("Yaxşı qənaət edirsiniz!")   
else:
    print("Gəlir 0 və ya az ola bilməz!")
#100 - 100
#75 - x