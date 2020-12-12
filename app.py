from flask import Flask, render_template
from controllers.nurses_controller import nurses_blueprint
from controllers.pokemons_controller import pokemon_blueprint

app = Flask(__name__)

app.register_blueprint(nurses_blueprint)
app.register_blueprint(pokemon_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)