from flask import Flask, request, jsonify, render_template
from hadoop import *
import main


app = Flask(__name__)

@app.route('/menu', methods=["GET"])
def index():
    # all the available services
    data = main.index()

    if request.method == "GET":
        return jsonify(data)
    else:
        return data




@app.route('/tech', methods=["POST"])
def Services():
    if request.method == "POST":
        tech = request.args.post['tech'] #  selected Technology
        service_no = request.args.post['service'] # particular Service, acts similar to press 1,2 ...
        service_no = int(service_no)
        ip_add = request.args.post['ip'] # ip of the system
        user = request.args.post['user'] #remote user
        passw = request.args.post['pass'] # remote user password or file 
        remote = request.args.post['remote'] #boolean value
        user_data = {"user": user, "passw": passw, "ip":ip_add, "remote": remote}
        try:
            # dict key is equal to function name
            output_data = eval(tech+f"(service = {service_no}, data = {data})") #executing the function
            return jsonify(output_data)
        except:
            output_data = {"Status": "Failed", "Remarks" : "Tech Stack Doens't exist"}
            return jsonify(output_data)
    return jsonify({"Status" : "Failed", "Remarks" : "Use POST method"})
    




@app.route('/')
def index_temp():
    tech_data = main.index()
    #print(tech_data)
    return render_template("index.html",data = tech_data )



@app.route('/out')
def out_temp():
    pass



if(__name__ == '__main__'):
    app.run(host='127.0.0.1', port=8080, debug=True)