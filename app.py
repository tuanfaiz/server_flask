
from flask import Flask, request, jsonify, redirect, render_template
import json
import pandas as pd
import os


app = Flask(__name__)

# @app.route('/')
# def Output():
#     return render_template('Output.html')

@app.route("/post", methods=['POST', 'GET'])
def listener():
  
    if request.method == 'POST':
        data = request.json
        df = pd.DataFrame(data)
        print(df)

        if os.path.exists(f"{df['NAME'].iloc[0]}.csv"):

            df.to_csv(f"{df['NAME'].iloc[0]}.csv", mode ='a', index = False, header = False)

        else:

            df.to_csv(f"{df['NAME'].iloc[0]}.csv", mode ='a', index = False, header = True)


if __name__=="__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')