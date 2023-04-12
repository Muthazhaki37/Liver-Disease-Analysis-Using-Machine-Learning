import Flask import Flask, render_templete, request
import pickle
app=Flash(_name_)
@app.route('/')
def home():
    return render_template('home,html')
@app.route('/predict')
def index():
    return render_template("index.html")
@app.route('/data_predict', methods=['POST'])
def predict():
    age = request.form['age']
    gender = request.form['gender']
    tb = request.form['tb']
    db = request.form['db']
    ap = request.form['ap']
    aa1 = request.form['aa1']
    aa2 = request.form['aa2']
    tp = request.form['tp']
    a = request.form['a']
    agr = request.form['agr']
    data = [[float(age), float(gender), float(tb), float(tb), float(ap), float(aa1), float(aa2), float(tp)]]
    model = pickel.load(open('liver_analysis.pk1', 'rb'))
    prediction= model.predict(data)[0]
    if (prediction == 1):
        return render_template('noChance.html', prediction='You have a liver disease problem, You must and')
    else
        return render_template('chance.html', prediction='You dont have a liver disease problem')
    if__name__ == '__main__';
    app.run()
