from django.shortcuts import render, redirect
from . models import *
#from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def recipes(request):
    # Getting data from frontend to backend by "POST" method
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image') # 'name' in HTML template
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description') 

        print(recipe_name)
        print(recipe_description) 
        print(recipe_image)

        # SAVING IT INTO MODELS - 
        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
         )
        
        return redirect('/') #important url
    
    #Viewing data into template - 
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
         queryset = queryset.filter(recipe_name__icontains = request.GET.get('search')) # here "icontains" is a django keyword.

    context = {'recipes':queryset}

    return render(request, 'vegie/recipes.html', context)





# Deleting recipe - 
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/') #important url





# Updating recipe - 
def update_recipe(request, id):
     queryset = Recipe.objects.get(id=id)

     if request.method == 'POST':
            data = request.POST
            recipe_name = data.get('recipe_name')
            recipe_description = data.get('recipe_description')
            recipe_image = request.FILES.get('recipe_image')

            queryset.recipe_name = recipe_name
            queryset.recipe_description = recipe_description
        
            if recipe_image :
                 queryset.recipe_image = recipe_image
            queryset.save()
            return redirect('/')
     
     context = {'recipe':queryset}
     return render(request, 'vegie/update_recipes.html', context)





# Login page - 
def login_page(request):
     return render(request, "vegie/login.html")





# Register page - 
def register_page(request):
     if request.method =="POST":
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = User.objects.filter(username = username)
          if user.exists():
               messages.warning(request, "Username already taken")
               return redirect('/register/')
          
          user = User.objects.create(
               first_name = first_name,
               last_name = last_name,
               username = username,
          )

          # For encrypted password - 
          user.set_password(password)
          
          user.save()

          messages.success(request, "Account created successfully !")

          return redirect('/register/')
     
     return render(request, "vegie/register.html")
        

