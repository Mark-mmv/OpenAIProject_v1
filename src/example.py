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
    messages: list[dict] = []

    print("Чат-бот запущен. Введите сообщение (или 'stopai' для выхода):")

    for idx in range(10):
        user_input = input("You: ").strip()
        if user_input.lower() == "stopai":
            break

        # Добавляем сообщение пользователя в историю
        messages.append({"role": "user", "content": user_input})

        # Отправляем всю историю в OpenAI и получаем ответ
        assistant_reply = assistant.respond(messages)

        # Добавляем ответ ассистента в историю
        messages.append({"role": "assistant", "content": assistant_reply})

        # Печатаем ответ на экран
        print("AI :", assistant_reply)

    # При выходе сохраняем всю историю в JSON-файл
    with open("transcription.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    print("История сохранена в transcription.json")


if __name__ == "__main__":
    main()