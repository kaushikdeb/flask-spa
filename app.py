from flask import Flask, send_from_directory
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/download')
def download():
    # return send_from_directory(filename='tmp\my-downloadable-file.txt', as_attachment=True)
    return send_from_directory(directory='tmp', filename='my-downloadable-file.txt', as_attachment=True)


if __name__ == '__main__':
    app.run()