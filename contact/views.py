from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm

def contact(request):
	title = "Contact Us"
	form = ContactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		comment = form.cleaned_data['comment']
		name =  form.cleaned_data['name']
		frm =  form.cleaned_data['email']
		sbj = 'Message from Seven.com'
		msg = '%s %s' %(comment, name)
		to_us = [settings.EMAIL_HOST_USER]
		send_mail(sbj, msg, frm, to_us, fail_silently=True)
		
		title = 'Thank you'
		confirm_message = '''
		Thank you for your message.  We have received it and we are reviewing it.
		'''
		form = None

	context = {
		'title': title,
		'form': form,
		'confirm_message': confirm_message,
	}

	template = 'contact.html'
	return render(request, template, context)
