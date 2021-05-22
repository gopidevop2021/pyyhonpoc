from flask import Flask, request, make_response
from flask import render_template,jsonify

app = Flask(__name__)

##### viewing the template #####
@app.route('/')
def home():
     return render_template("home.html")

@app.route('/save')
def mainpage():
    return render_template("save.html")


# ####### getting the file name and path details #######
# @app.route('/insert',methods = ['POST', 'GET'])
# def insert():
#     file_name = request.form['nm']
#     global file_location
#     file_location = str(file_path) + str(file_name)
#
#     if os.path.exists(os.path.join(os.path.dirname(__file__), file_location)):
#         df = pd.read_csv(file_location)
#         file_details = df.T.to_dict().values()
#         data_list.append(file_details)
#         dict = {file_location: file_details}
#         file_list.append(dict)
#         return render_template('display.html', data=df.to_html())
#     else:
#         error = "No Such Record Found......! "
#         return jsonify({"Error": error})

##### Getting field declaration based on our dataset  #####
@app.route('/field')
def field():
    return render_template("fields.html")



#### execution starts here ####
if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5000,threaded=True,debug=True)
