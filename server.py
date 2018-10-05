from flask import render_template
import connexion

#app instance
app = connexion.App(__name__, specification_dir='./')

#read the swagger.yml file
app.add_api('swagger.yml')

#URL route for /
@app.route('/', methods=['GET'])
def home():
        '''<h1>Phone Customers</h1>
        <p>Telephone Customers</p>'''
        return render_template('home.html')

#run app if running in stand alone mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
