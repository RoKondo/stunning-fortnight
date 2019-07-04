from chalice import Chalice, NotFoundError

app = Chalice(app_name='todo')
app.debug = True
TODO = {
    '1': {
        'item': 'todo one'
    },
    '2': {
        'item': 'todo two'
    },
    '3': {
        'item': 'todo three'
    }
}



@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/todo')
def todos():
    return [ v for k, v in TODO.items() ]

@app.route('/todo/{item_id}')
def todo(item_id):
    if (item_id in TODO):
        return TODO[item_id]
    raise NotFoundError

@app.route('/todo/{item_id}', methods=['DELETE'])
def deletetodo(item_id):
    if (item_id in TODO):
        item = TODO[item_id]
        del TODO[item_id]
        return item
    raise NotFoundError

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
