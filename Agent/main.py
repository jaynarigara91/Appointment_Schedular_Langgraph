from Agent.Agents import Appointment
from langchain_core.messages import HumanMessage
from flask_cors import CORS
from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)  

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Chatbot API! Use POST /chat to interact with the chatbot."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_question = data.get("question", "")
    print(user_question)
    if not user_question:
        return jsonify({"error": "Question is required"}), 400
    try:
        config = {"configurable": {"thread_id": "ssfjays"}}
        response = graph.invoke({"messages": [HumanMessage(content=user_question)]},config=config)
        return jsonify({"response": response['messages'][-1].content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__=="__main__":
    agent = Appointment()
    graph = agent()
    app.run(debug=True, use_reloader=False)

