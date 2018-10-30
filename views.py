from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/recommend/<int:film_id>')
def show_post(film_id):
	response = 'Film not found'
	knn_tbl = pd.read_csv("knn_tbl.csv",error_bad_lines=False)
	print('Film id passe est : ' + str(film_id))
	response = "You've picked " + knn_tbl.loc[film_id,'Film'] + " I recommend you : " + str(knn_tbl.loc[film_id,['Film1','Film2','Film3','Film4','Film5']])
	return response


if __name__ == "__main__":
    app.run()
