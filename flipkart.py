from flask import Flask, render_template, request, redirect, jsonify, url_for, make_response, abort, send_file
import pymongo
from flask_pymongo import PyMongo
from gridfs import GridFS
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
from bson.json_util import dumps
from gridfs.errors import NoFile
from flask import send_from_directory

app =Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/flipkart'

mongo = PyMongo(app)

@app.route('/')
def index():
	return render_template('flipkart.html')



@app.route('/file/<filename>')
def file(filename):
	return mongo.send_file(filename)


@app.route('/men_cloth')
def men_cloth():
	output=[]
	user=mongo.db.flipkart_data.find({'p_instalk' : 1})
	for q in user:
		output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
	return render_template('flipkart_view.html', output=output)
	

@app.route('/landline')
def landline():
	output=[]
	user=mongo.db.landline.find({'p_instalk' : 0, 'p_cod' : 1})
	for q in user:
		output.append({'id' : q['id'], 'p_id' : q['p_id'], 'p_category' : q['p_category'], 'p_title' : q['p_title'], 'p_img_small' : q['p_img_small'], 'p_img_medium' : q['p_img_medium'], 'p_img_large' : q['p_img_large'], 'p_retail_price' : q['p_retail_price'], 'retail_currency' : q['retail_currency'], 'p_productBrand' : q['p_productBrand'], 'p_product_url' : q['p_product_url'], 'p_instalk' : q['p_instalk'], 'p_cod' : q['p_cod']})
		
	return render_template('flipkart_view.html', output=output)


	"""for q in user:
		return f'''
			<h3>Product : { q['name'] }</h3>
			'''"""

if __name__ == "__main__":
	app.run()