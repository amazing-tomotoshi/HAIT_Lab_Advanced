from django.urls import path
from . import views
from .views import selectfunc, loginfunc, student_home, society_home, company_home, SignUpView, detailfunc, goodfunc

app_name = 'app'

urlpatterns = [
    path('',selectfunc,name='select'),
    path('login/', loginfunc, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('student_create/', views.StudentCreate.as_view(), name='student_create'),
    path('company_create/', views.CompanyCreate.as_view(), name='company_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    
    path('student_home/',student_home,name='student_home'),
    path('society_home',society_home,name='society_home'),
    path('company_home',company_home,name='company_home'),

    # nagaya_develop_branchの変更箇所
    path('detail/', views.detailfunc, name='detailfun'), # views.pyのdetailfuncを参照
    path('detail/<int:post_id>', views.everypost, name='everypost'), # views.pyのeverypost関数を参照
    path('add/', views.add, name='add'), # 投稿フォーム用のpath(仮)設定
    path('edit/<int:post_id/', views.edit, name='edit'), # 編集機能の追加
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    path('good/<int:pk>', goodfunc, name='good'),
]