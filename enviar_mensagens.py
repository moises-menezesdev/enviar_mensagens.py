import pandas as pd
import pywhatkit as kit

# Passo 1: Ler o arquivo Excel
df = pd.read_excel()  # Altere para o caminho do seu arquivo

# Passo 2: Identificar as colunas faltantes
for index, row in df.iterrows():
    missing_columns = []
    
    for column in df.columns:
        if pd.isnull(row[column]) or row[column] == "":
            missing_columns.append(column)
    
    if missing_columns:
        phone_number = row['TELEFONE']  # Altere para o nome exato da coluna de telefone
        
        # Passo 3: Gerar a mensagem
        message = f"Olá {row['NOME']}, os seguintes dados estão faltando no seu cadastro: {', '.join(missing_columns)}. Por favor, envie esses dados para regularizar seu cadastro."
        
        # Passo 4: Enviar a mensagem pelo WhatsApp
        kit.sendwhatmsg_instantly(f"+55{phone_number}", message, 15, tab_close=True)

print("Mensagens enviadas com sucesso!")








