from django.shortcuts import render

from .forms import ContactForm

def contact(request):

	form = ContactForm(request.POST or None)

	if form.is_valid():
		print form.cleaned_data['email']

	context = locals()
	template = 'contact.html'
	return render(request, template, context)
