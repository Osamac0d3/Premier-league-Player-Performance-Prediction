from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

df = pickle.load(open('player_data.pkl','rb'))

@app.route('/')
def home():

    teams = sorted(df['team'].unique())

    return render_template("index.html", teams=teams)


@app.route('/predict', methods=['POST'])
def predict():

    team = request.form['team']
    opponent = request.form['opponent']

    filtered = df[
        ((df['team'] == team) & (df['opponent_team'] == opponent)) |
        ((df['team'] == opponent) & (df['opponent_team'] == team))
    ]

    top_players = filtered.sort_values(
        by="predicted_rating",
        ascending=False
    ).head(30)

    return render_template(
        "result.html",
        players=top_players.to_dict(orient="records"),
        team=team,
        opponent=opponent
    )


if __name__ == "__main__":
    app.run(debug=True)