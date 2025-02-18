def convert_currency(rates, from_currency, to_currency, amount):
    if from_currency in rates and to_currency in rates:
        converted_amount = (amount * rates[to_currency]) / rates[from_currency]
        return converted_amount
    else:
        print("Geçersiz döviz kuru seçimi.")
        return None

def main():
    # Türk Lirası'na göre döviz kuru verisi
    rates = {
        "USD": 0.052,
        "EUR": 0.048,
        "GBP": 0.042,
        "JPY": 7.07,
        "AUD": 0.078,
        "CAD": 0.070,
        "CHF": 0.047,
        "CNY": 0.36,
        "INR": 4.26,
        "MXN": 0.91,
        "RUB": 4.74,
        "SAR": 0.20,
        "KWD": 0.016,
        "NOK": 0.51,
        "SEK": 0.55,
        "DKK": 0.36,
        "PLN": 0.21,
        "ZAR": 0.80,
        "HKD": 0.40,
        "SGD": 0.07
    }

    while True:
        print("\nSeçenekler:")
        print("1. Kur dönüşümü yap")
        print("2. Kur bilgisi")
        print("3. Çıkış")
        
        choice = input("Seçiminizi yapınız: ")
        
        if choice == "1":
            from_currency = input("Dönüşüm yapacağınız kuru seçin (Örn: USD): ").upper() 
            to_currency = input("Dönüşüm olacak kuru seçin (Örn: EUR): ").upper()
            amount = float(input("Miktarı giriniz: "))
            
            result = convert_currency(rates, from_currency, to_currency, amount)
            if result is not None:
                print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        
        elif choice == "2":
            currency = input("Bilgi almak istediğiniz kuru seçiniz (Örn: USD): ").upper()
            if currency in rates:
                print(f"1 TRY = {rates[currency]} {currency}")
            else:
                print("Geçersiz kur girdiniz.")
            
        elif choice == "3":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim. Tekrar deneyiniz.")

if __name__ == "__main__":
    main()
