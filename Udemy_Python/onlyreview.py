with open('Test') as oldfile2, open('newfile2.txt', 'w') as newfile2:

    for line in oldfile2:

         newline= line.lstrip()

         head, sep, tail = newline.partition('&')

         print tail

         newhead = tail.replace('Reviews','')

         newfile2.write(newhead + "\n")
