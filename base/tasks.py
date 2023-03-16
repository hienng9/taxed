
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from .chat import get_response_chatbot
channel_layer = get_channel_layer()

@shared_task
def get_response(channel_name, input_data):
    # chatterbot = ChatBot(**settings.CHATTERBOT)
    response = get_response_chatbot(input_data['text'])
    # response_data = response.serialize()

    async_to_sync(channel_layer.send)(
        channel_name,
        {
            "type": "chat_message",
            "text": {"msg": response, "source": "bot"},
        },
    )