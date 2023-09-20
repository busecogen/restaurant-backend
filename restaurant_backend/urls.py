"""
URL configuration for restaurant_backend project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ranger.urls')),
    path('entree/', EntreeView.as_view(), name='entree'),
    path('entree/beef/', BeefView.as_view(), name='beef'),
    path('entree/beef/steak/', SteakView.as_view(), name='steak'),
    path('entree/beef/roastbeef/', RoastBeefView.as_view(), name='roastbeef'),
    path('entree/beef/tbone/', TBoneView.as_view(), name='tbone'),
    path('entree/chicken/', ChickenView.as_view(), name='chicken'),
    path('entree/chicken/wings/', WingsView.as_view(), name='wings'),
    path('entree/chicken/tenders/', TendersView.as_view(), name='tenders'),
    path('entree/chicken/grilled/', GrilledView.as_view(), name='grilled'),
    path('entree/pasta/', PastaView.as_view(), name='pasta'),
    path('entree/pasta/fettuccine/', FettuccineView.as_view(), name='fettuccine'),
    path('entree/pasta/ravioli/', RavioliView.as_view(), name='ravioli'),
    path('entree/pasta/penne/', PenneView.as_view(), name='penne'),

    path('burger/', BurgerView.as_view(), name='burger'),
    path('burger/cheese/', CheeseBurgerView.as_view(), name='cheese'),
    path('burger/bbq/', BBQBurgerView.as_view(), name='bbq'),
    path('burger/chicken/', ChickenBurgerView.as_view(), name='chicken'),

    path('dessert/', DessertView.as_view(), name='dessert'),
    path('dessert/applepie/', ApplePieView.as_view(), name='applepie'),
    path('dessert/cheesecake/', CheeseCakeView.as_view(), name='cheesecake'),
    path('dessert/donut/', DonutView.as_view(), name='donut'),

    path('beverage/', BeverageView.as_view(), name='beverage'),
    path('beverage/water/', WaterView.as_view(), name='water'),
    path('beverage/coke/', CokeView.as_view(), name='coke'),
    path('beverage/lemonade/', LemonadeView.as_view(), name='lemonade'),
    path('beverage/lemonade/classic/', ClassicLemonadeView.as_view(), name='classic'),
    path('beverage/lemonade/mint/', MintLemonadeView.as_view(), name='mint'),
    path('beverage/lemonade/strawberry/', StrawberryLemonadeView.as_view(), name='strawberry'),
    path('beverage/beer/', BeerView.as_view(), name='beer'),

]
