from flask import Flask, render_template, redirect, abort, jsonify, url_for, send_from_directory
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
Bootstrap(app)

@app.route("/")
def accueil():
   return render_template("index.html")

@app.route("/index")
def index():
   return render_template("index.html")

# @app.route("/bootstrap")
# def bootstrap():
   # return render_template("bootstrap.html")

# @app.route("/salut/<nom>")
# def test_name(nom):
#    from datetime import datetime #from = importer une partie de la librairie uniquement
#    import calendar
#    joursSemaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
#    mtn = datetime.now()
#    # return f"Salut {nom} !"
#    jour_semaine = joursSemaine[mtn.weekday()] #renvoi chiffre jour de la semaine, puis tape dans tableau 
#    # jour_semaine = calendar.day_name[mtn.weekday()]
#    jour = mtn.day
#    mois = mtn.month
#    annee = mtn.year
#    return render_template("Testdesgars/salut.html",nom=nom, jour_semaine=jour_semaine, jour=jour, mois=mois, annee=annee)

# @app.route("/google")
# def google():
   # return redirect("https://google.com")

# @app.route("/test_index_template")
# def test_index_template():
   # return render_template("testdesgars/Test_Index_Template.html")

@app.route("/401")
def erreur_401():
   abort(401)

@app.errorhandler(404)
def error_404(error):
   # return redirect("/")
   return ("404"), 404


@app.route("/json")
def json():
   data = {"key": "value", "key2":"value2", "key3":"value3"}
   return jsonify(data)
   #utilité json = renvoyer valeur du back vers le front

@app.route("/setutilisateur/<nom>/<mdp>")
def utilisateur(nom, mdp):
   utilisateur = utilisateur(nom=nom, mdp=mdp)
   return utilisateur

@app.route("/addition/<v1>/<v2>")
def addition(v1, v2):
   result = int(v1) + int(v2)
   return str(result)

@app.route("/testolivia")
def olivia():
   return render_template("testdesgars/TestOlivia.html")

@app.route("/services")
def services():
   return render_template("services.html")

@app.route("/apropos")
def apropos():
   return render_template("apropos.html")

@app.route("/reservation")
def reservation():
   return render_template("reservation.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route("/connexion")
def connexion():
   return render_template("connexion.html")

# @app.route("/css/<path:path>")
# def send_css(path):
#    return send_from_directory("static/css", path)

# @app.route("/img/<path:path>")
# def send_img(path):
#    return send_from_directory("static/img", path)

@app.route("/formulaire_chien")
def formulaire_chien():
   return render_template("Testdesgars/formulaire_chien.html")

# @app.route("/calendrier")
# def calendrier():
   # return render_template("Testdesgars/calendrier.html")

app.run()



