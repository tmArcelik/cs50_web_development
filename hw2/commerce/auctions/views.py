from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, timedelta
from .models import User, Auction
from django.db.models import Max, F, Count
from django.contrib.auth.decorators import login_required

def index(request):
    now = datetime.now()
    return render(request, "auctions/index.html", {
                "listings": Auction.objects.filter(endTime__gt = now).annotate(price=Max('bids__price'))
            })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def createListing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        category = request.POST["category"]
        imageUrl = request.POST["imageUrl"]
        openingBid = float(request.POST["openingBid"]) * 100
        
        # TODO do some cheking

        try:
            newAuction = Auction(title=title, description=description, imagePath=imageUrl, category=category, openingPrice= openingBid, creator= request.user)
            newAuction.startTime = datetime.now()
            newAuction.endTime = newAuction.startTime + timedelta(weeks=1)
            newAuction.save()
        except IntegrityError:
            return render(request, "auctions/index.html", {
                "message": "Some Error Happened"
            })
        return HttpResponseRedirect(reverse("index"))


        

    else:
        return render(request, "auctions/createListing.html", {
                "message": "No message"
            })

def listing(request, auctionId):
    
    auction = Auction.objects.filter(pk = auctionId).annotate(price=Max('bids__price')).first()

    if auction == None:
        return HttpResponseNotFound()
    else:
        return render(request, "auctions/listing.html", {
                "auction": auction
            })