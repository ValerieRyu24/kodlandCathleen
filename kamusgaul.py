meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan"
            }
            
word = input('Ketik kata yang ingin dicari tahu:')

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Kata yang anda cari tidak ada di kamus ini.')
