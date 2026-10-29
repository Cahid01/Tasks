price = float(input("Sifarişin məbləğini daxil edin: "))
if price > 0:
    if price > 100:
        print ("Endirim qazandınız!")
        if price >= 200:
            discount = price * 0.8
        print ("Yekun məbləğ: ", discount , "AZN")
        if price >= 100 and price < 200:
            discount = price * 0.9
            print("Yekun məbləğ: ", discount , "AZN")
    else:
        discount = price
        print("Endirim yoxdur!")
        print("Yekun məbləğ: ", discount ,"AZN")                           
else :
    print("Yalnış məbləğ daxil etdiniz!")
    
