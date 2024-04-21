from flask import Flask, request, jsonify
from flask_cors import CORS
from evenFind.spiders.event_spider import run_spider  # Assuming this is your Scrapy spider function
import csv
from analysis import sentence_similarity

app = Flask(__name__)
CORS(app)  # Allow any origin



userInput="I love coding"
data = []
string=""
similarity = [[]]
topNResult=3
finalResult=[]


@app.route('/initialize', methods=['POST'])
def run_spider_endpoint():
    # Your code here

    # Your code here
    try:
        global data
        data = run_spider()  # Trigger Scrapy spider and get data
        file_name = "events.csv"
        # Open the file in write mode ('w') and specify newline='' to prevent extra newlines
        with open(file_name, mode='w',newline='') as file:
            pass
        with open(file_name, mode='w', newline='') as file:
            file.write(data)
           
        return jsonify({'message': 'connected'}), 200
    except Exception as e:
        # Log the error message
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500

@app.route('/send-csv', methods=['POST'])
def send_csv():
    try:
        global userInput
        userInput = request.data.decode('utf-8')  # Decode the received data as UTF-8

        return jsonify({'message': 'CSV data received successfully'}), 200
    except Exception as e:
        # Log the error message
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500


@app.route('/rec', methods=['POST'])
def recommend():
    global data,userInput

    #userInput = request.form.get('userInput')  # Assuming 'userInput' is the key for the user input
    
    if not data or not userInput:
        return jsonify({"status": "error", "message": "Data or userInput is missing", "data": data, "userInput":userInput}), 400

   
    for i in data:
        total = 0
        for j in range (4,8):
            descrip = i[j]  # Assuming the description is at index 4
            if descrip and userInput:
                total += sentence_similarity(userInput, descrip)
        similarity[i] = [i,total]

    similarity.sort(key=lambda x: x[1], reverse=True)
        
    finalResult = [data[i[0]] + [i[1]] for i in similarity[:topNResult]]

    return jsonify( finalResult), 200

if __name__ == '__main__':
    app.run(debug=True)

