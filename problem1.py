print("Welcome to Problem1, please enter three integer and this program will tell you if the first two integers can add up to the first")

firstnumber = int(raw_input("firstnumber"))
secondnumber = int(raw_input("secondnumber"))
thirdnumber = int(raw_input("thirdnumber"))

#is the sum of firstnumber and secondnumber equal to thirdnumber

if(firstnumber+secondnumber == thirdnumber):
	print("true")
if(firstnumber+secondnumber != thirdnumber):
	print("false")
