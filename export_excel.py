from pandas import DataFrame

Cars = {'Brand': ['Honda Civic', 'Toyota Corolla', 'Ford Focus', 'Audi A4'],
        'Price': [32000, 35000, 37000, 45000]
        }

df = DataFrame(Cars, columns=['Brand', 'Price'])

export_excel = df.to_excel(r'export_dataframe.xlsx', index=None,
                           header=True)  # Don't forget to add '.xlsx' at the end of the path

print(df)
