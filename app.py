import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# 1. 페이지 기본 설정 (와이드 레이아웃)
st.set_page_config(page_title="지역 축제 방문객 분석", layout="wide")

# 2. 데이터 불러오기 함수
def load_data():
    # 파일명 정의 (사용자님의 파일명과 정확히 일치해야 합니다)
    files = {
        "2023": "2023년 지역축제 방문자수.csv",
        "2024": "2024년 지역축제 방문자수.csv",
        "2025": "2025년 지역축제 방문자수.csv"
    }
    
    # 파일 존재 여부 확인
    for year, file in files.items():
        if not os.path.exists(file):
            st.error(f"❌ 파일을 찾을 수 없습니다: {file}. CSV 파일이 app.py와 같은 폴더에 있는지 확인해주세요.")
            st.stop()
            
    # 각 연도 데이터 읽기
    df23 = pd.read_csv(files["2023"])
    df24 = pd.read_csv(files["2024"])
    df25 = pd.read_csv(files["2025"])
    
    # 2023년 데이터 전처리 (컬럼명이 다름: '개최장소')
    # 필요한 컬럼만 추출하여 표준화
    df23 = df23[['축제명', '전체방문객수']].rename(columns={'전체방문객수': '2023_방문객'})
    df24 = df24[['축제명', '전체방문객수']].rename(columns={'전체방문객수': '2024_방문객'})
    df25 = df25[['축제명', '전체방문객수']].rename(columns={'전체방문객수': '2025_방문객'})
    
    # 데이터 병합 (축제명 기준)
    merged_df = pd.merge(df25, df24, on='축제명', how='outer')
    merged_df = pd.merge(merged_df, df23, on='축제명', how='outer')
    
    return merged_df

# 데이터 로드
df = load_data()

# 3. 데이터 전처리 및 예외 처리
# 숫자형 변환 (에러 방지)
for col in ['2023_방문객', '2024_방문객', '2025_방문객']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# TOP 7 선정 (최신 연도인 2025년 방문객 기준 상위 7개)
top7 = df.sort_values(by='2025_방문객', ascending=False).head(7).copy()

# 3개년 평균 계산
top7['평균방문객'] = top7[['2023_방문객', '2024_방문객', '2025_방문객']].mean(axis=1)

# 단위 변환 (명 -> 만 명, 소수점 1자리)
for col in ['2023_방문객', '2024_방문객', '2025_방문객', '평균방문객']:
    top7[f'{col}_만명'] = (top7[col] / 10000).round(1)

# 4. 시각화 (Plotly)
st.title("📊 지역 축제 데이터 분석 대시보드")
st.subheader("지역 축제 방문객 TOP 7 — 3개년 추이 비교")

fig = go.Figure()

years = ['2023', '2024', '2025']
colors = ['#AB63FA', '#EF553B', '#00CC96'] # 시인성 높은 팔레트

# 막대 그래프 추가 (각 연도별)
for i, year in enumerate(years):
    col_name = f'{year}_방문객_만명'
    
    # 예외 처리 로직을 포함한 텍스트 리스트 생성
    text_labels = []
    hover_labels = []
    
    for idx, row in top7.iterrows():
        val = row[col_name]
        name = row['축제명']
        
        # 예외 1: 유성국화축제(2023 데이터 없음)
        if year == '2023' and "유성국화축제" in name and (pd.isna(val) or val == 0):
            text_labels.append("데이터 없음")
            hover_labels.append("데이터 없음")
        # 예외 2: 광복로 겨울빛 트리축제(2023 미개최)
        elif year == '2023' and "광복로" in name and val == 0:
            text_labels.append("0 (미개최)")
            hover_labels.append("미개최 (데이터 없음)")
        else:
            label = f"{val}만" if not pd.isna(val) else "데이터 없음"
            text_labels.append(label)
            hover_labels.append(f"{val}만 명" if not pd.isna(val) else "데이터 없음")

    fig.add_trace(go.Bar(
        x=top7['축제명'],
        y=top7[col_name],
        name=f'{year}년',
        marker_color=colors[i],
        text=text_labels,
        textposition='outside',
        customdata=hover_labels,
        hovertemplate='%{x}<br>' + f'{year}년: ' + '%{customdata}<extra></extra>'
    ))

# 꺾은선 그래프 추가 (3개년 평균)
fig.add_trace(go.Scatter(
    x=top7['축제명'],
    y=top7['평균방문객_만명'],
    name='3개년 평균',
    mode='lines+markers+text',
    line=dict(color='royalblue', width=4, dash='dot'),
    text=top7['평균방문객_만명'].apply(lambda x: f"<b>{x}만</b>"),
    textposition='top center',
    hovertemplate='%{x}<br>3개년 평균: %{y}만 명<extra></extra>'
))

# 레이아웃 설정
fig.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="축제명",
    yaxis_title="방문객 수 (단위: 만 명)",
    legend_title="구분",
    barmode='group',
    height=600,
    margin=dict(t=50, b=100),
    hovermode="x unified"
)

# 차트 출력
st.plotly_chart(fig, use_container_width=True)

# 5. 하단 정보 표기
st.caption("출처: 문화체육관광부 지역축제 개최계획 현황 (2023~2025)")

col1, col2 = st.columns(2)
with col1:
    st.info("💡 **축제의 생명력 및 지속성 검증**\n\n3개년 동안 방문객이 꾸준히 유지되거나 성장한 축제를 식별하여, 단발성 유행에 그치지 않고 지역의 고정 자산으로 자리 잡은 '앵커(Anchor) 축제'가 무엇인지 정량적으로 입증합니다.")
with col2:
    st.info("🎯 **전국구 축제의 하한선(Baseline) 설정**\n\nTOP 7 축제의 최소 방문객 기준을 파악함으로써, 향후 다른 지자체들이 '성공적인 지역 축제'의 목표치를 설정할 수 있는 벤치마크 가이드를 제공합니다.")
