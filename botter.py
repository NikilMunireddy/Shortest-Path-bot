from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import json
import requests
import time
import os

app=Flask(__name__)

@app.route('/')
@cross_origin()
def root():
    return render_template('r.html')

@app.route('/home',methods=['POST','GET'])
@cross_origin()
def home():
    A=(18,36)
    S=(0,0)
    B=(36,30)
    src=request.form['src']
    dest=request.form['dest']
    path=request.form['path']
    if src=='s':
        xi,yi=S
    if src=='a':
        xi,yi=A
    if src=='b':
        xi,yi=B
    if dest=='a':
        xn,yn=A
    if dest=='b':
        xn,yn=B
    x1,y1,x2,y2=xi,yi,xn,yn
    fileobj=open('path.txt','w')
    fileobj.write(path)
    fileobj.close()
    try:
        os.remove('d.txt')
    except:
        pass
    ob=open('d.txt','w')
    string=str(x1)+','+str(y1)+','+str(xn)+','+str(yn)
    ob.write(string)
    ob.close()
    fileobj=open('f.txt','r')
    a=[]
    for line in fileobj:
        a.append(line)
    data={'d1':a[0]}
    return 'ok'
    #data={ "path":string }
    

@app.route('/home/plot', methods=['GET','POST'])
@cross_origin()
def plotter():
    fileobj=open('f.txt','r')
    a=[]
    for line in fileobj:
        a.append(line)
    data={'d1':a[0]}
    return jsonify(data)

app.run(port=5017,debug=True)