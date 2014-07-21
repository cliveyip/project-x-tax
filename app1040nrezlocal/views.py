from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response

from app1040nrezlocal.models import modelInput
from app1040nrezlocal.forms import TaxModelForm

from app1040nrezlocal.view_helper import generate_fdf, inputTo1040NREZ
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