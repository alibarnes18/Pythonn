from flask import Flask , request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.arg.get("q", "")

    if "'" in query or  "OR" in query.upper():
        return "MySql Error: You have an error in your Sql syntax", 500
    
    return f"Sonuçlar: {query}", 200  

@app.route("/comment")
def comment():
    yorum = request.args.get("yorum", "")
    # Savunmasız — input filtrelenmiyor
    return f"<html><body>{yorum}</body></html>", 200 

if __name__ == "__main__":
    app.run(port=5000)