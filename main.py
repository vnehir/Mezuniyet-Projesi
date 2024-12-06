from flask import Flask, render_template,redirect

app = Flask(__name__)

@app.route("/")
def Başlık():
    return render_template('index.html')
'<h1>İKLİM DEĞİŞİKLİĞİ VE ETKİLEYEN FAKTÖRLER</h1>' 

if __name__ == "__main__":
    app.run(debug=True)