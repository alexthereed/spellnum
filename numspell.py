ones = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tens = {0:'',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'nintey'}
teens = {0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
placelist = ['','thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion','nonillion','decillion','undecillion','duodecillion','tredecillion','quattuordecillion','quindecillion','sexdecillion','septemdecillion','octodecillion','novemdecillion','vigintillion','unvigintillion','duovigintillion','trevigintillion','quattuorvigintillion','quinvigintillion','sexvigintillion','septvigintillion','octovigintillion','nonvigintillion','trigintillion','untrigintillion','duotrigintillion','ten-duotrigintillion']

usernum = (input('Please enter a number: '))
sortingnum = usernum[::-1]

chunks = [sortingnum[x:x+3] for x in range(0,len(sortingnum),3)]
lastlist = []
placerev = []
place = []

for x in chunks:
    if x == '000':
        placerev.append('')
    else:
        placerev.append(placelist[chunks.index(x)])

for z in placerev[::-1]:
    place.append(z)

for i in chunks[::-1]:
    lastlist.append(i[::-1])

def num_translate(num):
    numlen = len(num)
    if numlen == 1:
        return(ones[int(num[0])])
    elif numlen == 2:
        if num[0] == '1':
            return (teens[int(num[1])])
        else:
            return(tens[int(num[0])] + ' ' + ones[int(num[1])])
    else:
        if num == '000':
            return ''
        else:
            return(ones[int(num[0])] + ' hundred ' + tens[int(num[1])] + ' ' + ones[int(num[2])])




for i in lastlist:

    print(num_translate(i) + ' ' + place[lastlist.index(i)], end=' ')
