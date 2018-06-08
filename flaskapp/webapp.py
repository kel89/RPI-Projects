from flask import Flask, render_template, flash, request, sessions, abort

app = Flask(__name__)

# root route
@app.route("/")
def index():
	return render_template("index.html") # automatically looks in Templates
	
	
# Test link
@app.route("/test")
def test_link():
	print("Button test passed")
	return render_template("index.html")
	
# Change value for test slider
@app.route("/slider/<val>")
def slider_update(val):
	print("Slider value is", val)
	return render_template("index.html")




if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
	
	print("\n\n")
	print(80*"-")
	print("Quitting") # here is where you can put cleanup
