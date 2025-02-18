import json

def convert_currency(rates, from_currency, to_currency, amount):
    if from_currency in rates and to_currency in rates:
        converted_amount = (amount * rates[to_currency]) / rates[from_currency]
        return converted_amount
    else:
        print("Geçersiz döviz kuru seçimi.")
        return None

def main():
    with open("exchange_rates.json", "r") as json_file:
        data = json.load(json_file)
    
    rates = data["rates"]
    
    while True:
        print("1. Kur dönüşümü yap")
        print("2. Kur bilgisi")
        print("3. Çıkış")
        
        choice = input("Yapmak istediğiniz işlemi seçiniz: ")
        
        if choice == "1":
            from_currency = input("Dönüşüm yapacağınız kuru seçin: ") 
            to_currency = input("Dönüşüm olacak kuru seçin: ")
            amount = float(input("Miktarı giriniz: "))
            
            result = convert_currency(rates, from_currency, to_currency, amount)
            if result is not None:
                print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            else:
                print("Geçersiz işlem.")
        
        elif choice == "2":
            currency = input("Bilgi almak istediğiniz kuru seçiniz: ")
            if currency in rates:
                print(f"1 TRY = {rates[currency]} {currency}")
            else:
                print("Geçersiz işlem.")
            
        elif choice == "3":
            print("Çıkış Ypılıyor..")
            break
        
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
    