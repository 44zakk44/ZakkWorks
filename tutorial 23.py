fw = open('sample.txt', 'w')
# zapisujemy plik txt
fw.write('writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

#wczytujemy tekst
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()