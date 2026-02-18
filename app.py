from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_score(moisture, brix, fiber, node_length, weight):
    score = 0

    # Moisture (25 marks)
    if 65 <= moisture <= 75:
        score += 25
    else:
        score += max(0, 25 - abs(70 - moisture))

    # Brix (30 marks)
    if 18 <= brix <= 22:
        score += 30
    else:
        score += max(0, 30 - abs(20 - brix)*2)

    # Fiber (20 marks)
    if 10 <= fiber <= 15:
        score += 20
    else:
        score += max(0, 20 - abs(12 - fiber)*2)

    # Node Length (15 marks)
    if 8 <= node_length <= 12:
        score += 15

    # Weight (10 marks)
    if weight >= 1:
        score += 10

    return round(score, 2)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        moisture = float(request.form["moisture"])
        brix = float(request.form["brix"])
        fiber = float(request.form["fiber"])
        node_length = float(request.form["node_length"])
        weight = float(request.form["weight"])

        score = calculate_score(moisture, brix, fiber, node_length, weight)

        if score >= 85:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 50:
            grade = "C"
        else:
            grade = "D"

        return render_template("result.html", score=score, grade=grade)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
