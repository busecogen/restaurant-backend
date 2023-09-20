from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FoodView(APIView):
    permission_classes = (IsAuthenticated,)
    food_name = ""
    explanation = ""

    def get(self, request):
        data = {
            'food_name': self.food_name,
            'explanation': self.explanation,
        }
        return Response(data, status=status.HTTP_200_OK)


class EntreeView(FoodView):
    food_name = 'Entree'
    explanation = 'A category of main courses in a meal.'


class BeefView(FoodView):
    food_name = 'Beef'
    explanation = 'A type of meat that comes from cattle.'


class SteakView(FoodView):
    food_name = 'Steak'
    explanation = 'A high-quality cut of beef that is usually cooked by grilling or pan-searing.'


class RoastBeefView(FoodView):
    food_name = 'Roast Beef'
    explanation = 'A large piece of beef that is cooked by roasting in an oven.'


class TBoneView(FoodView):
    food_name = 'T-Bone'
    explanation = 'A steak that includes a T-shaped bone with meat on both sides, typically from a steer.'


class ChickenView(FoodView):
    food_name = 'Chicken'
    explanation = 'Poultry meat that is commonly consumed and can be prepared in various ways.'


class WingsView(FoodView):
    food_name = 'Wings'
    explanation = 'Chicken wings, often seasoned and fried, served as a popular appetizer.'


class TendersView(FoodView):
    food_name = 'Tenders'
    explanation = 'Chicken tenders, also known as chicken strips, are boneless cuts of chicken meat.'


class GrilledView(FoodView):
    food_name = 'Grilled'
    explanation = 'Refers to food items that are cooked by grilling on an open flame or hot surface.'


class BurgerView(FoodView):
    food_name = 'Burger'
    explanation = 'A sandwich typically consisting of a patty, vegetables, and condiments.'


class CheeseBurgerView(FoodView):
    food_name = 'Cheese Burger'
    explanation = 'A burger topped with cheese, often melted over the patty.'


class BBQBurgerView(FoodView):
    food_name = 'BBQ Burger'
    explanation = 'A burger with a barbecue-flavored patty or sauce.'


class ChickenBurgerView(FoodView):
    food_name = 'Chicken Burger'
    explanation = 'A burger made with a chicken patty instead of beef.'


class PastaView(FoodView):
    food_name = 'Pasta'
    explanation = 'A type of Italian dish made from dough and usually served with sauce.'


class FettuccineView(FoodView):
    food_name = 'Fettuccine'
    explanation = 'A type of pasta that is popularly served with creamy sauces.'


class RavioliView(FoodView):
    food_name = 'Ravioli'
    explanation = 'A type of pasta that contains filling and is typically served with sauce.'


class PenneView(FoodView):
    food_name = 'Penne'
    explanation = 'A type of pasta with cylindrical shape and diagonally cut ends.'


class DessertView(FoodView):
    food_name = 'Dessert'
    explanation = 'A sweet dish typically served after the main course.'


class ApplePieView(FoodView):
    food_name = 'Apple Pie'
    explanation = 'A dessert made with a flaky pastry crust and apple filling.'


class CheeseCakeView(FoodView):
    food_name = 'Cheese Cake'
    explanation = 'A sweet dessert with a creamy cheese-based filling, often with a crust.'


class DonutView(FoodView):
    food_name = 'Donut'
    explanation = 'A fried or baked dough confection typically ring-shaped and sweet.'


class BeverageView(FoodView):
    food_name = 'Beverage'
    explanation = 'A drink, typically non-alcoholic, served with meals.'


class WaterView(FoodView):
    food_name = 'Water'
    explanation = 'A clear, odorless, and tasteless liquid essential for hydration.'


class CokeView(FoodView):
    food_name = 'Coke'
    explanation = 'A popular carbonated soft drink with a distinct flavor.'


class LemonadeView(FoodView):
    food_name = 'Lemonade'
    explanation = 'A sweet and tart beverage made from lemon juice, water, and sugar.'


class ClassicLemonadeView(FoodView):
    food_name = 'Classic Lemonade'
    explanation = 'The timeless version of lemonade, a refreshing and tangy drink.'


class MintLemonadeView(FoodView):
    food_name = 'Mint Lemonade'
    explanation = 'Lemonade infused with mint leaves for an extra burst of flavor.'


class StrawberryLemonadeView(FoodView):
    food_name = 'Strawberry Lemonade'
    explanation = 'Lemonade with added strawberry flavor, offering a fruity twist.'


class BeerView(FoodView):
    food_name = 'Beer'
    explanation = 'An alcoholic beverage made from fermented grains,'
