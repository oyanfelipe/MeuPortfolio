from flask import Flask, render_template

app = Flask(__name__)


# route -> hashtagtreinamentos.com/...
# função _> o que você uer exibir naquela pagina
# template
@app.route('/homepage')
@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku
