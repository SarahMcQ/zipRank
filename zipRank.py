def zipRank():
    ''' Input user's name, age, zipcode, salary, retirement savings balance,
    credit card debt, student loan debt, home value and mortgage balance. 
    Collects and stores this data in csv file. Returns how the user's salary  
    and home value compare to the median income and home value in their US 
    zipcode.'''

#dummy list
zipRankHistory = []

#ask for first name  
name = input('Do you live in the US? Want to know how you rank financially in your zipcode? Please tell me your first name:')
#ask for age
while True:
    try: 
        age = int(input("Great! How old are you"+""+ name + " ? "))
    except ValueError:
        print("Sorry that's not a valid age. Let's try that again...")
        continue
    else:
        break


while age < 18:
    print("Sorry we don't have data for anyone under 18. Please enter an age equal too or greater than 18.")
    while True:
        try:
            age = int(input("How old are you again?"))
        except ValueError:
            print("Sorry I don't understand your answer. Let's try this again...")
            continue
        else:
            break
                  
#ask for zipcode and confirm it's a valid input
zipcode = (input('What is your zipcode? Please enter a 5 digit number.')) 
#import US zipcode data
import uszipcode
from uszipcode import SearchEngine
search = SearchEngine(simple_zipcode=True)
zc = search.by_zipcode(str(zipcode))

while zc.zipcode==None:
    print('Sorry, that zipcode is invalid; please enter a valid zipcode.')
    zipcode = (input('What is your zipcode? Please enter a 5 digit number.'))
    if zipcode !=None:
        break
  
#ask for salary and confirm it's a valid input
while True:
    try:
        salary = int(input('What is your annual salary? $'))
    except ValueError:
        print("Sorry I don't understand that. Please try again and be sure to leave out commas or special characters.")
        continue
    else:
        break
    
while salary < 0:
    print("Please enter a number equal to or greater than 0.")
    while True:
        try:
            salary = int(input("What is your annual salary?"))
        except ValueError:
            print("Sorry I don't understand that. Please enter a number equal to or greater than 0.")
            continue
        else:
            break
#ask about emergency fund balance and confirm it's a valid input
while True:
    try:
        emergencyFund = int(input('In the event of an emergency how much cash do you have that you could access immediately?'))
    except ValueError:
        print("Sorry I don't understand your response please enter a number equal to or greater than 0.")
        continue
    else:
        break

while emergencyFund < 0:
    print("Please enter a number equal to or greater than 0.")
    while True:
        try:
            emergencyFund = int(input("How much is your emergency fund?"))
        except ValueError:
            print("Sorry I don't understand that. Please enter a number equal to or greater than 0.")
            continue
        else:
            break  
            
#ask for retirement savings balance and confirm it's a valid input
while True:
    try:
        retirementSavings = int(input('What is the total balance of all your retirement savings accounts?'))
    except ValueError:
        print("Sorry I don't understand that. Please enter a number leaving out any commas or special characters. Let's try that again...")
        continue
    else:
        break
while retirementSavings < 0:
    while True:
        try:
            retirementSavings = int(input("Oops let's try again. Please enter a number equal to or greater than 0..."))
        except ValueError:
            print("Sorry I don't understand your answer. Please enter a positive number of 0 or greater. Let's try this again...")
            continue
        else:
            break
#ask about credit card debt and confirm it's a valid input
while True:
    try:
        creditCardDebt = int(input('How much credit card debt do you have?'))
    except ValueError:
        print("Sorry I don't understand your answer. Let's try this again...")
        continue
    else:
        break
while creditCardDebt < 0:
    while True:
        try:
            creditCardDebt = int(input("Please enter a number greater than 0. Let's try this again..."))
        except ValueError: 
            print("Sorry I don't understand your answer. Let's try this again...")
            continue
        else:
            break
    
#ask student debt balance and confirm it's a valid input
while True:
    try:
        studentDebt = int(input('How much student loan debt do you have?'))
    except ValueError:
        print("Sorry I don't understand your answer. Let's try this again...")
        continue
    else:
        break
    #while studentDebt < 0:
    print("Let's try again...")
    while True:
        try:
            studentDebt = int(input("How much student debt do you have please enter a number equal to or greater than 0."))
        except ValueError:
            print("Sorry I don't understand your answer.")
            continue
        else:
            break
#ask about home value and confirm it's a valid input
while True:
    try:
        homeValue = int(input("If you own a home what is it's value? If you don't please enter '0'."))
    except ValueError:
            print("Sorry I don't understand your answer.")
            continue
    else:
        break
#while home value < 0:
while homeValue < 0:
    print("Let's try again...")
    while True:
        try:
            homeValue = int(input("What is the value of your home. Please enter a number equal to or greater than 0."))
        except ValueError:
            print("Sorry I don't understand your answer.")
            continue
        else:
            break
    
#ask for mortgage balance
while True:
    try:
        mortgageBalance = int(input("How much do you owe on your mortgage? Please enter a number equal to or greater than 0."))
    except ValueError:
        print("Sorry I don't understand your answer.")
        continue
    else:
        break
    #while mortgageBalance < 0:
    print("Let's try again...")
    while True:
        try:
            mortgageBalance = int(input("How much do you owe on your mortage? Please enter equal to or greater than 0."))
        except ValueError:
            print("Sorry I don't understand your answer.")
            continue
        else:
            break


#Save the updated list information to csv file
import csv
#replace filename with path to csv file or uncomment code below to create 
#new csv file
filename = '/Users/user/Documents/zipRankData.csv'
with open(filename,'a', newline='') as csvfile:
    fieldnames = ['name', 'age', 'zipcode','salary','emergencyFund','retirementSavings','creditCardDebt','studentDebt','homeValue','mortgageBalance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#    df = pd.read_csv(filename) # or pd.read_excel(filename) for xls file
#    if df.empty: # will return True if the dataframe is empty or False if not.
#    if csv file isn't open uncomment the following line
#        writer.writeheader()
      
    writer.writerow({'name': name, 'age': age, 'zipcode': zipcode,'salary': salary,'emergencyFund': emergencyFund, 'retirementSavings': retirementSavings,'creditCardDebt': creditCardDebt,'studentDebt': studentDebt,'homeValue': homeValue,'mortgageBalance': mortgageBalance})
           
print('\n') #create spacing
print("Thanks for that" + name + "! Stand by we're procesing your information now...")
print('\n')
print('\n')

#create variables for plotting results
vc = search.by_zipcode(zipcode)
city = vc.post_office_city
medianIncome = vc.median_household_income
medianHomeValue = vc.median_home_value

#print explanation of results for salary
if salary > medianIncome:
    print("Congratulations " + name + "! You make more than the median income in " + city + " of $" + str(medianIncome) + ".")

if salary < medianIncome:
    print("Sorry" + name + ". Right now you make less than the median income of $" + str(medianIncome) + " in " + city +  ".")

print('\n')

#plot results using subplot
import matplotlib.pyplot as plt 

#create plot showing how user's salary compares to median salary and style
plt.subplot(2,1,1)  #create new figure
x = [1, 2, 3, 4, 5]
labels =['','','','',''] 
plt.plot([3],[salary], 'g*')
plt.ylabel('Salary')
plt.title('Where your SALARY ranks in your zipcode')    #create title
plt.axhline(y=[medianIncome], color='r')
plt.ylim((min([medianIncome, salary])-(0.1*min([medianIncome, salary])),max([medianIncome,salary])+(0.1*max([medianIncome, salary]))))
plt.text(1.5,medianIncome+500, "Your neighbors' median income in " + city, fontsize=12)
plt.text(3,salary,'You')
plt.xticks(x,labels)

#create plot showing how user's home compares to median home value and style
plt.subplot(2,1,2)  #create new figure
plt.plot([3],[homeValue], 'b*')
plt.ylabel('Home Value')
plt.title('Where your HOUSE ranks in your zipcode')     #create title
plt.axhline(y=[medianHomeValue], color='r')
plt.ylim((min([medianHomeValue, homeValue])-(.1* min([medianHomeValue, homeValue])),max([medianHomeValue, homeValue])+(.1*max([medianHomeValue, homeValue]))))
plt.text(1.5,medianHomeValue+2000, "Your neighbors' median home value in "+ city, fontsize=12)
plt.text(3,homeValue,'You')
plt.xticks(x,labels)
plt.show()

print('\n')

#print explanation of results for home value
if homeValue > medianHomeValue: 
    print("When it comes to your $" + str(homeValue) + " house it's worth $" + str(homeValue - medianHomeValue) + " more than the median home value in " + city + " of $" + str(medianHomeValue) + ".")

if homeValue < medianHomeValue:
    print("When it comes to your $" + str(homeValue) + " house it's worth $" + str(medianHomeValue - homeValue) + " less than the median home value in " + city + " of $" + str(medianHomeValue) + ".")

print('\n')

#use json request to add US Census data about the gender wage gap in the user's state
def getCensusData(): 
    ''' asks for user's US state of residence
    returns the median earnings of men vs. women in that state
    as well as the percentage of the gender pay gap in that state. '''
#import to search states by fips code and make json request
import us 
import requests 
#add api endpoint
a = requests.get('https://api.census.gov/data/2016/acs/acs5/subject?get=NAME,S2414_C04_001E,S2419_C02_001E,S2419_C03_001E&for=state:*')
#search for state
yourState = str(us.states.lookup(zc.state))
# find state specific stats and return results
for x in (a.json()):
    if (x[0]) == yourState:
        print("Did you know that in " + (x[0]) + " women make " + (x[1]) + "% of what men earn? On average men earn $"+ (x[2]) + " a year versus women who earn $" + (x[3]) + " a year.")



    
    
    
    
        
        
