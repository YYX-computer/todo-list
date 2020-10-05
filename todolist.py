from flask import Flask,render_template
todolist = []
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('todolist.html')
@app.route('/api/todolist/checkItems',methods=['POST'])
def checkTodo():
	return str(todolist),200
@app.route('/api/todolist/delItem/<int:item>',methods=['POST'])
def delTodo(item):
	todolist.pop(item)
	return ''
@app.route('/api/todolist/addItem/<content>',methods=['POST'])
def addTodo(content):
	todolist.append(content)
	return ''
app.run()
