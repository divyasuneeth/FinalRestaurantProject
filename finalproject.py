from flask import Flask,render_template,request,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app= Flask(__name__)



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
    items= session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html',items=items) #"This page will show the restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newRestaurantMenu(restaurant_id):
    return render_template('newmenuitem.html',restaurants=restaurants) #"This page will let you create a new restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/edit')
def editRestaurantMenu(restaurant_id,item_id):
    return render_template('editmenuitem.html',restaurant_id=restaurant_id,item_id=item_id)#"This page will let you edit the restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/delete')
def deleteRestaurantMenu(restaurant_id,item_id):
    return render_template('deletemenuitem.html',restaurant_id=restaurant_id,item_id=item_id)#"This page will let you delete the restaurant menu"




if __name__ =='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000, threaded = False)
