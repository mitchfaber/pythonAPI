import MySQLdb
import json
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/get', methods=['GET'])
def api_get():
    try: 
        # opening database connection here!
        conn = MySQLdb.connect("DOMAIN NAME","USERNAME","PASSWORD","DB NAME")
        # prepare a cursor object using cursor() method
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # this is how to execute a SQL query with Python
        cursor.execute("SELECT * FROM tblStuff")
        # executing command and storing it in a variable to be sent as JSON
        all_grades = cursor.fetchall()
        return jsonify(all_grades)

    except ValueError as e:
        return ("Error getting records :(" + str(e))
    finally:
        conn.close()


@app.route('/post', methods=['POST'])
def api_post():
    try: 
        data = request.get_json()
        newTitle = data["title"]
        newAuthor = data["author"]
        # opening database connection here!
        conn = MySQLdb.connect("mitchfaber.ca","mitchfab_faberm","password1","mitchfab_dotnetcoreSamples")
        # prepare a cursor object using cursor() method
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        sql = "INSERT INTO tblStuff (title, author) VALUES (%s, %s)"

        val = (newTitle, newAuthor)
        # this is how to execute a SQL query with Python
        cursor.execute(sql, val)
        conn.commit()
        # executing command and storing it in a variable to be sent as JSON
        return "<h1>It sent!</h1>"
        

    except ValueError as e:
        print("Error getting records :(" + str(e))
    finally:
        conn.close()


@app.route('/put', methods=['PUT'])
def api_put():
    try: 
        id = request.args.get("id") 
        data = request.get_json()
        newTitle = data["title"]
        newAuthor = data["author"]
        # opening database connection here!
        conn = MySQLdb.connect("mitchfaber.ca","mitchfab_faberm","password1","mitchfab_dotnetcoreSamples")
        # prepare a cursor object using cursor() method
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        sql = "UPDATE tblStuff SET title=%s, author=%s WHERE ID=%s"

        val = (newTitle, newAuthor, id)
        # this is how to execute a SQL query with Python
        cursor.execute(sql, val)
        conn.commit()
        # executing command and storing it in a variable to be sent as JSON
        return "<h1>It sent!</h1>"
        

    except ValueError as e:
        print("Error getting records :(" + str(e))
    finally:
        conn.close()


@app.route('/delete', methods=['DELETE'])
def api_delete():
    try: 
        id = request.args.get("id") 
        # opening database connection here!
        conn = MySQLdb.connect("mitchfaber.ca","mitchfab_faberm","password1","mitchfab_dotnetcoreSamples")
        # prepare a cursor object using cursor() method
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        sql = "DELETE FROM tblStuff WHERE ID=%s"

        val = (id)
        # this is how to execute a SQL query with Python
        cursor.execute(sql, val)
        conn.commit()
        # executing command and storing it in a variable to be sent as JSON
        return "<h1>It sent!</h1>"
    except ValueError as e:
        print("Error getting records :(" + str(e))
    finally:
        conn.close()



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Uh-Oh! 404</h1><p>Nothing found... Check your URL! </p>", 404

app.run()
