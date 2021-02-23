from flask import Flask, request
from bson import json_util
from helpers.endpoints import *

app = Flask("ApiSiente")

@app.route("/")
def hola():
    return "¡¡Bien venido al registro de frases de personajes de la tele!!"

@app.route("/<typ>/new")
def new(typ):
    args = dict(request.args)
    id = insert(args,typ)
    return json_util.dumps({"_id":id})

@app.route("/<typ>")
def all(typ):
    return json_util.dumps(list_all(typ))

@app.route("/<typ>/details")
def details(typ):
    args = dict(request.args)
    return json_util.dumps(get(args,typ))

@app.route("/<typ>/delete")
def remove(typ):
    args = dict(request.args)
    return json_util.dumps(delete(args,typ))

@app.route("/<typ>/edit")
def edit(typ):
    args = dict(request.args)
    return json_util.dumps(update(args,typ))


app.run(debug=True)