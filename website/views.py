from django.shortcuts import render
from django.views import View
from website import models
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
class Landing(View):
    def get(self, request):

        return render(request, 'website/index.html',
			{'request': request,})

    def post(self, request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        business_name = request.POST.get('business_name', '')
        size = request.POST.get('size', '')
        service = request.POST.get('service', '')
        message = request.POST.get('message', '')
        print(name, email, business_name)

        form = models.Business(name=name,
            email=email, company=business_name, size=size, service=service, message=message)
        form.save()
        '''
        html = 'Dear Braintree,<br><br>Please see the following contact form submission:<br>Name: {}<br>Email: {}<br>Company: {}<br>Size: {}<br>Service: {} <br>Message: {}<br><br>Regards,<br>The Verde Team'.format(name, 
            email, business_name, size, service, message)

        send_mail('[Website] Request Callback Form Submission - {}'.format(name), '', 'noreply@verde.work', 
            ['dimitrik@braintree.co.za',], fail_silently=False, html_message=html)
        '''

        return JsonResponse({'name':name})

class Error(View):
    def get(self, request):
        return render(request, 'website/error.html',
            {'request': request, })