from flask import Flask, render_template,json

app=Flask(__name__) #this __ thing will allow cmd line server

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/test')
def test():
    some1={"title":"some title"} 
    return json.dumps(some1)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == "__main__":
    print("server running from python")
    app.run(debug=True)