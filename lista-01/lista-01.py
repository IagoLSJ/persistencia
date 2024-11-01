import pandas as pd

df = pd.read_csv('vendas.csv')

df['Total_Venda'] = df['Quantidade'] * df['Preco_Unitario']

total_vendas_produto = df.groupby('Produto')['Total_Venda'].sum().reset_index()

df['Data'] = pd.to_datetime(df['Data'])
vendas_janeiro = df[(df['Data'].dt.month == 1) & (df['Data'].dt.year == 2023)]

vendas_janeiro.to_csv('vendas_janeiro.csv', index=False)

with pd.ExcelWriter('total_vendas_produto.xlsx') as writer:
    for produto, grupo in df.groupby('Produto'):
        grupo.to_excel(writer, sheet_name=produto, index=False)
