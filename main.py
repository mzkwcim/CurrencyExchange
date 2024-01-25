import currencyapicom

client = currencyapicom.Client('cur_live_Ht7cwEfYvrVC1bbDJTvjhWEkVqwHW5d71kN5BK5k')
input_currency = input("Enter input currency: ").upper()
output_currencies = input("Enter output currencies (comma-separated): ").upper().split(', ')
amount = float(input("Enter amount: "))
date = input("Enter date (YYYY-MM-DD): ")
result = client.historical(date)
print(f"\nData for {date}:")
for output_currency in output_currencies:
    conversion_rate = result['data'][output_currency]['value']/result['data'][input_currency]['value']
    converted_amount = amount * conversion_rate
    print(f" -> {amount} {input_currency} = {converted_amount:.2f} {output_currency}")
