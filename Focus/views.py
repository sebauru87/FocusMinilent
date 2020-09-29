from django.http import request
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Emails

import csv
from .myemail import send_email


def index(request):
    return render(request, 'focus/index.html')

def contact(request):
    return render(request, 'focus/contact.html')

def lab(request):
    return render(request, 'focus/lab.html')

def lentescontacto(request):
    return render(request, 'focus/lentescontacto.html')

def write_data_to_csv(data):
    with open('./database.csv', newline='', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
        send_email(name, email, subject, message)


# @app.route('/submit_form', methods=['POST', 'GET'])
def submit_form(request):
    if request.method == 'POST':
        try:
            # data = request.form.to_dict()
            data = request.POST
            write_data_to_csv(data)
            message = 'Muchas gracias por escribirnos. Estaremos respondiendo tu mensaje lo mas rapido posible.'
            return render(request, 'focus/thankyou.html', {'message': message})
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again.'

def submit_newsletter(request):
    if request.method == 'POST':
        try:
            data = request.POST
            user_email = Emails(email=data['email'])
            user_email.save()
            message = 'Muchas gracias por suscribirte a nuestro Newsletter.'
            return render(request, 'focus/thankyou.html', {'message': message})
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again.'