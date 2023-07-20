from flask import Flask, jsonify, render_template
import requests




app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_data_from_api():
    # Replace 'API_ENDPOINT_URL' with the actual URL of the API you want to access
    api_endpoint = 'https://www.gamerpower.com/api/giveaways'

    try:
        response = requests.get(api_endpoint)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the API response is in JSON format
            data = response.json()
            return data

        # If the request was not successful, return an error message
        return jsonify({'error': 'Failed to fetch data from API'})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request error: {e}'})

@app.route("/")
def hello_world():
    data = get_data_from_api()
    return render_template("index.html",giveaways=data)

if __name__ == "__main__":
    app.run(debug=True)