from fdfgen import forge_fdf
from app1040nrezlocal.models import modelInput, model1040NREZ

def inputTo1040NREZ():
    
    f = model1040NREZ.objects.create()
    i = modelInput.objects.all().order_by("-id")[0]
    
    # TODO: use session ID instead of max ID
    f.refnum = i.id
    f.INFOL01 = i.A01
    f.INFOL02 = i.A02
    f.F1040NREZL03 = i.Q04_01_BOX1
    f.F1040NREZL04 = 100
    f.F1040NREZL05 = 0
    f.F1040NREZL06 = 0
    f.F1040NREZL07 = f.F1040NREZL03 + f.F1040NREZL04 + f.F1040NREZL05 + f.F1040NREZL06

    f.save()

def generate_fdf():
    
    # TODO: use session ID instead of max ID
    f = model1040NREZ.objects.all().order_by("-id")[0]
	
    fields = [('topmostSubform[0].Page1[0].f1_01_0_[0]', f.INFOL01),
            ('topmostSubform[0].Page1[0].f1_02_0_[0]', f.INFOL02), 
             ('topmostSubform[0].Page1[0].f1_10_0_[0]', f.F1040NREZL03), 
             ('topmostSubform[0].Page1[0].f1_12_0_[0]', f.F1040NREZL04), 
             ('topmostSubform[0].Page1[0].f1_14_0_[0]', f.F1040NREZL05), 
             ('topmostSubform[0].Page1[0].f1_16_0_[0]', f.F1040NREZL06), 
            ('topmostSubform[0].Page1[0].f1_18_0_[0]', f.F1040NREZL07)]    
            
    fdf = forge_fdf("",fields,[],[],[])
    # TODO: include session ID in fdf file
    fdf_file = open("data.fdf","w")
    fdf_file.write(fdf)
    fdf_file.close()
