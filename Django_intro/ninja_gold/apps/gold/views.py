from django.shortcuts import render, redirect
import random,datetime

# Create your views here.
def index(request):

    if "my_gold" not in request.session:
        request.session["my_gold"] = 0
        request.session["activities"] = []

    return render(request, ('gold/index.html'))

def money(request):

    date = datetime.datetime.now().strftime("%Y/%m/%d %X %p")
    print date # make sure date is correct, full year/mon/day, local time, am/pm

    if request.POST["building"] == "Farm":
        gold = random.randint(10,20)
        request.session["my_gold"] += gold
        request.session["activities"].append("You earned " + str(gold) + " golds from the farm! (" + date + ")")

    elif request.POST["building"] == "Cave":
        gold = random.randint(5,10)
        request.session["my_gold"] += gold
        request.session["activities"].append("You earned " + str(gold) + " golds from the cave! (" + date + ")")

    elif request.POST["building"] == "House":
        gold = random.randint(2,5)
        request.session["my_gold"] += gold
        request.session["activities"].append("You earned " + str(gold) + " golds from the house! (" + date + ")")

    elif request.POST["building"] == "Casino":
        gold = random.randint(-50,50)
        request.session["my_gold"] += gold
        if gold > 0:
            request.session["activities"].append("You earned " + str(gold) + " golds from the casino! (" + date + ")")
        else:
            request.session["activities"].append("You lost " + str(gold) + " golds from the casino! (" + date + ")")

    return redirect("/")

def you_won(request):

    request.session["my_gold"] = 0
    request.session["activities"] = []
    return redirect("/")
