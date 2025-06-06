from openai import OpenAI


class AIAssistant:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def respond(self, massage: dict, model="gpt-4o-mini"):
        response = self.client.responses.create(model=model, input=massage)
        return response