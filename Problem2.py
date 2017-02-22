print("Welcome to Problem2, this program asks for three numbers and will tell you if they are in ascending order, descending order, over the mountain, or in the dog house")

firstnumber = int(raw_input("firstnumber"))
secondnumber = int(raw_input("secondnumber"))
thirdnumber = int(raw_input("thirdnumber"))

if(firstnumber>secondnumber>thirdnumber):
	print("Falling Down!")
if(firstnumber<secondnumber<thirdnumber):
	print("Up And Rising!")
if(firstnumber<secondnumber>thirdnumber):
	print("Over The Mountain!")
if(firstnumber>secondnumber<thirdnumber):
	print("In The DogHouse!")
