## 【個人開発】Djnago ＋ openAI で制作した釣りサポートサイト

<br>
現在開発中。
<br>

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
