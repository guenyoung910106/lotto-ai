
from flask import Flask, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_lotto_data():
    result = []
    for draw_no in range(1, 1169):
        url = f"https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={draw_no}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        numbers = soup.select(".num.win p span")
        if len(numbers) == 6:
            nums = [int(n.text.strip()) for n in numbers]
            result.append(nums)
    return result

@app.route("/api/winning-numbers")
def winning_numbers():
    data = get_lotto_data()
    return jsonify(data)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
