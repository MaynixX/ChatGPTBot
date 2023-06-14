import openai

class ChatGpt:
    def __init__(self, api_key):
        openai.api_key = api_key
        models = openai.Model.list()
        self.model = models['data'][-1]['root']

    def ask(self, prompt, username):
        ans = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {'role': 'user', 'content': prompt, "name": username}
            ],
            temperature=0.9,
            stop=None,
            n=1
        )['choices'][0]['message']['content'].encode('utf-8').decode("utf-8")
        history = open('history.txt', 'a')
        history.write('Пользователь: @'+username+"\n"+'Вопрос: '+prompt+"\n"+'Ответ: '+ans+"\n\n")
        history.close()
        return ans