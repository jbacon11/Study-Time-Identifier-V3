#Study Hours Identifier V3
#Jeremy Bargy
#4/23/20

def welcome():  #define welcome function

    beginSequence= 'y'       #str
    
    print('\n\t\t\t\tHello Users!\n\t\t\t\t---------------')
    print('Thank you for taking the time to use this program.')
    print('The program was made by Jeremy Bargy.')
    print('Last update April 2020')

    #Display description of program
    print('\n\t\t\t\tInstructions\n\t\t\t\t------------')
    print('The program being used is designed to help students identify their study needs for this semester.\n')
    print('With this information, students can build and develop their own study habits to meet their academic goals.\n\n')
   
    #loop until user had read instructions
    beginSequence = input('Begin program?\n Please enter Y for yes\n')
    while not(beginSequence == 'Y' or beginSequence == 'y') or beginSequence=='' or beginSequence== ' ':
        print('\nError: please read the instructions and enter "Y" for yes to begin: \n')
        beginSequence= input('Begin program? \n\n')

def main():
    menuOption = ""
    STUDYHOURS = "studyHours.txt"
    GRADES = "Grades.txt"
    HOWMANYHOURS = "HowManyHours.txt"
    fileList=[]
    creditList = []
    studyList = []
    gradeList = []
    count = 0

    welcome()

    #Program menu for user to pick purchase options
    while menuOption != "C" and menuOption != "c":

        menuOption = getMenuOption(menuOption)
        if menuOption =="A" or menuOption =="a":

            #initialize variables
            #STUDYHOURS = "studyHours.txt"
            #check for file
            checkFile(STUDYHOURS)

            # Open study hours txt file to read
            studyHoursFile = open('StudyHours.txt', 'r')
            howManyHoursFile = open('HowManyHours.txt', 'a')
            print('File -', HOWMANYHOURS, '- opened...')


            #read the student name and validate
            userName = studyHoursFile.readline()

            #continue reading with the condition of a user name existing
            while userName != '':

                #validate variable and accumulate count
                userName = validateName(userName)
                #begin processing name
                userName = processNameCase(userName)
                #find index position of space between names
                indexPosition = findFirstLast(userName)
                #create first name varaiable
                firstName = getFirstName(userName, indexPosition)
                #create last name variable
                lastName = getLastName(userName, indexPosition)
                #strip the leading white space character left from the user name input on the last name variable
                lastName = lastName.lstrip()
                firstName = firstName.capitalize()
                lastName = lastName.capitalize()
                fullName = firstName + ' ' + lastName

                #read in credit hours and validate
                creditHours = studyHoursFile.readline()
                creditHours = creditHours.rstrip('\n')
                creditHours = validateCreditHours(creditHours)

                #preform calculation function to get number of classes from credit hours
                classes = getNumofClasses(creditHours)

                #read desired grade and validate
                grade = studyHoursFile.readline()
                grade = grade.rstrip('\n')
                grade = validateGrade(grade)

                #preform calculation to get study hours per class from grade desired
                studyHours = getStudyHours(grade)

                #get total study hours per week 
                TotalStudyHoursPerWeek = getTotalStudyHoursPerWeek(classes, studyHours)

                #strip escape character and display results
                fullName = fullName.rstrip('\n')
                
                print('\nStudent Name: \t',fullName)
                print('Credit Hours: \t',creditHours)
                print('Study Hours Recommended: ',TotalStudyHoursPerWeek)
                print('Desired Grade: \t',grade.upper(),'\n')

                userInfo = (fullName , str(creditHours) , str(TotalStudyHoursPerWeek) , grade.upper())
                
                for item in userInfo:
                    howManyHoursFile.write(str(item) + '\n')
                                   
                #read next line from file
                userName = studyHoursFile.readline()

            #close file
            studyHoursFile.close()
            howManyHoursFile.close()
            print('File -', STUDYHOURS, '- closed...')
            print('File -', HOWMANYHOURS, '- closed...')

            #sort records of file
            howManyHoursFile = open('HowManyHours.txt', 'r')
            readLine = howManyHoursFile.readline()
            while readLine != '':
                readLine = readLine.rstrip('\n')
                fileList.append(readLine)
                
                creditLine = howManyHoursFile.readline()
                creditLine = creditLine.rstrip('\n')
                creditList.append(creditLine)
                         
                studyLine = howManyHoursFile.readline()
                studyLine = studyLine.rstrip('\n')
                studyList.append(studyLine)

                gradeLine = howManyHoursFile.readline()
                gradeLine = gradeLine.rstrip('\n')
                gradeList.append(gradeLine)
                
                readLine = howManyHoursFile.readline()
            howManyHoursFile.close()
            
            #append sorted records to file
            sortedFile = open('SortedHours.txt', 'w')
            print('File -SortedHours.txt- opened...')
            for item in fileList:
                fileList.sort()
                creditList.sort()
                studyList.sort()
                gradeList.sort()
                sortedFile.write(item + '\n')
                sortedFile.write(creditList[count]+ '\n')
                sortedFile.write(studyList[count] + '\n')
                sortedFile.write(gradeList[count] + '\n')
                count+=1
            sortedFile.close()
            print('File -SortedHours.txt- closed...')
            
        # menu option B
        elif menuOption == "B" or menuOption == "b":
            #initialize variables and check file
            #GRADES = "Grades.txt"
            checkFile(GRADES)
            # Open grades text file to read
            gradesFile = open('Grades.txt', 'r')
            howManyHoursFile = open('HowManyHours.txt', 'a')
            print('File -', HOWMANYHOURS, '- opened...')

             #read the student name and validate
            studentName = gradesFile.readline()

            #continue reading with the condition of a user name existing
            while studentName != '':

                #validate variable and accumulate count
                studentName = validateName(studentName)
                #begin processing name
                studentName = processNameCase(studentName)
                #find index position of space between names
                indexPositionB = findFirstLast(studentName)
                #create first name varaiable
                firstNameB = getFirstName(studentName, indexPositionB)
                #create last name variable
                lastNameB = getLastName(studentName, indexPositionB)
                #strip the leading white space character left from the user name input on the last name variable
                lastNameB = lastNameB.lstrip()
                firstNameB = firstNameB.capitalize()
                lastNameB = lastNameB.capitalize()
                fullNameB = firstNameB + ' ' + lastNameB

                #read credit hours and validate
                creditHoursB = gradesFile.readline()
                creditHoursB = creditHoursB.rstrip('\n')
                creditHoursB = validateCreditHours(creditHoursB)

                classesB = getNumofClasses(creditHoursB)

                #get study hours per class from grade desired
                studyHoursB =gradesFile.readline()
                studyHoursB = studyHoursB.rstrip('\n')
                studyHoursB = validateStudyHrs(studyHoursB, creditHoursB)

                #use function to get grade variable
                gradeB = getGrade(classesB, studyHoursB)

                #display output
                fullNameB = fullNameB.rstrip('\n')
                print('\nStudent Name: \t',fullNameB)
                print('Credit Hours: \t',creditHoursB)
                print('Study Hours Allocated: ',studyHoursB)
                print('Possible Grade Earned: \t',gradeB.upper(),'\n')

                userInfoB = (fullNameB , str(creditHoursB) , str(studyHoursB) , gradeB.upper())
                
                for item in userInfoB:
                    howManyHoursFile.write(str(item) + '\n')

                #read next line from file
                studentName = gradesFile.readline()

            #close file
            gradesFile.close()
            howManyHoursFile.close()
            print('File -', STUDYHOURS, '- closed...')
            print('File -', HOWMANYHOURS, '- closed...')
            fileListB = []
            creditListB = []
            studyListB = []
            gradeListB = []

            #sort records of file
            howManyHoursFile = open('HowManyHours.txt', 'r')
            readLine = howManyHoursFile.readline()
            while readLine != '':
                readLine = readLine.rstrip('\n')
                fileListB.append(readLine)
                
                creditLine = howManyHoursFile.readline()
                creditLine = creditLine.rstrip('\n')
                creditListB.append(creditLine)
                         
                studyLine = howManyHoursFile.readline()
                studyLine = studyLine.rstrip('\n')
                studyListB.append(studyLine)

                gradeLine = howManyHoursFile.readline()
                gradeLine = gradeLine.rstrip('\n')
                gradeListB.append(gradeLine)
                
                readLine = howManyHoursFile.readline()
            howManyHoursFile.close()

            index = 0
            #append sorted records to file
            sortedFile = open('SortedHours.txt', 'w')
            print('File -SortedHours.txt- opened...')
            for item in fileListB:
                fileListB.sort()
                creditListB.sort()
                studyListB.sort()
                gradeListB.sort()
                sortedFile.write(item + '\n')
                sortedFile.write(creditListB[index]+ '\n')
                sortedFile.write(studyListB[index] + '\n')
                sortedFile.write(gradeListB[index] + '\n')
                index+=1
            sortedFile.close()
            print('File -SortedHours.txt- closed...')

        else:           #menu option C

            #initialize variables and check file
            studentCount = 0
            creditTotal = 0
            totalStudyHours = 0
            averageCredits = 0
            averageStudy = 0
            checkFile(HOWMANYHOURS)
            # Open howmanyhours text file to read
            howManyHoursFile = open('HowManyHours.txt', 'r')

            #read the student name and validate
            readName = howManyHoursFile.readline()

            #continue reading with the condition of a user name existing
            while readName != '':

                studentCount += 1
                readName = readName.rstrip('\n')

                addToCreditTotal = howManyHoursFile.readline()
                addToCreditTotal = addToCreditTotal.rstrip('\n')
                creditTotal += accumulateTotal(addToCreditTotal)

                addToStudyTotal = howManyHoursFile.readline()
                addToStudyTotal = addToStudyTotal.rstrip('\n')
                totalStudyHours += accumulateTotal(addToStudyTotal)

                gradeLine = howManyHoursFile.readline()
                gradeLine = gradeLine.rstrip('\n')

                readName = howManyHoursFile.readline()
                
            howManyHoursFile.close()
            print('File -', HOWMANYHOURS, '- closed...')
            
            try:
                print('Preforming calculations...')
                
                averageCredits = creditTotal / studentCount
                averageStudy = totalStudyHours / studentCount
                print('Calculations completed...\n\n')
                displayOutput(studentCount, averageCredits, averageStudy )
            except ZeroDivisionError:
                print('\nERROR...')
                print('The program is reading zero students used this program...')
                print('Please ask an administrator to check to files...\n')
                displayOutput(studentCount, averageCredits, averageStudy )                   

def getMenuOption(menuOption):      #function to get input for menu option and validates
    menuOption = input("\nSelect A -- Determine Hours to Study.\nSelect B -- Determine Grade.\nSelect C -- End the Program.\n")
    #validates the entry. The user has to pick a menu option  
    while menuOption != "A" and menuOption != "a" and menuOption != "B" and menuOption != "b" and menuOption != "C" and menuOption != "c":
        print("\nError: Please enter option A, B,or C.\n")
        menuOption = input("\nSelect A -- Determine Hours to Study.\nSelect B -- Determine Grade.\nSelect C -- End the Program.\n\n")
    return menuOption

def checkFile(validateFile):    #define check file function. validates there is a file to read, creates file if none found
    try:
        # Open the file.
        infile = open(validateFile, 'r')

        # Close the file.
        infile.close()
        print('File -', validateFile, '- found...')
    except IOError:             #for IOerror display message, append file for passed argument variable, close new file
        print('\nAn error occurred trying to read the file... -', validateFile, '-')
        print('Sample data has been provided. Please ask administrator to load the correct files when finished. \n')
        sampleFile = open(validateFile, 'a')
        sampleFile.close()

def validateName(userName):     #function to validate passed argument of the user name variable
    try:        #try validation for name
        while(userName.isdigit()):
            print('\nError: incorrect name input')
            print('--------------------------------\n')
            userName =input('Please enter your full name input: \n')
        return userName
    except ValueError: #exception for value error, then asks user to enter a name
        print('Error: There is a value error for name')
        print('---------------------------------------\n')
        userName =input('Please enter your full name input: \n')
        return userName

def processNameCase(nameVariable):
    #copy string with all lower cased letters
    nameVariable = nameVariable.lower()
    return nameVariable

def findFirstLast(nameVariable):
    #find the space between the names using the index position of the space beween names
    position = nameVariable.find(' ')
    return position

def getFirstName(nameVariable, position):
    #create first name variable with the index position of the space between names
    firstName = nameVariable[0: position]
    return firstName

def getLastName(nameVariable, position):
    #create last name variable with the index position of the space between names
    lastName = nameVariable[position: ]
    return lastName

def validateCreditHours(creditHours):       #function to validate passed argument of the credit hour variable
    try:        #try validation for digit that is divisible by 3 and greater then 3 and less than 18
        while not(int(creditHours.isdigit())) or not(int(creditHours) % 3 ==0) or int(creditHours) > 18 or int(creditHours) < 3 or int(creditHours)== '' or int(creditHours)== ' ':
            print('\nError: incorrect credit hours input')
            print('---------------------------------------\n')
            creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. Must be between 1 and 6 classes. Or as required, 3 - 18 credit hours. \n\n'))
        creditHours= int(creditHours)
        return creditHours
    except ValueError:      #exception for value error, then asks user to enter valid credit hours
        print('Error: There is a VALUE ERROR for credit hours')
        print('----------------------------------------------\n')
        creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. Must be between 1 and 6 classes. Or as required, 3 - 18 credit hours. \n\n'))
        while not(int(creditHours.isdigit())) or not(int(creditHours) % 3 ==0 ) or int(creditHours) > 18 or int(creditHours) < 3 or int(creditHours)== '' or int(creditHours)== ' ':
            print('\nError: incorrect credit hours input')
            creditHours = (input('Please enter the credit hours you are currently enrolled in. i.e. Must be between 1 and 6 classes. Or as required, 3 - 18 credit hours. \n\n'))
        creditHours= int(creditHours)
        return creditHours

def getNumofClasses(creditHours):       #function to get number of classes from passed argument of credit hours
    CREDITSPERCLASS = 3
    classes = int(creditHours) // CREDITSPERCLASS
    return classes

def validateGrade(grade):       #function to validate passed argument of the grade variable
    try:        #try validation for letter grade between A and F
        while not(grade.isalpha()) or not(grade=='A' or grade=='a' or grade =='B' or grade== 'b' or grade== 'C' or grade== 'c' or grade== 'D' or grade== 'd' or grade== 'F' or grade== 'f') or grade == '' or grade == ' ':
            print('\nError: incorrect grade input')
            print('------------------------------------\n')
            grade= input('Please enter the grade you wish to earn: \n\n')
        return grade
    except ValueError:      #exception for value error, then asks user to enter valid grade
        print('Error: There is a value error for grade')
        print('----------------------------------------\n')
        grade = input('Please enter the grade you wish to earn: \n\n')
        return grade

def getStudyHours(grade):       #function to get study hours from passed argument of the grade variable
    studyHours = 0
    if grade == 'A' or grade == 'a':
        studyHours = 15
    elif grade == 'B' or grade == 'b':
        studyHours = 12
    elif grade == 'C' or grade == 'c':
        studyHours = 9
    elif grade == 'D' or grade == 'd':
        studyHours = 6
    else:
        studyHours = 0
    return studyHours

def getTotalStudyHoursPerWeek(classes, studyHours):     #function to get total study hours per week from passed argument of classes and study hour variables
    TotalStudyHoursPerWeek= classes * studyHours
    return TotalStudyHoursPerWeek

def validateStudyHrs(studyHoursB, creditHoursB):        #function to validate study hours with passed arguments of study hours and credit hours
    try:        #try validation for number between 0 and 125
        while not(int(studyHoursB.isdigit())) or int(studyHoursB) < 0 or int(studyHoursB) > 125 or int(studyHoursB)< creditHoursB or int(studyHoursB) == '' or int(studyHoursB) == ' ':
            print('Error: incorrect study hours input')
            print('---------------------------------------\n')
            studyHoursB = input('Please enter in a positve number for your study hours that is more than your credit hours.\n Do not excced 125. You still need time to rest! :\n')
        studyHoursB = int(studyHoursB)
        return studyHoursB
    except ValueError:      #exception for value error, then asks user to enter valid study hours
        print('Error: There is a value error for study hours')
        print('----------------------------------------------\n')
        studyHoursB = input('Please enter in a positve number for your study hours. Do not excced 125. You still need time to rest! :\n')
        return studyHoursB

def getGrade(classesNum, expecthoursofstudy):       #function to get grade from passed arguments of number of classes and expected hours of study
    gradeDesired = ''
    studyhoursperclass = 0
    studyhoursperclass = int(expecthoursofstudy) / classesNum
    
    if studyhoursperclass >= 15:
        gradeDesired = 'A'
    elif studyhoursperclass >= 12:
        gradeDesired = 'B'
    elif studyhoursperclass >= 9:
        gradeDesired = 'C'
    elif studyhoursperclass >= 6:
        gradeDesired = 'D'
    else:
        gradeDesired = 'F'
    return gradeDesired

def accumuateCount(countVariable):      #function to accumulate from passed argument of count variable
    countVariable +=1
    return countVariable

def accumulateTotal(accVariable):       #function to accumulate total from passed argument of total variable
    totalVariable = 0
    totalVariable += int(accVariable)
    return int(totalVariable)

def displayOutput(sCount, aCredits, aStudy):
    print('\nProgram Averages: ')
    print('--------------------\n')
    print('Total Students: \t',sCount)
    print('Average Credits: \t',aCredits)
    print('Average Study Hours: \t',aStudy)
    print('\n\nThanks for using the program!')
    print('Goodbye!')

main()







    
