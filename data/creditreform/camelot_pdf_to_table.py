import camelot

foo = camelot.read_pdf('SchuldnerAtlas_Deutschland_2019_Kreise_Alphabet.pdf',pages='1,2,3,4,5,6,7,8,9,10,11')
foo.export('foo.csv', f='csv') 
