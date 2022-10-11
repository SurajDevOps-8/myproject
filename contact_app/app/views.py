

# Create your views here.


############## added by me

# <h2>Contact List</h2>
# {% for contacts in contact %}
# <li>{{ contacts.full_name: contacts.phone_number }}</li>
# {% endfor %}

from django.shortcuts import render
from .models import Contact

def contact_list_view(request):   
    contact = Contact.objects.all()
    return render(request, "app/contact_list.html", {'contact':contact})


