from fdfgen import forge_fdf
from app1040nrezlocal.models import modelInput

def generate():
    
    t = modelInput.objects.all().order_by("-id")[0]
	
    fields = [('topmostSubform[0].Page1[0].f1_01_0_[0]', t.A01),('topmostSubform[0].Page1[0].f1_02_0_[0]',t.A02)]
    fdf = forge_fdf("",fields,[],[],[])
    fdf_file = open("data.fdf","w")
    fdf_file.write(fdf)
    fdf_file.close()
