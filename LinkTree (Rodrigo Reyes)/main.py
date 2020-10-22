from flask import Flask, render_template, request, url_for
from jinja2 import Template, FileSystemLoader, Environment
import yaml

file_loader = FileSystemLoader('templates')
enviroment = Environment(loader = file_loader)


app = Flask(__name__)

with open('CV.yaml') as f:
  yaml_file = yaml.load(f, Loader = yaml.FullLoader)

@app.route('/')
def Homepage():
    html_file = enviroment.get_template('Homepage.html')
    foto = url_for('static', filename=yaml_file['fotografia'])
    foo="bar"
    Links = yaml_file['Links']
    quien = yaml_file['informacion_pagina']['autor']
    return html_file.render(pic = foto,  Links=Links, cv = quien)

@app.route('/PaginaPrincipal')
def PaginaPrincipal():
  html_file = enviroment.get_template('Info.html')
  foto = url_for('static', filename=yaml_file['fotografia'])
  info = yaml_file['informacion_personal']
  quien = yaml_file['informacion_pagina']['autor']
  #infoNombre = yaml_file['informacion_personal']['nombre_completo']
  return html_file.render(pic = foto, info = info, cv = quien)

@app.route('/InfoPersonal')
def InfoPersonal():
  html_file = enviroment.get_template('InfoPersonal.html')
  infoNombre = yaml_file['informacion_personal']['nombre_completo']
  infoNancimiento = yaml_file['informacion_personal']['pais_de_nacimiento']
  idioma = yaml_file['informacion_personal']['idiomas']
  edad = yaml_file['informacion_personal']['edad']
  experiencia = yaml_file['informacion_personal']['experiencia']
  intereses = yaml_file['informacion_personal']['intereses']
  foto = url_for('static', filename=yaml_file['fotografia'])
  return html_file.render(name = infoNombre, place = infoNancimiento, language = idioma, age = edad, experiencia = experiencia, interest = intereses, pic = foto)

@app.route('/InfoLaboral')
def InfoLaboral():
  html_file = enviroment.get_template('InfoLaboral.html')
  experiencia = yaml_file['informacion_personal']['experiencia']
  Educacion = yaml_file['informacion_profesional']['educacion']
  tecnologias = yaml_file['informacion_profesional']['tecnologias']
  referencias = yaml_file['informacion_referencias']['referencias_laborales']
  referenciaP = yaml_file['informacion_referencias']['referencia_personal']
  foto = url_for('static', filename=yaml_file['fotografia'])
  return html_file.render(experiencia = experiencia, edu = Educacion, tech = tecnologias, Ref = referencias, RefP = referenciaP, pic = foto)

@app.route('/about')
def about():
  html_file = enviroment.get_template('about.html')
  acercademi= yaml_file['informacion_personal']['acerca_de_mi']
  AboutPic = url_for('static', filename=yaml_file['Picture'])
  return html_file.render(aboutMe = acercademi, About=AboutPic)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)