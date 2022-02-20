print('Selamat datang di quiz cepat tanggap darurat')
jawaban=input('Apakah siap untuk menjawab? (yes/no) :')
skor=0
total_pertanyaan=3
 
if jawaban.lower()=='yes':
    jawaban=input('Pertanyaan 1 : 10 + 5 = ? ')
    if jawaban.lower()=='15':
        skor += 1
        print('Benar bro :) ')
    else:
        print('Salah jawab bro :( ')
 
 
    jawaban=input('Pertanyaan 2: 10 + 2 - 2 + 10 + 100 - 20 * 0 = ? ')
    if jawaban.lower()=='0':
        skor += 1
        print('Benar bro :) ')
    else:
        print('Salah jawab bro :( ')
 
    jawaban=input('Pertanyaan 3: 9 * 9 = ? ')
    if jawaban.lower()=='81':
        skor += 1
        print('Benar bro :) ')
    else:
        print('Salah jawab bro :( ')
 
print('Terimakasih telah mengikuti quiz yang tidak penting ini, jawaban kamu benar',skor,)
nilai=(skor/total_pertanyaan)*100
print('nilai:',nilai)
print('babay!')