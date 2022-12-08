import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 入門")  
#タイトルの追加
#streamlitモジュールのタイトル関数に名前を渡す
#実行はターミナルでstreamlit run ファイル名.py

st.write("DataFrame")
#テキストの追加

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,50,30,40]
})
#辞書型でデータふれ

st.write("・writeで表示")
st.write(df)
#streamlit.write(データ)で表示
#DataFrameはソート機能が追加されている

st.write("・dataframeで表示（サイズ変更）")
st.dataframe(df, width=100, height=100)
#sr.DataFrameでも表示できる
#writeと違ってサイズ変更ができる

st.write("・df.style.highlightで強調表示")
st.dataframe(df.style.highlight_max(axis=0))
#df.style.hightlight_max(axis=0(列))で最大値を強調表示

st.write("・tableで表を作成（ソート機能なし、表示するだけ）")
st.table(df)
#table（ソートできない(static=静的)表示するだけ


#マークダウン記法？
#見出しを作る
#pytho・・・以下の記述はpythonであることを示す（コピーできる）

st.write("・マークダウン記法？知らない")
"""
# 章
## 節
### 甲

```python
import streamlit as st
import numpy as np
import pandas as pd

```
"""


df2 = pd.DataFrame(
    np.random.rand(21,3), 
    #0以上1未満の乱数配列を作成、これだと20×3=60個の乱数を作成？
    columns = ['a','b','c']
)


st.write("・チャートの作成（保存できる）")
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)



st.write("・マッピング")
df3 = pd.DataFrame(
    np.random.rand(101,2)/[50,50] + [35.69, 139.79], 
    columns = ['lat','lon']  #lat=緯度、lon=経度
)
st.map(df3)


st.write("・画像の表示(PILを使用）")

if(st.checkbox("Show Image")): #check Boxにチェックが入ったら(True or False)
    img = Image.open("sample.png")
    st.image(img, caption="Test Image", use_column_width=True)


st.write("・セレクトボックス")
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,10))  #配列を渡す。
)

st.write("・Interactive Widgets")
st.write("・st.sidevbarを使うとサイドに表示することができる")
text = st.text_input("あなたの好きな趣味は？")

condition = st.slider("あなたのいまの調子は,",0,100,50)


"好きな趣味:", text
"コンディション:", condition


st.write("・カラムで分割表示")
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if(button):
    right_column.write("ここは右からむ")

st.write("・押すとしたに拡張表示する方法（expander）")
expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")


st.write("・プレグレスバーの表示")
st.write("Strat!")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteraion{i+1}') #テキスト表示の変更
    bar.progress(i+1) #barの表示を変更
    time.sleep(0.1)

st.write("終了！")
