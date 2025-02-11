import fedfred as fred

my_api_key = '43370c0e912250381f6728328dfff294'

client = fred.client(my_api_key)

gdp = fred.gdp()

print(gdp)