from django.urls import path

from . import views

urlpatterns = [
    # Default page ==> localhost:8800/
    path("", views.index, name="index"),
    # Wikis page ==> localhost:8800/wiki/entery
    path("wiki/<str:title>", views.enter, name="enter"),
    # Search page ==> localhost:8800/search
    path("search/", views.search, name="search"),
    # save edit function
    path("save_edit/", views.saveedit, name="saveedit"),
    # Edit page ==> localhost:8800/edit
    path("edit/", views.edit, name="edit"),
    # New page page ==> localhost:8800/new
    path("new/", views.pagenew, name="pagenew"),
    # Random wiki page ==> localhost:8800/random
    path('random/', views.random_page, name="random"),

]
