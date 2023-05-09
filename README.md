## Djnago ＋ ChatGPT で作成した文章の校正アプリ
### 事前準備
```OpenAI```のAPIを取得するAPIキーを取得してください。<br>
取得後は```.text```ファイル等に保存しておいてください。<br>
<br>

### リポジトリのクローン後
```manage.py```と同じディレクトリ階層に```.env```ファイルを作成してください。<br>
作成したら事前に取得したAPIキーを下記の様に保存。<br>
```
SECRET_KEY=sk-.....(一意な英数字が並びます).....
```
<br>

続いてローカルにモジュールをインストールします。

```
pip install django openai
```
<br>

起動コマンドは通常通り
```
python manage.py runserver
```

<br>
これで```http://localhost:8000/grammar_correction```にアクセスすると文章の校正を正してくれるアプリが立ち上がります。

<br><br>

### 参考
（参考元です。環境変数を使用する様に一部変更しています）<br>
https://note.com/shinya_hd/n/nc9ba9f431e9b

<br>

環境変数をDjangoで使う方法<br>
もしかすると```django-environ```のインストールが求めれるかも知れません。<br>
その場合は下記リンク参考にしてください。<br>
https://uha-blog.com/python/django-environ/

<br><br>

### バージョン情報
Python 3.10.11<br>
Djnago 4.2<br>
django-environ 0.10.0<br>
openai 0.27.4<br>
