# from crypt import methods
from operator import mod
from flask import Flask, request
from flask import Flask, render_template, redirect
import joblib
# import sklearn
# from sklearn.neighbors import KNeighborsClassifier
import numpy as np
app = Flask(__name__)

@app.route("/" , methods=['POST','get'])
def index():
    if request.method == 'POST':
        model = joblib.load('mlp_model.joblib')
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        d = float(request.form['d'])
        e = float(request.form['e'])
        f = float(request.form['f'])
        g = float(request.form['g'])
        h = float(request.form['h'])
        i = float(request.form['i'])
        j = float(request.form['j'])
        k = float(request.form['k'])
        l = float(request.form['l'])
        m = float(request.form['m'])
        n = float(request.form['n'])
        
        datas = np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n]]) 
        
        isKecemasan = model.predict(datas)
        (datas)
        return render_template ('hasil.html', finalData = isKecemasan)
    else:
        return render_template ('index.html')

if __name__ == "__main__":
    app.run(debug=False, host = '0.0.0.0')
