from fdfgen import forge_fdf
from app1040nrezlocal.models import modelInput, model1040NREZ, modelF8843, modelPostTaxInput

# function to asscoiate 1040NREZ form with user input
def inputTo1040NREZ():
    
    # create new 1040NREZ form record
    f = model1040NREZ.objects.create()
    
    # retrieve the relevant Input record
    # TODO: use session ID instead of max ID
    i = modelInput.objects.all().order_by("-id")[0]
    
    # field association/ calculation
    # TODO: associate all fields
    f.refnum = i.id
    f.INFOL01 = i.A01
    f.INFOL02 = i.A02
    # single or married
    if i.Q03_01 == 'a':
        f.F1040NREZL01 = True
    if i.Q03_01 == 'b':
        f.F1040NREZL02 = True
    single = helper_single_or_married(f.F1040NREZL01, f.F1040NREZL02)
    f.F1040NREZL03 = i.W2L01
    f.F1040NREZL04 = 50 #hardcode
    f.F1040NREZL05 = 0
    # TODO: get L06 from Schedule OI
    if i.Q02_01 == 'a':
        f.F1040NREZL06 = 5000
    if i.Q02_01 == 'b':
        f.F1040NREZL06 = 3000
    f.F1040NREZL07 = f.F1040NREZL03 + f.F1040NREZL04 + f.F1040NREZL05 + f.F1040NREZL06
    f.F1040NREZL08 = 0
    f.F1040NREZL09 = helper_F1040NREZL09(f.F1040NREZL07, f.F1040NREZL08, single)
    f.F1040NREZL10 = f.F1040NREZL07 - (f.F1040NREZL08 + f.F1040NREZL09)
    f.F1040NREZL11 = helper_F1040NREZL11(i.W2L17A, i.W2L19A, i.F1099GL11A, f.F1040NREZL10, single)
    f.F1040NREZL12 = f.F1040NREZL10 - f.F1040NREZL11
    f.F1040NREZL13 = helper_F1040NREZL13(f.F1040NREZL10, single)
    f.F1040NREZL14 = max(f.F1040NREZL12 - f.F1040NREZL13, 0)
    f.F1040NREZL15 = helper_tax_table(f.F1040NREZL14, single)
    f.F1040NREZL16 = 0
    f.F1040NREZL16a = 0
    f.F1040NREZL16b = 0
    f.F1040NREZL17 = f.F1040NREZL15 + f.F1040NREZL16
    f.F1040NREZL18a = 0
    f.F1040NREZL18b = 0
    f.F1040NREZL19 = 0
    f.F1040NREZL20 = 0
    f.F1040NREZL21 = f.F1040NREZL18a + f.F1040NREZL18b + f.F1040NREZL19 + f.F1040NREZL20
    f.F1040NREZL22 = max(f.F1040NREZL21 - f.F1040NREZL17, 0)
    f.F1040NREZL23a = 0
    f.F1040NREZL23b = 0
    f.F1040NREZL23c = 0
    f.F1040NREZL23d = 0
    f.F1040NREZL23e = 0
    f.F1040NREZL24 = 0
    f.F1040NREZL25 = max(f.F1040NREZL17 - f.F1040NREZL21, 0)
    f.F1040NREZL26 = 0

    f.save()


# for filling up Schedule OI    
def postTaxTo1040NREZ():
    # retrieve the relevant record
    # TODO: use session ID instead of max ID
    f = model1040NREZ.objects.all().order_by("-id")[0]
    
    # retrieve the relevant record
    # TODO: use session ID instead of max ID
    i = modelPostTaxInput.objects.all().order_by("-id")[0]
    
    # field association/ calculation
    # TODO: associate all fields
    f.F1040NREZSCHOILA = i.SCHOILA
    f.F1040NREZSCHOILB = i.SCHOILB
    f.F1040NREZSCHOILC = i.SCHOILC
    f.F1040NREZSCHOILD1 = i.SCHOILD1
    f.F1040NREZSCHOILD2 = i.SCHOILD2
    f.F1040NREZSCHOILE = i.SCHOILE
    f.F1040NREZSCHOILF = i.SCHOILF
    f.F1040NREZSCHOILFc = i.SCHOILFc
    f.F1040NREZSCHOILGa = i.SCHOILGa
    f.F1040NREZSCHOILGb = i.SCHOILGb
    f.F1040NREZSCHOILGc = i.SCHOILGc
    f.F1040NREZSCHOILGd = i.SCHOILGd
    f.F1040NREZSCHOILHa = i.SCHOILHa
    f.F1040NREZSCHOILHb = i.SCHOILHb
    f.F1040NREZSCHOILHc = i.SCHOILHc
    f.F1040NREZSCHOILI = i.SCHOILI
    f.F1040NREZSCHOILIc = i.SCHOILIc
    
    f.save()
    
def postTaxtoF8843():
    # create new form record
    f = modelF8843.objects.create()

    # retrieve the relevant record
    # TODO: use session ID instead of max ID
    i = modelPostTaxInput.objects.all().order_by("-id")[0]

    # field association/ calculation
    # TODO: associate all fields
    f.F8843L01A = i.F8843L01A
    
    f.save()

# helper function to convert single from 1040NREZ to a true/ false value
def helper_single_or_married(arg1, arg2): 
    # arg1 = f.F1040NREZL01 (single)
    # arg2 = f.F1040NREZL02 (married)
    single = True
    if arg1 == True:
        single = True
    if arg2 == True:
        single = False
    return single

# helper function to get F1040NREZL09
def helper_F1040NREZL09(arg1, arg2, arg3):

    F1040NREZL09WPL01 = 1987 #hardcode
    F1040NREZL09WPL02 = arg1
    F1040NREZL09WPL03 = arg2
    F1040NREZL09WPL04 = F1040NREZL09WPL02 - F1040NREZL09WPL03
    
    if F1040NREZL09WPL04 > 60000:
        F1040NREZL09WPL05 = F1040NREZL09WPL04 - 60000
        # TODO: ensure L06 is a decimal
        F1040NREZL09WPL06 = F1040NREZL09WPL05 / 15000
        F1040NREZL09WPL07 = F1040NREZL09WPL01 * F1040NREZL09WPL06
    else:
        F1040NREZL09WPL07 = 0
        
    # TODO - paid int, single, AGI<75000
    qualified = True;
        
    if qualified: 
        F1040NREZL09WPL08 = F1040NREZL09WPL01 - F1040NREZL09WPL07
    else:
        F1040NREZL09WPL08 = 0
        
    return F1040NREZL09WPL08
    
# helper function to get F1040NREZL11
def helper_F1040NREZL11(arg1, arg2, arg3, arg4, arg5):
    # TODO: W2L17T = W2L17A + W2L17B + W2L17C
    # arg1 = W2L17A
    # arg2 = W2L19A
    # arg3 = F1099GL11A
    # arg4 = F1040NREZL10
    # arg5 = single/married
    F1040NREZL11WPL01 = arg1 + arg2 + arg3
    F1040NREZL11WPL02 = F1040NREZL11WPL01 * 0.8
    F1040NREZL11WPL03 = arg4
    # TODO: check marry status (add an arg)
    single = arg5
    if single:
        F1040NREZL11WPL04 = 150000
    else:
        F1040NREZL11WPL04 = 250000
    if (F1040NREZL11WPL03 > F1040NREZL11WPL04):
        F1040NREZL11WPL05 = F1040NREZL11WPL03 - F1040NREZL11WPL04
    else:
        F1040NREZL11WPL05 = 0
    F1040NREZL11WPL06 = F1040NREZL11WPL05 * 0.03
    F1040NREZL11WPL07 = min(F1040NREZL11WPL02, F1040NREZL11WPL06)
    F1040NREZL11WPL08 = F1040NREZL11WPL01 - F1040NREZL11WPL07
    return F1040NREZL11WPL08

# helper function to get F1040NREZL13
def helper_F1040NREZL13(arg1, arg2):
# arg1 = F1040NREZL10
# arg2 = single
    # TODO: check marry status (add an arg)
    single = arg2
    if single:
        F1040NREZL13WPL04 = 150000
    else:
        F1040NREZL13WPL04 = 250000
        
    if arg1 > F1040NREZL13WPL04:
        F1040NREZL13WPL03 = arg1
    else:
        return 3900  
        
    F1040NREZL13WPL02 = 3900 #PE, constant
    
    F1040NREZL13WPL05 = F1040NREZL13WPL03 - F1040NREZL13WPL04
    
    if single:
        if F1040NREZL13WPL05 > 61250:
            return 0
        else:
            F1040NREZL13WPL06 = F1040NREZL13WPL05 / 1250
    else:
        if F1040NREZL13WPL05 > 122500:
            return 0
        else:
            F1040NREZL13WPL06 = F1040NREZL13WPL05 / 2500     
    
    F1040NREZL13WPL07 = F1040NREZL13WPL06 * 0.02
    
    F1040NREZL13WPL08 = F1040NREZL13WPL02 * F1040NREZL13WPL07
    
    F1040NREZL13WPL09 = F1040NREZL13WPL02 - F1040NREZL13WPL08
    
    return F1040NREZL13WPL09

# helper function to get F1040NREZL15
def helper_tax_table(arg1, arg2):
# arg1 = L14
# arg2 = single/ married
    L14 = arg1
    single = arg2
    if single:
        if L14 < 8925:
            L15 = L14 * 0.1
        elif L14 < 36250:
            L15 = L14 * 0.15 + 892.50
        elif L14 < 87850:
            L15 = L14 * 0.25 + 4991.25
        elif L14 < 183250:
            L15 = L14 * 0.28 + 17891.25
        elif L14 < 398350:
            L15 = L14 * 0.33 + 44603.25
        elif L14 < 400000:
            L15 = L14 * 0.35 + 115586.25
        else:
            L15 = L14 * 0.396 + 116164.75
    else:
        if L14 < 17850:
            L15 = L14 * 0.1
        elif L14 < 72500:
            L15 = L14 * 0.15 + 1785.00
        elif L14 < 146400:
            L15 = L14 * 0.25 + 9982.50
        elif L14 < 223050:
            L15 = L14 * 0.28 + 28457.50
        elif L14 < 398350:
            L15 = L14 * 0.33 + 49919.50
        elif L14 < 450000:
            L15 = L14 * 0.35 + 107768.50
        else:
            L15 = L14 * 0.396 + 125846.00   
            
    return L15
        
    
# generate fdf file for PDFtk use - F1040NREZ
def generate_fdf():
    
    # TODO: use session ID instead of max ID
    f = model1040NREZ.objects.all().order_by("-id")[0]
    
    boolean_tuple = []
    
    single = helper_single_or_married(f.F1040NREZL01, f.F1040NREZL02)
    if single:
        boolean_tuple+=[('topmostSubform[0].Page1[0].c1_2_0_[0]', 1)]
    else:
        boolean_tuple+=[('topmostSubform[0].Page1[0].c1_2_0_[1]', 2)]
    
    # SchOI_C "have you ever.. green card"?    
    if f.F1040NREZSCHOILC == 0:
        # No
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_01_0_[1]', 2)]
    else:
        # yes
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_01_0_[0]', 1)]
    
    # SchOI_D1 "A US Citizen"?
    if f.F1040NREZSCHOILD1 == 0:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_35_0_[1]', 2)]
    else:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_35_0_[0]', 1)]
    
    # SchOI_D2 "A greencard holder"?
    if f.F1040NREZSCHOILD2 == 0:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_37_0_[1]', 2)]
    else:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_37_0_[0]', 1)]
    
    # SchOI_F "Changed Visa Type"?
    if f.F1040NREZSCHOILF == 0:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_36_0_[1]', 2)]
    else:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_36_0_[0]', 1)]
    
    # SchOI_G "Resident of Canada or Mexico"?
    if f.F1040NREZSCHOILGa == 1:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_38_0_[0]', 1)]
    if f.F1040NREZSCHOILGb == 1:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_38_0_[1]', 2)]
    
    # SchOI_I "File return prior year"?
    if f.F1040NREZSCHOILI == 0:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_22_0_[1]', 2)]
    else:
        boolean_tuple+=[('topmostSubform[0].Page2[0].c2_22_0_[0]', 1)]
     

        
    # ---
    # FieldName: topmostSubform[0].Page2[0].c2_01_0_[0]
    # FieldStateOption: 1
    # ---
    # FieldName: topmostSubform[0].Page2[0].c2_01_0_[1]
    # FieldStateOption: 2
    # ---       
    fields = [('topmostSubform[0].Page1[0].f1_01_0_[0]', f.INFOL01),
            ('topmostSubform[0].Page1[0].f1_02_0_[0]', f.INFOL02), 
             ('topmostSubform[0].Page1[0].f1_10_0_[0]', f.F1040NREZL03), 
             ('topmostSubform[0].Page1[0].f1_12_0_[0]', f.F1040NREZL04), 
             ('topmostSubform[0].Page1[0].f1_14_0_[0]', f.F1040NREZL05), 
             ('topmostSubform[0].Page1[0].f1_16_0_[0]', f.F1040NREZL06), 
             ('topmostSubform[0].Page1[0].f1_18_0_[0]', f.F1040NREZL07), 
             ('topmostSubform[0].Page1[0].f1_20_0_[0]', f.F1040NREZL08), 
             ('topmostSubform[0].Page1[0].f1_22_0_[0]', f.F1040NREZL09), 
             ('topmostSubform[0].Page1[0].f1_24_0_[0]', f.F1040NREZL10), 
             ('topmostSubform[0].Page1[0].f1_26_0_[0]', f.F1040NREZL11), 
             ('topmostSubform[0].Page1[0].f1_28_0_[0]', f.F1040NREZL12), 
             ('topmostSubform[0].Page1[0].f1_30_0_[0]', f.F1040NREZL13), 
             ('topmostSubform[0].Page1[0].f1_32_0_[0]', f.F1040NREZL14), 
             ('topmostSubform[0].Page1[0].f1_34_0_[0]', f.F1040NREZL15), 
             ('topmostSubform[0].Page1[0].f1_36_0_[0]', f.F1040NREZL16), 
             ('topmostSubform[0].Page1[0].f1_38_0_[0]', f.F1040NREZL17), 
             ('topmostSubform[0].Page1[0].f1_40_0_[0]', f.F1040NREZL18a), 
             ('topmostSubform[0].Page1[0].f1_100_0_[0]', f.F1040NREZL18b), 
             ('topmostSubform[0].Page1[0].f1_42_0_[0]', f.F1040NREZL19), 
             ('topmostSubform[0].Page1[0].f1_44_0_[0]', f.F1040NREZL20), 
             ('topmostSubform[0].Page1[0].f1_46_0_[0]', f.F1040NREZL21), 
             ('topmostSubform[0].Page1[0].f1_48_0_[0]', f.F1040NREZL22), 
             ('topmostSubform[0].Page1[0].f1_50_0_[0]', f.F1040NREZL23a), 
             ('topmostSubform[0].Page1[0].f1_54_0_[0]', f.F1040NREZL24), 
             ('topmostSubform[0].Page1[0].f1_56_0_[0]', f.F1040NREZL25),
             ('topmostSubform[0].Page1[0].f1_58_0_[0]', f.F1040NREZL26), 

            # Schdule OI: CharField, DateField and IntegerField
             ('topmostSubform[0].Page2[0].f2_01_0_[0]', f.F1040NREZSCHOILA), 
             ('topmostSubform[0].Page2[0].f2_02_0_[0]', f.F1040NREZSCHOILB), 
             ('topmostSubform[0].Page2[0].f2_19_0_[0]', f.F1040NREZSCHOILE), 
             ('topmostSubform[0].Page2[0].f2_18_0_[0]', f.F1040NREZSCHOILFc), 
             ('topmostSubform[0].Page2[0].Table_LineG-1[0].Row1[0].f2_019_0_[0]', f.F1040NREZSCHOILGc), 
             ('topmostSubform[0].Page2[0].Table_LineG-1[0].Row1[0].f2_22_0_[0]', f.F1040NREZSCHOILGd), 
             ('topmostSubform[0].Page2[0].f2_15_0_[0]', f.F1040NREZSCHOILHa), 
             ('topmostSubform[0].Page2[0].f2_16_0_[0]', f.F1040NREZSCHOILHb), 
             ('topmostSubform[0].Page2[0].f2_17_0_[0]', f.F1040NREZSCHOILHc), 
             ('topmostSubform[0].Page2[0].f2_100_0_[0]', f.F1040NREZSCHOILIc),]    
    
    fields += boolean_tuple
    
    fdf = forge_fdf("",fields,[],[],[])
    # TODO: include session ID in fdf file name
    fdf_file = open("data.fdf","w")
    fdf_file.write(fdf)
    fdf_file.close()

# generate fdf file for PDFtk use - F8843
def generate_F8843_fdf():
    # TODO: use session ID instead of max ID
    f = modelF8843.objects.all().order_by("-id")[0]
    fields = [('topmostSubform[0].Page1[0].f1_09_0_[0]',f.F8843L01A),]
    
    fdf = forge_fdf("",fields,[],[],[])
    # TODO: include session ID in fdf file name
    fdf_file = open("f8843_data.fdf","w")
    fdf_file.write(fdf)
    fdf_file.close()