
from upload_video import *


from flask import Flask, render_template, request

app = Flask(__name__)

# Your existing code here
def your_function():
    # Your existing code logic here
    file_name_upload_per_file()
    service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME_D, API_VERSION, SCOPES_D)
    File_names, File_ids = list_drive_files(service, 'Youtube_Shorts')
    for file_id, title in zip(File_ids, File_names):
        print('Name & ID: ', title, ' --> ', file_id)
        if os.path.exists(title):
            os.remove(title)
            print('file removed after sucessful upload :) :) :) :):) :) :) :)')
        else:
            print('file not found to delete')

        try:
            service.files().delete(fileId=file_id).execute()
            print("File with ID {} deleted successfully from GDrive XXXX.".format(file_id))
        except Exception as e:
            print("An error occurred: {}".format(e))


    result = "COMPLETED!"
    return result

# Define a route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for handling a form submission (example)
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Call your existing function
        result = your_function()
        return render_template('result.html', result=result)

if __name__ == '__main__':
    import argparse
    app.run(debug=True)




