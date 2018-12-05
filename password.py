password = "a1234"
x = 3
while x > 0:
	pwd = input('請輸入你的密碼：')
	if pwd == password:
		print('成功登入')
		break
	else:
		x = x - 1
		print('密碼錯誤,你還剩下',x,'次機會')