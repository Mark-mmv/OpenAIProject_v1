import os
from ai_assistant import AIAssistant
import settings


OPENAI_API_KEY = settings.OPENAI_API_KEY


def main():
    assistant = AIAssistant(api_key=OPENAI_API_KEY)
    massage = ''
    while massage != 'stopai':
        print('Your massage: ')
        new_massage = input()
        massage += f'User: {new_massage} \n'
        ans = assistant.respond(massage=massage)
        massage += ans
        [print('# ',a) for a in ans]
        print(ans)
        with open("transcription.txt", "w", encoding="utf-8") as f:
            f.write(f"[{massage}")

if __name__ == '__main__':
    main()
