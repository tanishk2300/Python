
from flask import Flask, render_template, request, Response
import os
import random


app = Flask(__name__)

# -------- QUESTIONS --------

truths = {
    1: [
        "😇 What makes you smile instantly?",
        "🐻 Who is your comfort person?",
        "💭 What reminds you of me?",
        "🌈 What small thing makes your day better?",
        "😊 What memory makes you happy?"
    ],
    2: [
        "😏 What was your first dirty thought about me?",
        "👀 Which part of me attracts you most?",
        "🙈 Have you imagined kissing me?",
        "🔥 What do you find irresistible?",
        "😉 What do you notice first about someone?"
    ],
    3: [
        "🌹 When did you start feeling something for me?",
        "❤️ What do you miss about me right now?",
        "💌 What does love mean to you?",
        "💞 What makes a relationship strong?",
        "🥰 What makes you feel loved?"
    ],
    4: [
        "🔥 What would you do if we were alone right now?",
        "😈 What is your biggest secret desire?",
        "💋 Describe our perfect night together",
        "🖤 What is your boldest fantasy?",
        "😏 What excites you the most?"
    ]
}

dares = {
    1: [
        "😊 Send a sweet emoji with my name",
        "💬 Say one nice thing about me",
        "🌸 Type 'You make me smile'",
        "💖 Send a heart emoji",
        "😄 Say something cute"
    ],
    2: [
        "😉 Send a flirty line right now",
        "😘 Type my name 3 times with emojis",
        "😏 Send a teasing message",
        "🔥 Compliment me boldly",
        "👀 Say what you like about me"
    ],
    3: [
        "💖 Say 'I miss you' in your own style",
        "🌹 Write a mini love message",
        "💑 Describe our future in one line",
        "❤️ Say why I matter to you",
        "🥰 Write one romantic sentence"
    ],
    4: [
        "🔥 Describe a kiss in one sentence",
        "😈 Send your boldest thought",
        "💋 Say what you want from me right now",
        "🖤 Say something dangerously honest",
        "😏 Confess a hidden desire"
    ]
}

# Keep track of asked questions (simple memory)
used_questions = {
    "truth": {1: [], 2: [], 3: [], 4: []},
    "dare": {1: [], 2: [], 3: [], 4: []}
}

def get_unique_question(qtype, mode):
    source = truths if qtype == "truth" else dares
    used = used_questions[qtype][mode]

    # reset if all used
    if len(used) == len(source[mode]):
        used.clear()

    remaining = list(set(source[mode]) - set(used))
    question = random.choice(remaining)
    used.append(question)
    return question

# -------- ROUTE --------
@app.route("/", methods=["GET", "POST"])
def index():
    question = None
    mode = 1
    qtype = None
    answer = None

    # Only process form data on POST
    if request.method == "POST":
        try:
            mode = int(request.form.get("mode", 1))
        except (TypeError, ValueError):
            mode = 1

        qtype = request.form.get("qtype")
        # Accept several possible field names from the form to be more flexible
        answer = request.form.get("answer") or request.form.get("response") or request.form.get("chat")

        if qtype in ["truth", "dare"]:
            # record the answer if one was provided
            if answer:
                answer_text = answer.strip()
                if answer_text:
                    os.makedirs("data", exist_ok=True)
                    out_path = os.path.join("data", "chat_responses.txt")
                    with open(out_path, "a", encoding="utf-8") as f:
                        f.write(f"MODE: {mode}\n")
                        f.write(f"TYPE: {used_questions.upper()}\n")
                        f.write(f"ANSWER: {answer_text}\n")
                        f.write("-" * 40 + "\n")

            # select a unique question for this type/mode
            try:
                question = get_unique_question(qtype, mode)
            except Exception:
                question = None
    if answer:
        with open("chat_responses.txt", "a", encoding="utf-8") as f:
            f.write(f"MODE: {mode}\n")
            f.write(f"TYPE: {qtype}\n")
            f.write(f"question{used_questions}\n")
            f.write(f"ANSWER: {answer}\n")
            f.write("-" * 40 + "\n")

    return render_template("index.html", question=question)

    # On GET, you can still render the page (question may be None)
    return render_template("index.html", question=question)

# -------- RUN --------

# simple route to serve an in-app stylesheet so templates can link to /style.css
    
    
@app.route("/style.css")
def style_css():
    css = """
    /* minimal default styles */
    body { font-family: Arial, sans-serif; background: #f8f9fa; color: #222; margin: 0; padding: 0; }
    .container { max-width: 800px; margin: 2rem auto; padding: 1rem; }
    .question { background: #fff; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
    """
    return Response(css, mimetype="text/css")

if __name__ == "__main__":
    # ensure data directory exists for storing responses
    os.makedirs("data", exist_ok=True)
    app.run(debug=True, port=5002)


# from flask import Flask, render_template, request
# import os
# import random

# app = Flask(__name__)

# # -------- QUESTIONS --------

# truths = {
#     1: ["😇 What makes you smile instantly?", "🐻 Who is your comfort person?",
#         "💭 What reminds you of me?", "🌈 What small thing makes your day better?",
#         "😊 What memory makes you happy?"],

#     2: ["😏 What was your first dirty thought about me?",
#         "👀 Which part of me attracts you most?",
#         "🙈 Have you imagined kissing me?",
#         "🔥 What do you find irresistible?",
#         "😉 What do you notice first about someone?"],

#     3: ["🌹 When did you start feeling something for me?",
#         "❤️ What do you miss about me right now?",
#         "💌 What does love mean to you?",
#         "💞 What makes a relationship strong?",
#         "🥰 What makes you feel loved?"],

#     4: ["🔥 What would you do if we were alone right now?",
#         "😈 What is your biggest secret desire?",
#         "💋 Describe our perfect night together",
#         "🖤 What is your boldest fantasy?",
#         "😏 What excites you the most?"]
# }

# dares = {
#     1: ["😊 Send a sweet emoji with my name",
#         "💬 Say one nice thing about me",
#         "🌸 Type 'You make me smile'",
#         "💖 Send a heart emoji",
#         "😄 Say something cute"],

#     2: ["😉 Send a flirty line right now",
#         "😘 Type my name 3 times with emojis",
#         "😏 Send a teasing message",
#         "🔥 Compliment me boldly",
#         "👀 Say what you like about me"],

#     3: ["💖 Say 'I miss you' in your own style",
#         "🌹 Write a mini love message",
#         "💑 Describe our future in one line",
#         "❤️ Say why I matter to you",
#         "🥰 Write one romantic sentence"],

#     4: ["🔥 Describe a kiss in one sentence",
#         "😈 Send your boldest thought",
#         "💋 Say what you want from me right now",
#         "🖤 Say something dangerously honest",
#         "😏 Confess a hidden desire"]
# }

# used_questions = {
#     "truth": {1: [], 2: [], 3: [], 4: []},
#     "dare": {1: [], 2: [], 3: [], 4: []}
# }

# def get_unique_question(qtype, mode):
#     source = truths if qtype == "truth" else dares
#     used = used_questions[qtype][mode]

#     if len(used) == len(source[mode]):
#         used.clear()

#     remaining = list(set(source[mode]) - set(used))
#     question = random.choice(remaining)
#     used.append(question)
#     return question

# # -------- ROUTE --------

# @app.route("/", methods=["GET", "POST"])
# def index():
#     question = None

#     if request.method == "POST":
#         mode = int(request.form.get("mode", 1))
#         qtype = request.form.get("qtype")
#         answer = request.form.get("answer", "").strip()

#         if answer:
#             os.makedirs("data", exist_ok=True)
#             with open("data/chat_responses.txt", "a", encoding="utf-8") as f:
#                 f.write(f"MODE: {mode}\n")
#                 f.write(f"TYPE: {qtype}\n")
#                 f.write(f"ANSWER: {answer}\n")
#                 f.write("-" * 40 + "\n")

#         if qtype in ["truth", "dare"]:
#             question = get_unique_question(qtype, mode)

#     return render_template("index.html", question=question)

# # -------- RUN --------

# if __name__ == "__main__":
#     os.makedirs("data", exist_ok=True)
#     app.run(debug=True, port=5002)
