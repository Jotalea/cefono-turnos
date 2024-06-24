from flask import Flask

def start():
  app = Flask(__name__)

	@app.route("/", methods=["GET"])
  def index():
    return "Hola, funciona"

if __name__ == __main__:
	start()
