from flask import render_template, request, jsonify, session
from app import db
from app.chatbot import chatbot
from app.models import ChatMessage
import uuid


RESPONSES = {
    'hello': 'Hello! Welcome to Isamani Tours. How can I help you today?',
    'hi': 'Hi there! How can I assist you?',
    'tours': 'We offer Kilimanjaro climbs, Mount Meru treks, and day trips. Which interests you?',
    'price': 'Our tours start from $800. Visit our tours page for full pricing.',
    'booking': 'You can book directly on our website or contact us at info@isamani.com',
    'kilimanjaro': 'Kilimanjaro is the highest peak in Africa at 5,895m. We offer 7-9 day climbs.',
    'bye': 'Goodbye! Have a great day!',
}


def get_bot_response(message):
    message_lower = message.lower().strip()

    if message_lower in RESPONSES:
        return RESPONSES[message_lower]

    return "Sorry i dont understnd that. Can you rephrase?"


@chatbot.route('/')
def index():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

    history = ChatMessage.query.filter_by(
        session_id=session['session_id']
    ).order_by(ChatMessage.timestamp).all()

    return render_template('chatbot/index.html', history=history)


@chatbot.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    user_message = data.get('message', '')

    bot_response = get_bot_response(user_message)

    msg = ChatMessage(
        user_message=user_message,
        bot_response=bot_response,
        session_id=session.get('session_id', 'anonymous')
    )
    db.session.add(msg)
    db.session.commit()

    return jsonify({
        'response': bot_response,
        'timestamp': msg.timestamp.strftime('%H:%M')
    })


@chatbot.route('/clear', methods=['POST'])
def clear_history():
    return jsonify({'status': 'ok'})
