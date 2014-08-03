from django.db import models

class model1040NREZ(models.Model):
    refnum = models.IntegerField("Reference Number", default=0)
    INFOL01 = models.CharField("Your first name and initial", max_length=128)
    INFOL02 = models.CharField("Last name", max_length=128)
    F1040NREZL01 = models.BooleanField("Single nonresident alien", default=False)
    F1040NREZL02 = models.BooleanField("Married nonresident alien", default=False)
    F1040NREZL03 = models.IntegerField("Wages, salaries, tips, etc. Attach Form(s) W-2", default=0)
    F1040NREZL04 = models.IntegerField("Taxable refunds, credits, or offsets of state and local income taxes", default=0)
    F1040NREZL05 = models.IntegerField("Scholarship and fellowship grants. Attach Form(s) 1042-S or required statement", default=0)
    F1040NREZL06 = models.IntegerField("Total income exempt by a treaty from page 2, Item J(1)(e)", default=0)
    F1040NREZL07 = models.IntegerField("Add lines 3, 4, and 5", default=0)
    F1040NREZL08 = models.IntegerField("Scholarship and fellowship grants excluded", default=0)
    F1040NREZL09 = models.IntegerField("Student loan interest deduction", default=0)
    F1040NREZL10 = models.IntegerField("Subtract the sum of line 8 and line 9 from line 7. This is your adjusted gross income", default=0)
    F1040NREZL11 = models.IntegerField("Itemized deductions", default=0)
    F1040NREZL12 = models.IntegerField("Subtract line 11 from line 10", default=0)
    F1040NREZL13 = models.IntegerField("Exemption", default=0)
    F1040NREZL14 = models.IntegerField("Taxable income. Subtract line 13 from line 12. If line 13 is more than line 12, enter -0-", default=0)
    F1040NREZL15 = models.IntegerField("Tax. Find your tax in the Tax Table on pages 17 through 25", default=0)
    F1040NREZL16 = models.IntegerField("Unreported social security and Medicare tax from Form:", default=0)
    F1040NREZL16a = models.IntegerField("Form 4137", default=0)
    F1040NREZL16b = models.IntegerField("Form 8919", default=0)
    F1040NREZL17 = models.IntegerField("Add lines 15 and 16. This is your total tax", default=0)
    F1040NREZL18a = models.IntegerField("Federal income tax withheld from Form(s) W-2 and 1099-R", default=0)
    F1040NREZL18b = models.IntegerField("Federal income tax withheld from Form(s) 1042-S", default=0)
    F1040NREZL19 = models.IntegerField("2013 estimated tax payments and amount applied from 2012 return", default=0)
    F1040NREZL20 = models.IntegerField("Credit for amount paid with Form 1040-C", default=0)
    F1040NREZL21 = models.IntegerField("Add lines 18a through 20. These are your total payments", default=0)
    F1040NREZL22 = models.IntegerField("If line 21 is more than line 17, subtract line 17 from line 21. This is the amount you overpaid", default=0)
    F1040NREZL23a = models.IntegerField("Amount of line 22 you want refunded to you.", default=0)
    F1040NREZL23b = models.IntegerField("Routing number", default=0)
    F1040NREZL23c = models.IntegerField("Checking or Savings", default=0)
    F1040NREZL23d = models.IntegerField("Account number", default=0)
    F1040NREZL23e = models.IntegerField("If you want your refund check mailed to an address outside the United States not shown above, enter that address here:", default=0)
    F1040NREZL24 = models.IntegerField("Amount of line 22 you want applied to your 2014 estimated tax", default=0)
    F1040NREZL25 = models.IntegerField("Amount you owe. Subtract line 21 from line 17. For details on how to pay, see instructions", default=0)
    F1040NREZL26 = models.IntegerField("Estimated tax penalty (see instructions)", default=0)
    
    # label not required here, since the modelPostTaxInput already has it, which gets passed to postTaxInputForm
    # null=True is for database, blank=True is for form validation
    # since boolean does not accept null, use default=false 
    F1040NREZSCHOILA = models.CharField(max_length=128)
    F1040NREZSCHOILB = models.CharField(max_length=128)
    F1040NREZSCHOILC = models.BooleanField(default=False)
    F1040NREZSCHOILD1 = models.BooleanField(default=False)
    F1040NREZSCHOILD2 = models.BooleanField(default=False)
    F1040NREZSCHOILE = models.CharField(max_length=128)
    F1040NREZSCHOILF = models.BooleanField(default=False)
    F1040NREZSCHOILFc = models.CharField(max_length=128)
    F1040NREZSCHOILGa = models.BooleanField(default=False)
    F1040NREZSCHOILGb = models.BooleanField(default=False) #to delete
    F1040NREZSCHOILGc = models.DateField(null=True)
    F1040NREZSCHOILGd = models.DateField(null=True)
    F1040NREZSCHOILHa = models.IntegerField(null=True)
    F1040NREZSCHOILHb = models.IntegerField(null=True)
    F1040NREZSCHOILHc = models.IntegerField(null=True)
    F1040NREZSCHOILI = models.BooleanField(default=False)
    F1040NREZSCHOILIc = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.INFOL01 + " " + self.INFOL02
   
class modelSummary(models.Model):
    SUMMARY01 = models.CharField("Filing Status", default="", max_length=128)
    SUMMARY02 = models.IntegerField("Gross Income", default=0)
    SUMMARY03 = models.IntegerField("Deductions:", default=0)
    SUMMARY03a = models.IntegerField("Tax treaty exemption:", default=0)
    SUMMARY03aa = models.CharField("country", default="Hong Kong", max_length=128)
    SUMMARY03b = models.IntegerField("Personal exemption", default=0)
    SUMMARY03c = models.IntegerField("State and local income taxes", default=0)
    SUMMARY03d = models.IntegerField("Student loan interest", default=0)
    SUMMARY03e = models.IntegerField("Scholarship and fellowship grants", default=0)
    SUMMARY04 = models.IntegerField("Taxable Income", default=0)
    SUMMARY05 = models.IntegerField("Tax", default=0)
    SUMMARY06 = models.IntegerField("Other taxes: Unreported social security and Medicare tax", default=0)
    SUMMARY07 = models.IntegerField("Total Taxes", default=0)
    SUMMARY08 = models.IntegerField("Tax payments and credit", default=0)
    SUMMARY09a = models.IntegerField("Tax Refundable", default=0)
    SUMMARY09b = models.IntegerField("Tax Due", default=0)

class modelPostTaxInput(models.Model):

    # Schedule OI fields
    SCHOILA = models.CharField("A. Of what country or countries were you a citizen or national during the tax year?", default="", max_length=128, blank=True, null=True)
    SCHOILB = models.CharField("B. In what country did you claim residence for tax purposes during the tax year?", default="", max_length=128, blank=True, null=True) 
    SCHOILC = models.BooleanField("C. Have you ever applied to be a green card holder (lawful permanent resident) of the United States?", default=False)
    SCHOILD1 = models.BooleanField("A U.S. citizen?",  default=False)
    SCHOILD2 = models.BooleanField("A green card holder (lawful permanent resident) of the United States?",  default=False)
    SCHOILE = models.CharField("E. If you had a visa on the last day of the tax year, enter your visa type. If you did not have a visa, enter your U.S. immigration status on the last day of the tax year.", default="", max_length=128, blank=True, null=True)
    SCHOILF = models.BooleanField("F. Have you ever changed your visa type (nonimmigrant status) or U.S. immigration status?", default=False)
    SCHOILFc = models.CharField("If you answered 'Yes,' indicate the date and nature of the change.", default="", max_length=128, blank=True, null=True)
    SCHOILGa = models.BooleanField("Canada", default=False)
    SCHOILGb = models.BooleanField("Mexico", default=False)
    SCHOILGc = models.DateField("Date entered United States (mm/dd/yy)", blank=True, null=True)
    SCHOILGd = models.DateField("Date departed United States (mm/dd/yy)", blank=True, null=True)
    SCHOILHa = models.IntegerField("2011", default=0)
    SCHOILHb = models.IntegerField("2012", default=0)
    SCHOILHc = models.IntegerField("and 2013", default=0)
    SCHOILI = models.BooleanField("I. Did you file a U.S. income tax return for any prior year?", default=False)
    SCHOILIc = models.CharField("If 'Yes,' give the latest year and form number you filed", default="", max_length=128, blank=True, null=True)
    
    # F8843 fields
    F8843L01A = models.CharField("1a. Type of U.S. visa (for example, F, J, M, Q, etc.) and date you entered the United States", default="", max_length=128, blank=True, null=True)
    F8843L01B = models.CharField("1b. Current nonimmigrant status and date of change (see instructions)", default="", max_length=128, blank=True, null=True)
    F8843L02 = models.CharField("2. Of what country were you a citizen during the tax year?", default="", max_length=128, blank=True, null=True)
    F8843L03A = models.CharField("3a. What country issued you a passport?", default="", max_length=128, blank=True, null=True)
    F8843L03B = models.CharField("3b. Enter your passport number", default="", max_length=128, blank=True, null=True)

    F8843L04Aa = models.IntegerField("2013", default=0, blank=True, null=True)
    F8843L04Ab = models.IntegerField("2012", default=0, blank=True, null=True)
    F8843L04Ac = models.IntegerField("2011", default=0, blank=True, null=True)
    F8843L04B = models.IntegerField("4b. Enter the number of days in 2013 you claim you can exclude for purposes of the substantial presence test", default=0, blank=True, null=True)

    F8843Teachers = models.BooleanField("Teachers and Trainees (Visa J or Q)", default=False)
    F8843TeachersL05 = models.CharField("5. For teachers, enter the name, address, and telephone number of the academic institution where you taught in 2013", default="", max_length=128, blank=True, null=True)
    F8843TeachersL06 = models.CharField("6. For trainees, enter the name, address, and telephone number of the director of the academic or other specialized program you participated in during 2013", default="", max_length=128, blank=True, null=True)
    F8843TeachersL07a = models.CharField("2007", default="", max_length=128, blank=True, null=True)
    F8843TeachersL07b = models.CharField("2008", default="", max_length=128, blank=True, null=True)
    F8843TeachersL07c = models.CharField("2009", default="", max_length=128, blank=True, null=True)
    F8843TeachersL07d = models.CharField("2010", default="", max_length=128, blank=True, null=True)
    F8843TeachersL07e = models.CharField("2011", default="", max_length=128, blank=True, null=True)
    F8843TeachersL07f = models.CharField("2012", default="", max_length=128, blank=True, null=True)
    F8843TeachersL08 = models.BooleanField("8. Were you present in the United States as a teacher, trainee, or student for any part of 2 of the 6 prior calendar years (2007 through 2012)?", default=False)

    F8843Students = models.BooleanField("Students (Visa F, J, M, or Q)", default=False)
    F8843StudentsL09 = models.CharField("9. Enter the name, address, and telephone number of the academic institution you attended during 2013", default="", max_length=128, blank=True, null=True)
    F8843StudentsL10 = models.CharField("10. Enter the name, address, and telephone number of the director of the academic or other specialized program you participated in during 2013", default="", max_length=128, blank=True, null=True)
    F8843StudentsL11a = models.CharField("2007", default="", max_length=128, blank=True, null=True)
    F8843StudentsL11b = models.CharField("2008", default="", max_length=128, blank=True, null=True)
    F8843StudentsL11c = models.CharField("2009", default="", max_length=128, blank=True, null=True)
    F8843StudentsL11d = models.CharField("2010", default="", max_length=128, blank=True, null=True)
    F8843StudentsL11e = models.CharField("2011", default="", max_length=128, blank=True, null=True)
    F8843StudentsL11f = models.CharField("2012", default="", max_length=128, blank=True, null=True)
    F8843StudentsL12 = models.BooleanField("12. Were you present in the United States as a teacher, trainee, or student for any part of more than 5 calendar years?", default=False)
    F8843StudentsL13 = models.BooleanField("13. During 2013, did you apply for, or take other affirmative steps to apply for, lawful permanent resident status", default=False)
    F8843StudentsL14 = models.CharField("14. If you checked the 'Yes' box on line 13, explain", default="", max_length=128, blank=True, null=True)
    
    F8843Athletes = models.BooleanField("Professional Athletes", default=False)
    F8843AthletesL15 = models.CharField("15. Enter the name of the charitable sports event(s) in the United States in which you competed during 2013 and the dates of competition", default="", max_length=128, blank=True, null=True)
    F8843AthletesL16 = models.CharField("16. Enter the name(s) and employer identification number(s) of the charitable organization(s) that benefited from the sports event(s)", default="", max_length=128, blank=True, null=True)
    F8843AthletesL16a = models.BooleanField("16a. Note. You must attach a statement to verify that all of the net proceeds of the sports event(s) were contributed to the charitable organization(s) listed on line 16.", default=False)
    F8843AthletesL17A = models.CharField("17a. Describe the medical condition or medical problem that prevented you from leaving the United States", default="", max_length=128, blank=True, null=True)
    F8843AthletesL17B = models.CharField("17b Enter the date you intended to leave the United States prior to the onset of the medical condition or medical problem described on line 17a", default="", max_length=128, blank=True, null=True)
    F8843AthletesL17C = models.CharField("17c. Enter the date you actually left the United States", default="", max_length=128, blank=True, null=True)
    
    F8843Medical = models.BooleanField("Individuals With a Medical Condition or Medical Problem", default=False)
    F8843MedicalL18a = models.CharField("18. Physician's Statement:", default="", max_length=128, blank=True, null=True)
    F8843MedicalL18b = models.CharField("Name of physician or other medical official", default="", max_length=128, blank=True, null=True)
    F8843MedicalL18c = models.CharField("Physician's or other medical official's address and telephone number", default="", max_length=128, blank=True, null=True)

class modelF8843(models.Model):
    # F8843 fields
    F8843L01A = models.CharField("Type of U.S. visa (for example, F, J, M, Q, etc.) and date you entered the United States", default="", max_length=128)
    F8843L01B = models.CharField("Current nonimmigrant status and date of change (see instructions)", default="", max_length=128)
    F8843L02 = models.CharField("Of what country were you a citizen during the tax year?", default="", max_length=128)
    F8843L03A = models.CharField("What country issued you a passport?", default="", max_length=128)
    F8843L03B = models.CharField("Enter your passport number", default="", max_length=128)
    F8843L04Aa = models.IntegerField("2013", default=0)
    F8843L04Ab = models.IntegerField("2012", default=0)
    F8843L04Ac = models.IntegerField("2011", default=0)
    F8843L04B = models.IntegerField("Enter the number of days in 2013 you claim you can exclude for purposes of the substantial presence test", default=0)
    F8843L05 = models.CharField("For teachers, enter the name, address, and telephone number of the academic institution where you taught in 2013", default="", max_length=128)
    F8843L06 = models.CharField("For trainees, enter the name, address, and telephone number of the director of the academic or other specialized program you participated in during 2013", default="", max_length=128)
    F8843L07a = models.CharField("2007", default="", max_length=128)
    F8843L07b = models.CharField("2008", default="", max_length=128)
    F8843L07c = models.CharField("2009", default="", max_length=128)
    F8843L07d = models.CharField("2010", default="", max_length=128)
    F8843L07e = models.CharField("2011", default="", max_length=128)
    F8843L07f = models.CharField("2012", default="", max_length=128)
    F8843L08 = models.BooleanField("Were you present in the United States as a teacher, trainee, or student for any part of 2 of the 6 prior calendar years (2007 through 2012)?", default=False)
    F8843L09 = models.CharField("Enter the name, address, and telephone number of the academic institution you attended during 2013", default="", max_length=128)
    F8843L10 = models.CharField("Enter the name, address, and telephone number of the director of the academic or other specialized program you participated in during 2013", default="", max_length=128)
    F8843L11a = models.CharField("2007", default="", max_length=128)
    F8843L11b = models.CharField("2008", default="", max_length=128)
    F8843L11c = models.CharField("2009", default="", max_length=128)
    F8843L11d = models.CharField("2010", default="", max_length=128)
    F8843L11e = models.CharField("2011", default="", max_length=128)
    F8843L11f = models.CharField("2012", default="", max_length=128)
    F8843L12 = models.BooleanField("Were you present in the United States as a teacher, trainee, or student for any part of more than 5 calendar years?", default=False)
    F8843L13 = models.BooleanField("During 2013, did you apply for, or take other affirmative steps to apply for, lawful permanent resident status", default=False)
    F8843L14 = models.CharField("If you checked the 'Yes' box on line 13, explain", default="", max_length=128)
    F8843L15 = models.CharField("Enter the name of the charitable sports event(s) in the United States in which you competed during 2013 and the dates of competition", default="", max_length=128)
    F8843L16 = models.CharField("Enter the name(s) and employer identification number(s) of the charitable organization(s) that benefited from the sports event(s)", default="", max_length=128)
    F8843L16a = models.BooleanField("Note. You must attach a statement to verify that all of the net proceeds of the sports event(s) were contributed to the charitable organization(s) listed on line 16.", default=False)
    F8843L17A = models.CharField("Describe the medical condition or medical problem that prevented you from leaving the United States", default="", max_length=128)
    F8843L17B = models.CharField("Enter the date you intended to leave the United States prior to the onset of the medical condition or medical problem described on line 17a", default="", max_length=128)
    F8843L17C = models.CharField("Enter the date you actually left the United States", default="", max_length=128)
    F8843L18a = models.CharField("Physician's Statement:", default="", max_length=128)
    F8843L18b = models.CharField("Name of physician or other medical official", default="", max_length=128)
    F8843L18c = models.CharField("Physician's or other medical official's address and telephone number", default="", max_length=128)

class modelInput(models.Model):
   
    # text input
    A01 = models.CharField("First Name", max_length=128, blank=True, null=True)
    A02 = models.CharField("Last Name", max_length=128, blank=True, null=True)
    
    # choose one
    CHOICES_Q01 = (("a", "Current Year"), ("b", "Prior Year(s)"),)
    Q01 = models.CharField("Please select tax year", max_length=128, choices = CHOICES_Q01, blank=True, null = True)
    
    # choose one
    CHOICES_Q01_01 = (("a", "2010"), ("b", "2011"), ("c", "2012"),)
    Q01_01 = models.CharField("Please select a prior tax year", max_length=128, choices = CHOICES_Q01_01, blank=True, null = True)
    
    # choose one
    CHOICES_Q02 = (("a", "Nonresident Tax Return"), ("b", "Social Security & Medicare Tax Refunds"),)
    Q02 = models.CharField("Please select your service need:", max_length=128, choices = CHOICES_Q02, blank=True, null = True)
	
    # choose one
    CHOICES_Q02_01 = (("a", "China"), ("b", "Mexico"),)
    Q02_01 = models.CharField("Please select your country of origin: ", max_length=128, choices = CHOICES_Q02_01, blank=True, null = True)
	
    # read-only
    Q02_01_01 = models.IntegerField("Tax Treaty Amount:", max_length=128, blank=True, null = True)
	
    # choose one
    CHOICES_Q03 = (("a", "1040NR-EZ"), ("b", "1040NR"),)
    Q03 = models.CharField("Please select your forms:", max_length=128, choices = CHOICES_Q03, blank=True, null = True)
	
    # choose one
    CHOICES_Q03_01 = (("a", "Single"), ("b", "Married"),)
    Q03_01 = models.CharField("What do you want to file as?", max_length=128, choices = CHOICES_Q03_01, blank=True, null = True)
    
    # read-only
    Q03_01_01 = models.IntegerField("Personal Exemption:", max_length=128, blank=True, null = True)
    
    # read-only
    Q03_01_02 = models.IntegerField("Standard Deviation:", max_length=128, blank=True, null = True)

    # choose many
    Q04 = models.CharField("Please select source of income:", max_length=128, blank=True, null = True)
    Q04_a = models.BooleanField("W2 - check to expand", max_length=128, default=False)
    Q04_b = models.BooleanField("1099G - check to expand", max_length=128, default=False)

    W2L01 = models.IntegerField("Box 1: Wages, tips, other comp.", blank=True, null=True, default=0)
    W2L02 = models.IntegerField("Box 2: Federal income tax withheld", blank=True, null=True, default=0)
    W2L03 = models.IntegerField("Box 3: Social security wages", blank=True, null=True, default=0)
    W2L04 = models.IntegerField("Box 4: Social security tax withheld", blank=True, null=True, default=0)
    W2L05 = models.IntegerField("Box 5: Medicare wages and tips", blank=True, null=True, default=0)
    W2L06 = models.IntegerField("Box 6: Medicare tax withheld", blank=True, null=True, default=0)
    W2L12aB = models.IntegerField("Box 12a: Enter code and amount", blank=True, null=True, default=0)
    W2L12bB = models.IntegerField("Box 12b: Enter code and amount", blank=True, null=True, default=0)
    W2L15aA = models.IntegerField("Box 15a: State", blank=True, null=True, default=0)
    W2L15bA = models.IntegerField("Box 15b: Employer's state ID number", blank=True, null=True, default=0)
    W2L16A = models.IntegerField("Box 16: State wages, tips, etc.", blank=True, null=True, default=0)
    W2L17A = models.IntegerField("Box 17: State income tax", blank=True, null=True, default=0)
    W2L18A = models.IntegerField("Box 18: Local wages, tips, etc.", blank=True, null=True, default=0)
    W2L19A = models.IntegerField("Box 19: Local income tax", blank=True, null=True, default=0)
    W2L20A = models.IntegerField("Box 20: Locality name", blank=True, null=True, default=0)
    W2L07 = models.IntegerField("Box 7: Social security tips", blank=True, null=True, default=0)
    W2L08 = models.IntegerField("Box 8: Allocated tips", blank=True, null=True, default=0)
    W2L10 = models.IntegerField("Box 10: Dependent care benefits", blank=True, null=True, default=0)
    W2L11 = models.IntegerField("Box 11: Nonqualified plans", blank=True, null=True, default=0)
    W2L14 = models.IntegerField("Box 14: Other", blank=True, null=True, default=0)

    F1099GL01 = models.IntegerField("Box 1: Unemployment compensation OR Recipient's identification number:", blank=True, null=True, default=0)
    F1099GL02 = models.IntegerField("Box 2: State or local income tax refunds, credits, or offsets", blank=True, null=True, default=0)
    F1099GL03 = models.IntegerField("Box 3: Box 2 amount is for tax year", blank=True, null=True, default=0)
    F1099GL04 = models.IntegerField("Box 4: Federal income tax withheld", blank=True, null=True, default=0)
    F1099GL05 = models.IntegerField("Box 5: RTAA payments", blank=True, null=True, default=0)
    F1099GL06 = models.IntegerField("Box 6: Taxable grants", blank=True, null=True, default=0)
    F1099GL07 = models.IntegerField("Box 7: Agriculture payments", blank=True, null=True, default=0)
    F1099GL08 = models.IntegerField("Box 8: Check if box 2 is trade or business", blank=True, null=True, default=0)
    F1099GL09 = models.IntegerField("Box 9: Market Gain", blank=True, null=True, default=0)
    F1099GL10aA = models.IntegerField("Box 10a: State", blank=True, null=True, default=0)
    F1099GL10bA = models.IntegerField("Box 10b: State identification no.", blank=True, null=True, default=0)
    F1099GL11A = models.IntegerField("Box 11: State income tax withheld", blank=True, null=True, default=0)

    def __unicode__(self):
        return self.A01 + " " + self.A02
        
        