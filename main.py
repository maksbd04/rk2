from flask import Flask, request, jsonify, render_template
import json
app = Flask(__name__)

my_api = [{
    "game":"GTA6",
    "url":"/game/GTA6"
},{
    "game":"Terraria",
    "url":"/game/terraria"
},{
    "game":"Minecraft",
    "url":"/game/minecraft"
},
]

@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html")



@app.route('/game/<gamename>',methods=['GET'])
def game(gamename):
    if gamename.lower() == "gta6":
        return render_template("GTA6.html")
    elif gamename.lower() == "terraria":
        return render_template("terraria.html")
    elif gamename.lower() == "minecraft":
        return render_template("minecraft.html")
    else:
        return render_template("error.html")


@app.route('/about',methods=['GET'])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)