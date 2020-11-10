from flask import Flask, render_template, url_for, redirect, request, jsonify
from result import searchResult

app = Flask(__name__, template_folder='template')
app.jinja_env.globals.update(zip=zip)
app.config['SECRET_KEY'] = 'FKDJFKSLERJEWJRKKSDFNKSDJKEORIEWR'

@app.route('/', methods=['GET', 'POST'])
def input_string():
	if request.method == 'POST':
		ip = request.form['ip']	
		links, contents= searchResult(ip)
		return render_template('index.html', ip=ip, links=links, contents=contents, request=1)
	return render_template('index.html', request=0)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8080', debug=True)

