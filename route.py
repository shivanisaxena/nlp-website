from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def student():
	return render_template('index.html')
@app.route('/paper_search',methods=['POST','GET'])
def result():
	if 'search-text' in request.form:
		import pandas as pd
		data=pd.read_json('papers.json')
		data = [["A00-1001", "Title1"], ["A00-1021", "Title2"]]
		return render_template("paper_search.html",a1=data,v=request.form['search-text'])
	else:
		return render_template("paper_search.html",a1=[])
@app.route('/graph_demo',methods=['POST','GET'])
def data():
	dataa=request.args.get('data')
	return redirect('graph')
@app.route('/graph',methods = ['POST', 'GET'])
def graph():
	return render_template('sigma.js/examples/drag-nodes.html')

@app.route('/team',methods=['POST','GET'])
def team():
		return render_template("team.html")



if __name__ == '__main__':
   app.run(debug = True)
