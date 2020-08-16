import pandas as pd

# another file reading the file, showing the columnbs and the user selects to see the results
print('*' * 25)
print('Conversor de XLSX para CSV')
print('*' * 25)
print('')
# escolha = str(input('Olá, seja bem-vindo ao conversor! O que você deseja converter? ')
file = input('Local do Arquivo: ')
# nome = str(input('Qual o nome do arquivo? ')).lower
# if nome == 'csv':
df = pd.read_excel(file)
writer = pd.ExcelWriter('teste.xlsx')
df.to_csv(writer, index=False)
writer.save()
print('Pronto! Arquivo convertido para XLSX no desktop.')
# elif type == 'xlsx':
    #df1 = pd.read_excel(file)
    #writer1 = pd.ExcelFile
    #df.to_csv(writer1, index=False)
    #writer1.save()
    #print('Pronto! Arquivo convertido para CSV no desktop,')
# else:
    #print('O tipo desejado não satisfaz as capacidades do programa')