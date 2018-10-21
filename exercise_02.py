num = int(input("Num? "))
check = int(input("Check? "))

res = num % check

if res == 0:
	print("OK! (" + str(res) + ")")
else:
	print("Not OK! (" + str(res) + ")")
