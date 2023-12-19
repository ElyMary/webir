from django.shortcuts import render, redirect
from .models import Person
from .resources import PersonResource  # Updated import
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# # Create Employee

# def insert_gentax(request):
#     if request.method == "POST":
#         id = request.POST['id']
#         last_name = request.POST['last_name']
#         first_name = request.POST['first_name']
#         middle_name = request.POST['middle_name']
#         name_of_doctor = request.POST['name_of_doctor']
#         tin_no = request.POST['tin_no']
#         hospital_name = request.POST['hospital_name']
#         mobile_no = request.POST['mobile_no']
#         email_address = request.POST['email_address']
#         data = Person(id=id, last_name=last_name, first_name=first_name, middle_name=middle_name, name_of_doctor=name_of_doctor,
#         tin_no=tin_no, hospital_name=hospital_name, mobile_no=mobile_no, email_address=email_address)
#         data.save()
  
#         return redirect('show/')
#     else:
#         return render(request, 'insert.html')
    

# bulk upload
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()  # Updated to use PersonResource
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'Wrong Format')
            return render(request, 'upload.html')
        
        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            # Unpack values from the data list
            id, last_name, first_name, middle_name, name_of_doctor, tin_no, hospital_name, mobile_no, email_address = data

            # Create a Person object with the unpacked values
            person = Person(
                id=id,
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                name_of_doctor=name_of_doctor,
                tin_no=tin_no,
                hospital_name=hospital_name,
                mobile_no=mobile_no,
                email_address=email_address
            )

            # Save the Person object to the database
            person.save()

        return redirect('show/')
    else:
        return render(request, 'upload.html')
