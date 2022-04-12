from flask import Flask, request
import emoji, json

app = Flask(__name__)   

all_txt = None

with open('all.txt', 'r') as f:
    all_txt = f.readlines()
emojis = {}
for item in all_txt:
    item = item.strip()
    emojis[item] = emoji.emojize(item)


@app.route('/')
def emoji2pic():
    args = request.args
    emo = args.get("emoji", default="", type=str)
    return emoji.emojize(f'Hello {emo}!')
    
@app.route('/all')
def allemoji():
    return json.dumps(emojis, ensure_ascii=False)

