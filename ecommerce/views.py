from django.shortcuts import render,redirect
from .forms import ContactForm
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    context = {
        'title':''
    }
    return render (request, 'index.html', context)

def about(request):
    context = {
        "title":"About Page",
        "content":" Welcome to the about page."
    }
    return render (request, 'about.html', context)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

# def contact(request):
#     contact_form=ContactForm(request.POST or None)
#     context = {
#         'title':'Contact',
#         'content':'welcome',
#         'form':contact_form
#     }
#     if contact_form.is_valid():
#         print(contact_form.cleaned_data)
#     # if request.method =='POST':
#     #     print(request.POST)
#     return render (request, 'contact/view.html', context)


