from flask import Flask,render_template,request,redirect,url_for,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app= Flask(__name__)

#ADD JSON API
@app.route('/restaurants/JSON')
def restaurantJSON():
	restaurant = session.query(Restaurant).all()
	return jsonify(Restaurant=[i.serialize for i in restaurant])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
	return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants= session.query(Restaurant).all()
    return render_template('restaurants.html',restaurants=restaurants) #"This page will show all my restaurants!!"

@app.route('/restaurants/new',methods=['GET','POST'])
def newRestaurant():
    if request.method=='POST':
        newRestaurant=Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newrestaurant.html')#"This page will let you create a new restaurant"

@app.route('/restaurants/<int:restaurant_id>/edit',methods=['GET','POST'])
def editRestaurant(restaurant_id):
    getRestaurant=session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method=='POST':
        if request.form['name']:
            getRestaurant.name=request.form['name']
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editrestaurant.html',item=getRestaurant)#"This page will let you Edit a restaurant"

@app.route('/restaurants/<int:restaurant_id>/delete',methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    getRestaurant=session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method=='POST':
        session.delete(getRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleterestaurant.html',item=getRestaurant)#"This page will let you delete a restaurant"

@app.route('/restaurants/<int:restaurant_id>/menu')
def showRestaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id= restaurant_id).one()
    items= session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html',restaurant_id=restaurant_id, items=items) #"This page will show the restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/new',methods=['GET','POST'])
def newRestaurantMenu(restaurant_id):
    if request.method == 'POST':
        newItem= MenuItem(name=request.form['name'],
        description=request.form['description'],course=request.form['course'],
        price=request.form['price'],restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showRestaurantMenu',restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html',restaurant_id=restaurant_id) #"This page will let you create a new restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
			editedItem.name = request.form['name']
        if request.form['description']:
			editedItem.description = request.form['description']
        if request.form['price']:
			editedItem.price = request.form['price']
        if request.form['course']:
			editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()

        return redirect(url_for('showRestaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = editedItem)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete',methods=['GET','POST'])
def deleteMenuItem(restaurant_id,menu_id):
    deleteitem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method=='POST':
        session.delete(deleteitem)
        session.commit()
        return redirect(url_for('showRestaurantMenu',restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html',restaurant_id=restaurant_id,
        menu_id=menu_id, item=deleteitem)#"This page will let you delete the restaurant menu"




if __name__ =='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000, threaded = False)
