tecrube = int(input("Təcrübə ilinizi daxil edin: "))
bal = int(input("Texniki müsahizə balınızı daxil edin: "))
if bal > 0 and bal < 100 :    
    if bal >= 90:
        print("Güclü namizəd!")
    elif tecrube <= 2 and bal >= 70:
        print("Növbəti mərhələyə keçdiniz!")
    else:
        print("Namizəd uyğun deyil!")
else:
    print("Düzgün bal daxil edlimemişdir!")
    