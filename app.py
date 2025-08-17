from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/file/<path:file_path>')
def redirect_file(file_path):
    # Redirect to Backblaze URL
    target_url = f'https://f002.backblazeb2.com/file/{file_path}'
    return redirect(target_url, code=301)

@app.route('/')
def index():
    return "Redirect app is working."

if __name__ == '__main__':
    app.run()
