from flask import Flask, make_response, request, render_template, redirect, url_for, flash, Response, send_file
import pymongo
import re
import requests
from flask_pymongo import PyMongo
from gridfs import GridFS
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
from bson.json_util import dumps
from gridfs.errors import NoFile
from flask import send_from_directory
from werkzeug.exceptions import HTTPException, NotFound
#...

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/flipkart'

mongo = PyMongo(app)


@app.route("/")
def hello():
    return render_template("indexsam.html")

@app.route("/office")
def office():
	output=[]
	user=mongo.db.productfeed_men.find({'p_instalk' : 1, 'p_cod' : 1}).limit(200).skip(130)
	for q in user:
		output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
	
	resp = make_response(render_template('flipkart_view.html', output=output))
	resp.set_cookie('comportement', 'Office')
	return resp 
	

@app.route("/travel")
def travel():
	output=[]
	user=mongo.db.flipkart_data.find({'p_instalk' : 1}).limit(5)
	for q in user:
		output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})

	resp = make_response(render_template('flipkart_view.html', output=output))
	resp.set_cookie('comportement', 'Travel')
	return resp

@app.route("/get")
def getcookie():
    comportement = request.cookies.get('comportement')
    return 'The preffered style is ' + comportement

@app.route("/del")
def delete_cookie():
    resp = make_response("Cookie Removed")
    resp.set_cookie('comportement', '')
    return resp

@app.route('/file/<filename>')
def file(filename):
	return mongo.send_file(filename)


"""*************************************travel functions************************************"""	

@app.route('/trousers_travel')
def trousers_travel():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'travel' ,'p_title' : { '$regex' : 'Trousers' }}).limit(50)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_travel.html', output=output)

@app.route('/tshirt_travel')
def tshirt_travel():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'travel', 'p_title' : { '$regex' : 'T-Shirt' }}).limit(50)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_travel.html', output=output)

@app.route('/shirt_travel')
def shirt_travel():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'travel' ,'$and' : [ {'p_title' : {'$not' : re.compile('T-Shirt')}}, {'p_title' : {'$not' : re.compile('T Shirt')}}, {'p_title' : {'$regex' : 'Shirt'}} ] }).skip(100).limit(50)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_travel.html', output=output)

@app.route('/jeans_travel')
def jeans_travel():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'travel' , '$and' : [ {'p_title' : {'$not' : re.compile('T-Shirt')}}, {'p_title' : {'$not' : re.compile('Shirt')}}, {'p_title' : {'$not' : re.compile('Jones')}}, {'p_title' : {'$not' : re.compile('Pepe')}}, {'p_title' : {'$regex' : 'Jeans'}} ] }).limit(200)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_travel.html', output=output)

"""*************************************Men travel functions************************************"""


"""*************************************Men office functions************************************"""

@app.route('/trousers_office')
def trousers_office():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'office' ,'p_title' : { '$regex' : 'Trousers' }}).limit(50)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_office.html', output=output)

@app.route('/tshirt_office')
def tshirt_office():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'office', 'p_title' : { '$regex' : 'T-Shirt' }}).limit(50)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_office.html', output=output)

@app.route('/shirt_office')
def shirt_office():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'office' ,'$and' : [ {'p_title' : {'$not' : re.compile('T-Shirt')}}, {'p_title' : {'$not' : re.compile('T Shirt')}}, {'p_title' : {'$regex' : 'Shirt'}} ] }).skip(100).limit(50)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_office.html', output=output)

@app.route('/jeans_office')
def jeans_office():
	output=[]
	user=mongo.db.men_final.find({'p_type' : 'office' , '$and' : [ {'p_title' : {'$not' : re.compile('T-Shirt')}}, {'p_title' : {'$not' : re.compile('Shirt')}}, {'p_title' : {'$not' : re.compile('Jones')}}, {'p_title' : {'$not' : re.compile('Pepe')}}, {'p_title' : {'$regex' : 'Jeans'}} ] }).limit(200)
	for q in user:
		output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
	return render_template('flipkart_view_men_office.html', output=output)


"""*************************************Men office functions************************************"""




"""-----------------------------------------deals-----------------------------------------------"""

@app.route('/deals')
def deals():
	output=[]
	user=mongo.db.top_deals.find()
	for q in user:
		output.append({'p_discount' : q['p_discount'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_product_url' : q['p_product_url']})
		
	return render_template('flipkart_deals_view.html', output=output)

"""----------------------------------------deals------------------------------------------------"""

@app.route("/aman", methods=['POST'])
def aman():
	name = request.form['name']
	r = requests.post('http://127.0.0.1:4000/api/message', json={"foo": name})
	return dumps(r)

@app.route('/category', methods=['POST'])
def category():
	if request.method == 'POST':
		sex = request.form['sex']
		cater = request.form['cater']
	
		"""-------------------------travel---------------------------"""

		if sex == 'm' and cater == 'travel':
			output=[]
			user=mongo.db.men_final.find({'p_type' : 'travel'}).limit(200)
			for q in user:
				output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
			resp = make_response(render_template('flipkart_view_men_travel.html', output=output))
			resp.set_cookie('comportement', 'Travel')
			return resp

		if sex == 'f' and cater == 'travel':
			output=[]
			user=mongo.db.productfeed_women.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view_men_travel.html', output=output))
			resp.set_cookie('comportement', 'Travel')
			return resp

		"""------------------------travel----------------------------"""

		"""--------------------------office-------------------------"""

		if sex == 'm' and cater == 'office':
			output=[]
			user=mongo.db.men_final.find({'p_type' : 'office'}).limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_productId' : q['p_productId'], 'p_title' : q['p_title'], 'p_description' : q['p_description'], 'p_img_large' : q['p_img_large'], 'p_mrp' : q['p_mrp'], 'p_price' : q['p_price'], 'p_productUrl' : q['p_productUrl'], 'p_categories' : q['p_categories'], 'p_productBrand' : q['p_productBrand'], 'p_deliveryTime' : q['p_deliveryTime'], 'p_in_stock' : q['p_in_stock'], 'p_codAvailable' : q['p_codAvailable'], 'p_emiAvailable' : q['p_emiAvailable'], 'p_offers' : q['p_offers'], 'p_discount' : q['p_discount'], 'p_cashBack' : q['p_cashBack'], 'p_size' : q['p_size'], 'p_color' : q['p_color'], 'p_sizeUnit' : q['p_sizeUnit'], 'p_sizeVariants' : q['p_sizeVariants'], 'p_colorVariants' : q['p_colorVariants'], 'p_styleCode' : q['p_styleCode'], 'p_type' : q['p_type']})
		
			resp = make_response(render_template('flipkart_view_men_office.html', output=output))
			resp.set_cookie('comportement', 'Office')
			return resp

		if sex == 'f' and cater == 'office':
			output=[]
			user=mongo.db.productfeed_women.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view_men_office.html', output=output))
			resp.set_cookie('comportement', 'Office')
			return resp

		"""-----------------------------office----------------------------"""

		"""---------------------------college-----------------------------"""

		if sex == 'm' and cater == 'college':
			output=[]
			user=mongo.db.productfeed_men.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view.html', output=output))
			resp.set_cookie('comportement', 'College')
			return resp

		if sex == 'f' and cater == 'college':
			output=[]
			user=mongo.db.productfeed_women.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view.html', output=output))
			resp.set_cookie('comportement', 'College')
			return resp

		"""---------------------------college--------------------------------"""

		"""-----------------------------party---------------------------------"""

		if sex == 'm' and cater == 'party':
			output=[]
			user=mongo.db.productfeed_men.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view.html', output=output))
			resp.set_cookie('comportement', 'Party')
			return resp

		if sex == 'f' and cater == 'party':
			output=[]
			user=mongo.db.productfeed_women.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view.html', output=output))
			resp.set_cookie('comportement', 'Party')
			return resp

		"""-------------------------------party---------------------------------"""

		"""--------------------------------sports-------------------------------"""

		if sex == 'm' and cater == 'sports':
			output=[]
			user=mongo.db.productfeed_men.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view.html', output=output))
			resp.set_cookie('comportement', 'Sports')
			return resp

		if sex == 'f' and cater == 'sports':
			output=[]
			user=mongo.db.productfeed_women.find().limit(50).skip(200)
			for q in user:
				output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
			resp = make_response(render_template('flipkart_view.html', output=output))
			resp.set_cookie('comportement', 'Sports')
			return resp

		"""--------------------------------college----------------------------------"""

if __name__ == '__main__':
 app.run(debug=True)