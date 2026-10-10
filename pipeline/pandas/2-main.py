from_file = __import__('2-from_file').from_file

df1 = from_file('coinbase.csv', ',')
print(df1.head())
