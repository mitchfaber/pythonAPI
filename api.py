import MySQLdb
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/grades/get', methods=['GET'])
def api_get():
    try: 
        # opening database connection here!
        conn = MySQLdb.connect("mitchfaber.ca","mitchfab_faberm","password1","mitchfab_dotnetcoreSamples")
        # prepare a cursor object using cursor() method
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # this is how to execute a SQL query with Python
        cursor.execute("SELECT * FROM tblGrades")
        # executing command and storing it in a variable to be sent as JSON
        all_grades = cursor.fetchall()
        return jsonify(all_grades)

    except ValueError as e:
        print("Error getting records :(" + str(e))
    finally:
        conn.close()


@app.route('/grades/get', methods=['POST'])
def api_post():
    try: 
        # opening database connection here!
        conn = MySQLdb.connect("mitchfaber.ca","mitchfab_faberm","password1","mitchfab_dotnetcoreSamples")
        # prepare a cursor object using cursor() method
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # this is how to execute a SQL query with Python
        cursor.execute("INSERT INTO tblGrades")
        # executing command and storing it in a variable to be sent as JSON
        all_grades = cursor.fetchall()
        return jsonify(all_grades)

    except ValueError as e:
        print("Error getting records :(" + str(e))
    finally:
        conn.close()



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Uh-Oh! 404</h1><p>Nothing found... Check your URL! </p>", 404

app.run()