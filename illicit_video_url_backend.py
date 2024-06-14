from flask import Flask, request
import pandas as pd

app = Flask(__name__)

# Load the data for illicit video URLs
illicit_video_urls = pd.read_csv('illicit_video.csv')['MovieURL'].tolist()

@app.route('/illicit_video/predict_url', methods=['POST'])
def predict_illicit_video_url():
    url = request.form['url']
    if url in illicit_video_urls:
        result = 'Illicit Video URL'
    else:
        result = 'Safe URL'
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)