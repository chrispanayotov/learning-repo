# Program that converts certain currencies to BGN,
# according to the input of the use

currencies = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']

def displayIntro():
    print('Welcome to the Currency Exchange Kiosk!')
    print('Here you can convert from Leva to the major currencies of the world')
    input('Press Enter to begin!')
    print(f"You can select from the following currencies: {currencies}")

def currencySelection():
    selection = ''
    print('Please enter the abbreviature of the currency that you want to convert to:') 
    selection = input()
    return selection

def amountConversion():
    amount = ''
    print(f'Please type how much BGN you would lke to convert to {selectedCurrency}:')
    amount = input()
    return amount


convertAgain = 'Yes'
while convertAgain == 'Yes' or convertAgain == 'yes' or convertAgain == 'y':
    displayIntro()
    selectedCurrency = currencySelection()
    money = amountConversion()
    
    print('Do you want to convert another currency?')
    convertAgain = input()

