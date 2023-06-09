#When is ur date of birth: <day>
#When is ur month of birth: <month>
#When is ur year of birth: <year>

#On January 1st 2023 you turned <days> old

d = int(input("When is ur date of birth: "))
m = int(input("When is ur month of birth: "))
y = int(input("When is ur year of birth: "))

month = (1 -m)*30
year = (2023 - y)*365
date = 1-d

age = month + year + date

print("On January 1st 2023 you turned " + str(age) + " days old")
