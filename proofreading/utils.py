import openai
import os
from django.conf import settings
from server.settings import SECRET_KEY

APK_KEY = SECRET_KEY


def chat_gpt(prompt):
    openai.api_key = APK_KEY  # API KEYをセット
    openai.Model.list()  # OpenAIのインスタンスを生成

    # APIを使ってリクエストを投げる
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0

    )
    response = (response["choices"][0]["text"]).strip()
    return response


def create_prompt(input_text, file_name):
    prompt_file = os.path.join(settings.BASE_DIR, 'template', file_name)
    with open(prompt_file, encoding="utf-8") as f:
        file_read = f.read()
    # Chat-GTPへ投げるフォーマットに入力文をセットする。
    prompt = file_read.replace("[input]", input_text)
    return prompt
