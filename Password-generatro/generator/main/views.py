from django.shortcuts import render
import random
import string
from .models import PasswordConfiguration

# Create your views here.

def generate_password(request):
    if request.method == 'POST':
        # Get data from the form
        length = int(request.POST.get('length', 8))
        include_uppercase = request.POST.get('uppercase') == 'on'
        include_lowercase = request.POST.get('lowercase') == 'on'
        include_numbers = request.POST.get('numbers') == 'on'
        include_special = request.POST.get('special') == 'on'

        # Generate password
        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_numbers:
            characters += string.digits
        if include_special:
            characters += '!@#$%^&*()'

        if not characters:
            generated_password = "Please select at least one character type."
        else:
            generated_password = ''.join(random.choice(characters) for _ in range(length))

        return render(request, 'index.html', {'password': generated_password})

    return render(request, 'index.html')