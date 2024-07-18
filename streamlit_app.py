import streamlit as st
import pandas as pd
import plotly.express as px # type: ignore
import plotly.graph_objects as go # type: ignore

# Webアプリケーションのタイトル
st.title('科目別成績の可視化')

# ユーザーからの入力を取得
subjects = ['国語', '数学', '英語', '理科', '社会']
scores = []

for subject in subjects:
    score = st.number_input(f'{subject}の点数', min_value=0, max_value=100, value=50, step=1)
    scores.append(score)

# データフレームの作成
df = pd.DataFrame({'科目': subjects, '点数': scores})

# 棒グラフの作成
fig_bar = px.bar(df, x='科目', y='点数', title='科目別の点数', labels={'点数': '点数', '科目': '科目'})

# レーダーチャートの作成
fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=scores,
    theta=subjects,
    fill='toself'
))
fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    showlegend=False,
    title='科目別の点数'
)

# グラフの表示
st.plotly_chart(fig_bar)
st.plotly_chart(fig_radar)
