from fdfgen import forge_fdf
from app1040nrezlocal.models import modelInput, model1040NREZ

# function to asscoiate 1040NREZ form with user input
def inputTo1040NREZ():
    
    # create new 1040NREZ form record
    f = model1040NREZ.objects.create()
    
    # retrieve the relevant Input record
    # TODO: use session ID instead of max ID
    i = modelInput.objects.all().order_by("-id")[0]
    
    # field association/ calculation
    f.refnum = i.id
    f.INFOL01 = i.A01
    f.INFOL02 = i.A02
    f.F1040NREZL03 = i.Q04_01_BOX1
    f.F1040NREZL04 = 50 #hardcode
    f.F1040NREZL05 = 0
    f.F1040NREZL06 = 0
    f.F1040NREZL07 = f.F1040NREZL03 + f.F1040NREZL04 + f.F1040NREZL05 + f.F1040NREZL06
    f.F1040NREZL08 = 0
    f.F1040NREZL09 = helper_F1040NREZL09(f.F1040NREZL07, f.F1040NREZL08)
    f.F1040NREZL10 = f.F1040NREZL07 - (f.F1040NREZL08 + f.F1040NREZL09)
    f.F1040NREZL11 = 0 #function
    f.F1040NREZL12 = f.F1040NREZL10 - f.F1040NREZL11
    f.F1040NREZL13 = 0 #function
    f.F1040NREZL14 = max(f.F1040NREZL12 - f.F1040NREZL13, 0)
    f.F1040NREZL15 = 1000 #hardcode
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
    
# helper function to get F1040NREZL09
def helper_F1040NREZL09(arg1, arg2):

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
def helper_F1040NREZL11(arg1):
    F1040NREZL11WPL01 = 999 # TODO: W2L17T + W2L19T + F1099GL11T
    F1040NREZL11WPL02 = F1040NREZL11WPL01 * 0.8
    F1040NREZL11WPL03 = arg1 #F1040NREZL10
    # TODO: check marry status
    single = True
    if single:
        F1040NREZL11WPL04 = 150000
    else:
        F1040NREZL11WPL04 = 250000
     
# helper function to get F1040NREZL13
# def helper_F1040NREZL13():


def generate_fdf():
    
    # TODO: use session ID instead of max ID
    f = model1040NREZ.objects.all().order_by("-id")[0]
	
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
            ('topmostSubform[0].Page1[0].f1_58_0_[0]', f.F1040NREZL26)]    
            
    fdf = forge_fdf("",fields,[],[],[])
    # TODO: include session ID in fdf file
    fdf_file = open("data.fdf","w")
    fdf_file.write(fdf)
    fdf_file.close()
