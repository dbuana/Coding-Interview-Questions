# 1). Find the missing number in the array
import random

array = [3,7,1,2,8,4,5] # find the missing number in this unorganized array

def organizing():
	# array = [1,2,3,4,5,7,8] - How the output of the random organizer should potray
	organizedArray = [1,2,3,4,5,7,8]
	for n in array:
		firstResult = random.shuffle(array)
		if firstResult == organizedArray:
			pass
		elif firstResult != firstResult:
			# It should repeat the whole validation process
			for firstResult in organizedArray:
				firstResult = random.shuffle(array)
				pass
		else:
			return None

def theMissingNumber():
	organizedArray = [1,2,3,4,5,7,8] # The ideal shuffled array
	firstResult = random.shuffle(array)
	# The main function code
	for array in organizedArray:
		if firstResult == organizedArray:
			pass
	# The missing number validation
	for array in organizedArray(1,8):
		if organizedArray[0] == 1:
			pass
		elif organizedArray[1] == 2:
			pass
		elif organizedArray[2] == 3:
			pass
		elif organizedArray[3] == 4:
			pass
		elif organizedArray[4] == 5:
			pass
		elif organizedArray[5] == 6:
			newArray = [1,2,3,4,5,6,7,8]
		elif organizedArray[6] == 7:
			pass
		elif organizedArray[7] == 8:
			pass
		else:
			return True
