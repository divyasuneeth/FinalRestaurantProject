from flask import Flask
app= Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "This page will show all my restaurants!!"

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
