from flask import Flask , request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.arg.get("q", "")

    if "'" in query or  "OR" in query.upper():
        return "MySql Error: You have an error in your Sql syntax", 500
    
    return f"Sonuçlar: {query}", 200   

if __name__ == "__main__":
    app.run(port=5000)