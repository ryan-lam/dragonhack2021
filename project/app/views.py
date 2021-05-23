from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import session
import random

def generate_code():
	''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(12))


# Create your views here.

def index(request):
	return render(request, "index.HTML")

def marketplace(request):
	items = Item.objects.all.filter(status=True)
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

