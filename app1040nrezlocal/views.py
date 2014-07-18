from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response

from app1040nrezlocal.models import modelInput
from app1040nrezlocal.forms import TaxModelForm

from app1040nrezlocal.gen_fdf import generate
import subprocess

def index(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = TaxModelForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():

            # fAdd = form.save(commit=False)
            # tax calculation logic
            # fAdd.L07 = fAdd.L03 + fAdd.L04 + fAdd.L05 + fAdd.L06
            # fAdd.L10 = fAdd.L07 - fAdd.L08 - fAdd.L09
            # fAdd.L12 = fAdd.L10 - fAdd.L11
			
            # if (fAdd.L12 - fAdd.L13) > 0:
                # fAdd.L14 = fAdd.L12 - fAdd.L13
            # else:
                # fAdd.L14 = 0
			
            # fAdd.L15 = fAdd.L14 * 0.1			
            # fAdd.L17 = fAdd.L15 + fAdd.L16	
            # fAdd.L21 = fAdd.L18a + fAdd.L18b + fAdd.L19 + fAdd.L20			

            # if (fAdd.L21 - fAdd.L17) > 0:
                # fAdd.L22 = fAdd.L21 - fAdd.L17
            # else:
                # fAdd.L22 = 0	

            # if (fAdd.L17 - fAdd.L21) > 0:
                # fAdd.L25 = fAdd.L17 - fAdd.L21
            # else:
                # fAdd.L25 = 0
				
		    # Save the new category to the database.				
            # fAdd.save()
            form.save()
           
            # generate FDF
            generate()
            # call PDFTK
            subprocess.call(['pdftk', 'f1040nre.pdf', 'fill_form', 'data.fdf', 'output', 'static/f1040nre_output.pdf'])
			
            return outputPdf(request)
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