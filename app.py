from flask import Flask, render_template, request, redirect
from src_.components.show_data_pipeline import ShowTable  # Assuming your pipeline file is named show_table_pipeline.py
import os

app = Flask(__name__)

DATABASES_DIR = "/Users/archismanchakraborti/Desktop/python_files/HRI_Research_Work/Data_management/artifacts/db_files"

@app.route('/')
def index():
    # Get a list of all database names in the directory
    database_names = [f for f in os.listdir(DATABASES_DIR) if f.endswith('.db')]
    return render_template('index.html', databases=database_names)

@app.route('/view', methods=['GET'])
def view_db():
    dbname = request.args.get('dbname')
    if dbname:
        show_table = ShowTable(DATABASES_DIR, dbname)
        show_table.open_in_dtale()
        dtale_url = show_table.dtale_instance._url
        return redirect(dtale_url)
    return "Database not found", 404

if __name__ == '__main__':
    app.run(debug=True)
