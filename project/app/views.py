from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Item, User
from .models import Item, User, Image
from django.urls import reverse
from django import forms
import random
import string

# Generate random code
def generate_code():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(12))






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

# Function to sign up
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
	itemdb = Item.objects.filter(status=True)
	codes = []

	items = []
	for item in itemdb:
		if item.code not in items:
			items.append(item)
		else:
			pass

	db = []
	for item in itemdb:
		code = item.code
		img = Image.objects.filter(code=code).first()
		db.append([item, img])
	print(db)

	images = Image.objects.values("code").distinct()
	n = range(len(items))
	imgdb = Image.objects.all()
	print(imgdb)

	return render(request, "marketplace.HTML", {
		"items":items, "images":images, "n":n, "imgdb":imgdb, "db":db
		})


def item_code(request, code):
	code = code

	item = Item.objects.get(code=code)
	images = Image.objects.filter(code=code)

	return render(request, "item_code.HTML", {
		"item":item, "images":images
		})




# Add item webpage
def add_item(request):
	if "username" in request.session:
		return render(request, "add_item.HTML")
	else:
		return HttpResponseRedirect(reverse(index))

# Add item (to db) function
def add_item_submit(request):
	if request.method == "POST":
		data = request.POST
		code = generate_code()
		print("data:", data)
		print(code)

		poster = request.session["username"]
		title = request.POST["title"]
		condition = request.POST["title"]
		location = request.POST["location"]
		description = request.POST["description"]
		images = request.FILES.getlist("images")

		for image in images:
			print("image:", image)
			image = Image.objects.create(code=code, image=image)

		new_item = Item(poster=poster, code=code, title=title, condition=condition, location=location, description=description)
		new_item.save()

		return HttpResponseRedirect(reverse(marketplace), {
			"add_item": True
			})

	else:
		return HttpResponseRedirect(reverse(add_item))


# Logout function
def logout(request):
	request.session.flush()
	return HttpResponseRedirect(reverse(index))


######################### Testing stuff #########################

# Testing function
def test(request):
	return render(request, "test.HTML")

# add image testing function
def add_image(request):

	if request.method == "POST":
		data = request.POST
		images = request.FILES.getlist("images")
		code = generate_code()

		print("data:", data)
		print(code)

		for image in images:
			print("image:", image)
			image = Image.objects.create(code=code, image=image)

	return render(request, "index.HTML")