from django.conf.urls import url
from first_app import views

app_name = "first_app"

urlpatterns = [
url(r'^users/$',views.users,name = "users"),
url(r'^forms/$',views.FormPage,name = "forms"),
url(r'^user_names/$',views.userNames,name = "usernames"),
url(r'^register/$',views.register,name = "register"),
url(r'^user_login/$',views.user_login,name = "user_login"),
url(r'^special/$',views.special,name = "special")
]
