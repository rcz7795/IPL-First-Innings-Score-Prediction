from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin

import IPLScorePredictor as tm

app = Flask(__name__)

@app.route('/get_team1_names', methods=['GET'])
def get_team1_names():
    response = jsonify({
        'team1': tm.get_team_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_team2_names', methods=['GET'])
def get_team2_names():
    response = jsonify({
        'team2': tm.get_team_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_venue_names', methods=['GET'])
def get_venue_names():
    response = jsonify({
        'venue': tm.get_venue_values()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_overs_names', methods=['GET'])
def get_overs_names():
    response = jsonify({
        'overs': tm.get_over_values()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_wickets_names', methods=['GET'])
def get_wickets_names():
    response = jsonify({
        'wickets': tm.get_wickets_values()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
#@cross_origin()
def predict():
    if request.method == "POST":
        team1 = request.form.get('team1')
        team2 = request.form.get('team2')
        venue = request.form.get('venue')
        over = int(request.form.get('overs'))
        wickets = int(request.form.get('wickets'))
        score = int(request.form['score'])
        runs_in_last4 = int(request.form['runs_last4'])
        wickets_in_last4 = int(request.form['wickets_last4'])

        prediction = abs(int(tm.predict_cricket_price(team1, team2, venue, over, wickets, score, runs_in_last4, wickets_in_last4)))

        return render_template('result.html', lower_limit= prediction - 10, upper_limit= prediction + 5)

    return render_template("home.html")


if __name__ == "__main__":
    tm.load_saved_attributes()
    app.run(debug = True)