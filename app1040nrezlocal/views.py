from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from app1040nrezlocal.models import modelInput, modelSummary, model1040NREZ
from app1040nrezlocal.forms import TaxModelForm
from app1040nrezlocal.view_helper import generate_fdf, inputTo1040NREZ, helper_single_or_married
import subprocess

def index(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = TaxModelForm(request.POST or None)

        # Have we been provided with a valid form?
        if form.is_valid():

            # fAdd = form.save(commit=False)
            # calculation logic
            # fAdd.save()
            form.save()
           
            # view helper methods
            inputTo1040NREZ()
            generate_fdf()
            # call PDFTK
            subprocess.call(['pdftk', 'f1040nre.pdf', 'fill_form', 'data.fdf', 'output', 'static/f1040nre_output.pdf'])
			
            return summary(request)
            #return outputPdf(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = TaxModelForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('app1040nrezlocal/index.html', {'form': form}, context)
	
def outputPdf(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('app1040nrezlocal/output_pdf.html', context_dict, context)
	
def styled(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('app1040nrezlocal/styled.html', context_dict, context)

def summary(request):
    context = RequestContext(request)
    
    # create new summary record
    s = modelSummary.objects.create()
    
    # retrieve the relevant Input record
    # TODO: use session ID instead of max ID
    f = model1040NREZ.objects.all().order_by("-id")[0]    
    i = modelInput.objects.all().order_by("-id")[0] 
    
    # field association/ calculation
    single = helper_single_or_married(f.F1040NREZL01, f.F1040NREZL02)
    if single:
        s.SUMMARY01 = "Single nonresident alien"
    else:
        s.SUMMARY01 = "Married nonresident alien"
    s.SUMMARY02 = f.F1040NREZL03 + f.F1040NREZL04 + f.F1040NREZL05
    s.SUMMARY03 = f.F1040NREZL06 + f.F1040NREZL13 + f.F1040NREZL11 + f.F1040NREZL09 + f.F1040NREZL08
    s.SUMMARY03a = f.F1040NREZL06
    # 'a' = China, 'b' = Mexico
    if i.Q03_01 == 'a':
        s.SUMMARY03aa = "China"
    if i.Q03_01 == 'b':
        s.SUMMARY03aa = "Mexico"
    s.SUMMARY03b = f.F1040NREZL13
    s.SUMMARY03c = f.F1040NREZL11
    s.SUMMARY03d = f.F1040NREZL09
    s.SUMMARY03e = f.F1040NREZL08
    s.SUMMARY04 = f.F1040NREZL14
    s.SUMMARY05 = f.F1040NREZL15
    s.SUMMARY06 = f.F1040NREZL16
    s.SUMMARY07 = f.F1040NREZL17
    s.SUMMARY08 = f.F1040NREZL21
    s.SUMMARY09a = f.F1040NREZL22
    s.SUMMARY09b = f.F1040NREZL25
    
    #TODO - hide if 0
    
    context_dict = {'SUMMARY01': s.SUMMARY01,
        'SUMMARY02': s.SUMMARY02,
        'SUMMARY03': s.SUMMARY03,
        'SUMMARY03a': s.SUMMARY03a,
        'SUMMARY03aa': s.SUMMARY03aa,
        'SUMMARY03b': s.SUMMARY03b,
        'SUMMARY03c': s.SUMMARY03c,
        'SUMMARY03d': s.SUMMARY03d,
        'SUMMARY03e': s.SUMMARY03e,
        'SUMMARY04': s.SUMMARY04,
        'SUMMARY05': s.SUMMARY05,
        'SUMMARY06': s.SUMMARY06,
        'SUMMARY07': s.SUMMARY07,
        'SUMMARY08': s.SUMMARY08,
        'SUMMARY09a': s.SUMMARY09a,
        'SUMMARY09a': s.SUMMARY09b,}
        
    return render_to_response('app1040nrezlocal/summary.html', context_dict, context)