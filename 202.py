# Student: Shuntian Xiao, 260823600
# This program is for the challenge question for 202

# The purpose of this program is to determine the average loan amount for each of the home ownership from the data
# in two csv files.

# This program is based one the following discoveries of the two files
# 1. The first row in both files are the name of information which is not "real data"
# 2. Assume the id numbers in two files can be matched up, and are unique
# 3. To determine the average amount of loan, pieces of information I need are the id numbers, type of ownership, and
#     the amount of loan. Respectively, those data are stored in the first column of each file, the second column in the
#    home_ownership_data.csv file, and the second column in the loan_data.csv file.
# 4. Columns in csv files are separated by comma, and each row is a new line

# Step 1 : Load data from csv files.
home_ownership_data_file = open("home_ownership_data.csv", "r")
# print(home_ownership_data_file.readable()) # This is a test to make sure the files are readable
# skip the first row of the file
home_ownership_data_file.readline()
# store data of (id and ownership) status into a list
ownership = home_ownership_data_file.readlines()
home_ownership_data_file.close()

loan_data_file = open("loan_data.csv", "r")
# print(loan_data_file.readable()) # This is a test to make sure the files are readable
# skip the first row of the file
loan_data_file.readline()
# store data of (id, amount of loan, and other information ) status into a list
loan = loan_data_file.readlines()
loan_data_file.close()

# Step 2: Parse the data, match up every person's Id and load amount with the ownership status
# As the first column in both files are the identities of people, data in both files can be matched up.
# Sort both lists of data. Peoples ID are matched up, so their loan and status are matched uo
ownership.sort()
loan.sort()
# Some variables to store the total amount of loan and the number of people with that status
member_mortgage = 0
total_mortgage = 0
member_rent = 0
total_rent = 0
member_own = 0
total_own = 0
# loop through every lines (every person) to add up the total loan and amount of people in each status
# to write a while loop, need the total amount of people by finding the length of the list
number_of_people = len(ownership)
j = 0
while j < number_of_people:
    # Assume people will always have a status that is one of "MORTGAGE","RENT", or"OWN"
    if "MORTGAGE" in ownership[j]:
        member_mortgage = member_mortgage + 1
        # split each line of information in the loan_data.csv file
        # In index 1 (the second piece of information) is the loan, and we need to typecast it into float
        total_mortgage = total_mortgage + float(loan[j].split(",")[1])
    elif "RENT" in ownership[j]:
        member_rent = member_rent + 1
        total_rent = total_rent + float(loan[j].split(",")[1])
    elif "OWN" in ownership[j]:
        member_own = member_own + 1
        total_own = total_own + float(loan[j].split(",")[1])
    j = j+1

# Step 3: determine the average loan amount for each of the home ownership status by dividing the total amount of money
# by the total number of people for the three ownership status
# overwrite result into a csv file
result_file = open("result.csv", "w")
result_file.write("home_ownership,loan_amnt\n")
result_file.write("MORTGAGE," + str(total_mortgage/member_mortgage)+"\n")
result_file.write("OWN," + str(total_own/member_own) + "\n")
result_file.write("RENT," + str(total_rent/member_rent) + "\n")
result_file.close()
