from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# 設定你的 OpenAI API 金鑰
openai.api_key = 'KEY'
# 成員名字的映射
member_names = {
    "いとう りりあ": "伊藤 理々杏",
    "いわもと れんか": "岩本 蓮加",
    "うめざわ みなみ": "梅澤 美波",
    "くぼ しおり": "久保 史緒里",
    "さかぐち たまみ": "阪口 珠美",
    "さとう かえで": "佐藤 楓",
    "なかむら れの": "中村 麗乃",
    "むかい はづき": "向井 葉月",
    "やました みづき": "山下 美月",
    "よしだ あやのクリスティー": "吉田 綾乃クリスティー",
    "よだ ゆうき": "与田 祐希",
    "えんどう さくら": "遠藤 さくら",
    "かき はるか": "賀喜 遥香",
    "かけはし さやか": "掛橋 沙耶香",
    "かながわ さや": "金川 紗耶",
    "きたがわ ゆり": "北川 悠理",
    "くろみ はるか": "黒見 明香",
    "さとう りか": "佐藤 璃果",
    "しばた ゆな": "柴田 柚菜",
    "せいみや レイ": "清宮 レイ",
    "たむら まゆ": "田村 真佑",
    "つつい あやめ": "筒井 あやめ",
    "はやかわ せいら": "早川 聖来",
    "はやし るな": "林 瑠奈",
    "まつお みゆ": "松尾 美佑",
    "やくぼ みお": "矢久保 美緒",
    "ゆみき なお": "弓木 奈於",
    "いけだ てれさ": "池田 瑛紗",
    "いちのせ みく": "一ノ瀬 美空",
    "いのうえ なぎ": "井上 和",
    "おかもと ひな": "岡本 姫奈",
    "おがわ あや": "小川 彩",
    "おくだ いろは": "奥田 いろは",
    "かわさき さくら": "川﨑 桜",
    "すがわら さつき": "菅原 咲月",
    "とみさと なお": "冨里 奈央",
    "なかにし アルノ": "中西 アルノ"
}

def translate(text):
    # 建立一個新的 ChatCompletion 物件
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "將以下訊息以日本女子偶像團體成員的口吻翻譯成繁體中文 ％％％維持原樣。另外，文字的格式如：表情符號、標點、換行請按照原本的格式"},
            {"role": "system", "content": "以下是一些成員的名字映射，可以用來參考翻譯名字：{}".format(", ".join(f"{kana} -> {name}" for kana, name in member_names.items()))},
            {"role": "system", "content": "注意名字也要符合格式，如果原本內容只有姓，那翻譯留姓就好，以此類推，以下為要翻譯的內容："},
            {"role": "user", "content": text}
        ]
    )

    # 返回翻譯後的文本
    return completion.choices[0].message['content'].replace('\n', '<br>')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        translated_text = translate(text)
        return jsonify({'translated_text': translated_text})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
