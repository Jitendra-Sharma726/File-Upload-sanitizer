from flask import Flask, render_template, request, redirect, url_for
import os
#TODO: You will need to import 'secure_filename' from werkzeug.utils and the 'uuid' library.

app = Flask(__name__)
app.secret_key = 'supersecret_dev_key'

# Create the uploads directory if it doesn't exist
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index();
      return render
