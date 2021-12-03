from flask import Flask, render_template, url_for, request
import pickle

app = Flask(__name__)


# load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # take value from form
        value = []
        deliver_check = int(request.form['deliver_check'])
        value.append(deliver_check)
        basket_icon_click = int(request.form['basket_icon_click'])
        value.append(basket_icon_click)
        saw_checkout = int(request.form['saw_checkout'])
        value.append(saw_checkout)
        basket_add_list = int(request.form['basket_add_list'])
        value.append(basket_add_list)
        basket_add_detail = int(request.form['basket_add_detail'])
        value.append(basket_add_detail)
        list_size_dropdown = int(request.form['list_size_dropdown'])
        value.append(list_size_dropdown)
        closed_minibasket_click = int(request.form['closed_minibasket_click'])
        value.append(closed_minibasket_click)

        # Predict
        pred = model.predict([value])[0]
        print("pred: ", pred)
        result = "Predict: Order" if pred == 1 else "Predict: Not order"

        return render_template('index.html', result=result)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
