from flask import Flask,render_template
app= Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'},
{'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},
{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},
{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]

item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return render_template('restaurants.html',restaurants=restaurants) #"This page will show all my restaurants!!"

@app.route('/restaurants/new')
def newRestaurant():
    return "This page will let you create a new restaurant"

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This page will let you Edit a restaurant"

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This page will let you delete a restaurant"

@app.route('/restaurants/<int:restaurant_id>/menu')
def showRestaurantMenu(restaurant_id):
    return "This page will show the restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newRestaurantMenu(restaurant_id):
    return "This page will let you create a new restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editRestaurantMenu(restaurant_id,menu_id):
    return "This page will let you edit the restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteRestaurantMenu(restaurant_id,menu_id):
    return "This page will let you delete the restaurant menu"




if __name__ =='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000, threaded = False)
