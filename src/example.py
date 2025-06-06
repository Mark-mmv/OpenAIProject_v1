import json
from openai import OpenAI
import settings

OPENAI_API_KEY = settings.OPENAI_API_KEY


class AIAssistant:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def respond(self, messages: list[dict], model: str = "gpt-4o-mini"):
        """
        Формирует запрос к модели с полным списком сообщений (chat history).
        messages — список словарей вида {"role": "user" | "assistant", "content": "..."}.
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        # Извлекаем текст из ответа
        assistant_message = response.choices[0].message.content
        return assistant_message


def main():
    assistant = AIAssistant(api_key=OPENAI_API_KEY)

    # История переписки — пустой список
    messages: list[dict] = [{"role": "assistant", "content": 'ВЫ два асистента ai. Начните обсуждать сколько бы мог стоить биткоин 1 января 2025 года'}]


    for idx in range(10):
        assistant1_reply = assistant.respond(messages)
        messages.append({"role": "assistant", "content": assistant1_reply})
        print("AI č1:", assistant1_reply)

        assistant2_reply = assistant.respond(messages)
        messages.append({"role": "assistant", "content": assistant2_reply})
        print("AI č2 :", assistant2_reply)


    # При выходе сохраняем всю историю в JSON-файл
    with open("transcription.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    print("История сохранена в transcription.json")


if __name__ == "__main__":
    main()