from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Mipaginaweb.html')
def mipaginaweb():
    return render_template('Mipaginaweb.html')

@app.route('/Git.html')
def git():
    return render_template('Git.html')

@app.route('/VR.html')
def vr():
    return render_template('VR.html')

@app.route('/escaneo3d.html')
def escaneo3d():
    return render_template('escaneo3d.html')

@app.route('/Investigacion.html')
def Investigacion():
    return render_template('Investigacion.html')

@app.route('/Juegos.html')
def Juegos():
    return render_template('Juegos.html')

@app.route('/Presentacion.html')
def Presentacion():
    return render_template('Presentacion.html')

if __name__ == '__main__':
    app.run(debug=True)
