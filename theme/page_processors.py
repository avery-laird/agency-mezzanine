from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import HomePage, messages
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name *'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email *'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Phone *'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message *'}))    

@processor_for(HomePage)
def author_form(request, page):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form processing goes here.
	    message = messages(name = form.data['name'], email = form.data['email'], phone = form.data['phone'], message = form.data['message'])
	    message.save()
	    # form.save()
	    redirect = request.path
            return HttpResponseRedirect(redirect)
    return {"form": form}
