from flask import Flask, render_template, request, redirect
import os
from src_.components.show_data_pipeline import ShowTable

app = Flask(__name__)

DATABASES_DIR = "artifacts/db_files"

@app.route('/')
def index():
    databases = [db for db in os.listdir(DATABASES_DIR) if db.endswith('.db')]
    return render_template('index.html', databases=databases)

@app.route('/view', methods=['POST'])
def view_db():
    database_name = request.form.get('dbname')
    if database_name:
        show_table = ShowTable(DATABASES_DIR, database_name)
        show_table.open_in_dtale()
        dtale_url = show_table.dtale_instance._url
        return redirect(dtale_url, code=302)
    return "Database not found", 404

if __name__ == '__main__':
    app.run(debug=True)
