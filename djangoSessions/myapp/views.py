from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from myapp.forms import Details

# def visit_count(request):
#     page_count = int(request.COOKIES.get("page_count", 1))
#     page_count += 1
#     response = HttpResponse(f"Page visit count: {page_count}")
#     response.set_cookie("page_count", page_count)
#     return response

# def clear_count(request):
#     response = HttpResponse("Cookie cleared...")
#     response.delete_cookie("page_count")
#     return response

def email_login(request):
    if "email" in request.session:
        return redirect("profile")
    if request.method == "GET":
        form = Details()
    else:
        form = Details(request.POST)
        if form.is_valid():
            request.session["email"] = form.cleaned_data["email"]
            request.session['fullName'] = form.cleaned_data['fullName']
            request.session['gender'] = form.cleaned_data['gender']
            request.session['age'] = form.cleaned_data['age']
            return redirect("profile")
    return render(request, "myapp/login.html", {"form": form})

def profile(request):
    return render(request, "myapp/profile.html")

def logout(request):
    request.session.pop("email")
    request.session.pop("fullName")
    request.session.pop("gender")
    request.session.pop("age")
    return redirect("login")