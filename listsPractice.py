currencies = ['Dollar', 'Euro', 'Pound']
# append 'Yen' to the list
currencies.append('Yen')

currenciesWithRate = [['Dollar', 182], ['Euro', 200], ['Pound', 220]]
# append 'Yen' With Rate to the list
currenciesWithRate.append(['Yen', 1.2]) # append will add this list as new subset of a list

newList = [['Lira', 14],['OMR', 430],['Dinar', 510]]
# extend Complete List to the Prev list
currenciesWithRate.extend(newList) # extend will add this list as extending the previous list not adding just one as new subset of a list

# print(currencies)
print(currenciesWithRate)

# for currency in currencies:
#     print(currency)


currenciesWithRate.sort()
for currency in currenciesWithRate:
    print(f"{currency[0]} Rate is: {currency[1]}")


# Slicing List
print("Slicing List: ", currenciesWithRate[3:7])

# Copying List
newListCopy = currenciesWithRate.copy()
print("Copied List: ", newListCopy)