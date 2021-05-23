from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Item, User
from .models import Item, User, Image
from django.urls import reverse
import random
import string

def generate_code():
	''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(12))


# Create your views here.
# Index page
def index(request):
	return render(request, "index.HTML")

# Function to sign in
def signin(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		if User.objects.filter(username=username, password=password).exists():
			user = User.objects.get(username=username, password=password)
			request.session["username"] = user.username
			request.session["name"] = user.name
			# return HttpResponseRedirect(reverse(test))
			return HttpResponseRedirect(reverse(marketplace))
		else:
			return render(request, "index.HTML")

	else:
		return render(request, "index.HTML")

def signup(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		name = request.POST["name"]
		email = request.POST["email"]

		if not User.objects.filter(username=username).exists():
			new_user = User(username=username, password=password, name=name, email=email)
			new_user.save()
			request.session["username"] = username
			request.session["name"] = name
			# return HttpResponseRedirect(reverse(test))
			return HttpResponseRedirect(reverse(marketplace))
		else:
			return render(request, "index.HTML")

	else:
		return render(request, "index.HTML")




def marketplace(request):
	items = Item.objects.all().filter(status=True)
	return render(request, "marketplace.HTML", {
		"items":items
		})




# Done
def add_item(request):
	if "username" in request.session:
		return render(request, "add_item.HTML")
	else:
		return HttpResponseRedirect(reverse(index))


# Done
def add_item_submit(request):
	if request.method == "POST":
		poster = request.session["username"]
		title = request.POST["title"]
		condition = request.POST["title"]
		location = request.POST["location"]
		description = request.POST["description"]

		new_item = Item(poster=poster, title=title, condition=condition, location=location, description=description)
		new_item.save()

		return HttpResponseRedirect(reverse(marketplace), {
			"add_item": True
			})

	else:
		return HttpResponseRedirect(reverse(add_item))



def logout(request):
	request.session.flush()
	return HttpResponseRedirect(reverse(index))

def test(request):
	return render(request, "test.HTML")