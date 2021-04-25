from django.utils.deprecation import MiddlewareMixin    
from django.shortcuts import render, redirect
from django.urls import reverse


class AuthRequiredMiddleware(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if  user.is_superuser ==True:
                if  modulename == "authentication.views" or modulename == "dashboard.views":
                    pass
                else:
                    return redirect("home")  
            else:
                return redirect("/")

        else:
            if request.path == reverse("/") or request.path == reverse("/"):
                pass
            else:
                return redirect("/")
