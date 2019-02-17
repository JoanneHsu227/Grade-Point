score = input('學生分數: ')
sco = int(score)
if sco <= 100 and sco >= 90:
    print('A+')
elif sco <90 and sco >=85:
	print('A')
elif sco <85 and sco >=80:
	print('A-')
elif sco <80 and sco >=77:
	print('B+')
elif sco <77 and sco >=73:
	print('B')
elif sco <73 and sco >=70:
	print('B-')
elif sco <70 and sco >=67:
	print('C+')
elif sco <67 and sco >=63:
	print('C')
elif sco <63 and sco >=60:
	print('C-')
else :
	print('別看了你不及格')

