from flask import Flask, jsonify
import random
import emoji

app = Flask(__name__)

moods = [
    ("happy", "😄"),
    ("chaotic", "🌀"),
    ("sleepy", "😴"),
    ("mysterious", "🕵️"),
    ("dramatic", "🎭"),
    ("confused", "🤯")
]

fortunes = [
    "Today is suspiciously productive...",
    "You will debug something on the first try. Unsettling.",
    "Your code will work... but you won’t know why.",
    "A bug will disappear when you show it to someone.",
    "You will fix one thing and break 375474502394774 more.",
    "The solution is simpler than you think. Or...?",
    "Someone will say 'I passed all my courses last semester'."
]

@app.route("/")
def home():
    return "🔮 Welcome to the Mood Fortune Teller API! 🔮"

@app.route("/fortune")
def fortune():
    mood, mood_emoji = random.choice(moods)
    fortune_text = random.choice(fortunes)

    return jsonify({
        "mood": mood,
        "emoji": emoji.emojize(mood_emoji),
        "fortune": fortune_text
    })

@app.route("/whatsup")
def health():
    return jsonify({"status": "alive and slightly burnt out"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)