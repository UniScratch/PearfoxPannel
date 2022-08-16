from flask import Flask,render_template
from mirai import Mirai, WebSocketAdapter, FriendMessage
import yaml,json,_thread

def botrun():

	bot.run()
# 导入配置
with open('./config.yml', 'r', encoding='utf-8') as f:
	config = yaml.load(stream=f, Loader=yaml.FullLoader)


bot = Mirai(
    qq=config['account'],
    adapter=WebSocketAdapter(
        verify_key=config['verifyKey'], host=config['host'], port=config['port']
    )
)

_thread.start_new_thread(botrun, ())
app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")


