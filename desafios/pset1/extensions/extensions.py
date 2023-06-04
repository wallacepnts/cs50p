arquivo = input('Nome do arquivo: ').strip().lower()

if arquivo.endswith('.gif'):
    print('image/gif')
elif arquivo.endswith('.jpg') or arquivo.endswith('.jpeg'):
    print('image/jpeg')
elif arquivo.endswith('.png'):
    print('image/png')
elif arquivo.endswith('.pdf'):
    print('application/pdf')
elif arquivo.endswith('.txt'):
    print('text/plain')
elif arquivo.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')
