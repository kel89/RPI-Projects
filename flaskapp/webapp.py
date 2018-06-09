from flask import Flask, render_template, flash, request, sessions, abort

app = Flask(__name__)

# root route
@app.route("/", methods=["GET"])
def index():
	# Now we pull the command
	command = request.args['command']
	print("Command is:", command)
	
	return render_template("index.html") # automatically looks in Templates
	
# Test JQuery
@app.route("/command")
def btn():
	s = request.headers.get("command")
	print("Got", s)
	d = request.args
	for k in d.keys():
		print("\t", k)
	return render_template("index.html") 

	
	
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
