from django.contrib import messages
from django.shortcuts import render
from .forms import UserImageForm


# Create your views here.


# def user_image(request):
#     image_form = UserImageForm()
    
#     if request.method == "POST":
#         image_form = UserImageForm(request.POST, request.FILES)
#         if image_form.is_valid():
#             obj = image_form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # messages.success(request, "User image saved!")
            
#     context = {
# 		'image_form': image_form,
# 	}
    
#     return render(request, 'partials/image.html', context)