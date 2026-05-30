import었습니다.

#### **파일 2: app.py**
```python
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# 1. 페이지 기본 설정 (와이드 모드)
st.set_page_config(layout="wide", page_title="지역축제 방문객 분석")

# 2. 데이터 불러오기 함수
def load_data():
    files = {
        "2023": "202 streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# 1. 페이지 기본3년 지역축제 방문자수.csv",
        "2024": "2024 설정 (와이드 레이아웃)
st.set_page_config(page_title="지역 축제년 지역축제 방문자수.csv",
        "2025": "2025년 방문객 분석", layout="wide")

# 2. 데이터 불러오기 함수
def load_data():
     지역축제 방문자수.csv"
    }
    
    # 파일 존재 여부 확인
    for yearfiles = {
        2023: "2023년 지역축제 방문자수.csv, file in files.items():
        if not os.path.exists(file):
            st.error(",
        2024: "2024년 지역축제 방문자수.csv",
f"🚨 파일을 찾을 수 없습니다: {file}\n데이터 파일이 같은 폴더에 있는지 확인해주세요.")
            st        2025: "2025년 지역축제 방문자수.csv"
    }
    
    # 파일 존재 여부 확인
    for year, file in files.items():
        if not os.path..stop()
            
    # 데이터 읽기 (축제명과 방문객수 위주로 추출)
    df23exists(file):
            st.error(f"❌ 파일을 찾을 수 없습니다: {file}. CSV 파일이 app = pd.read_csv(files["2023"])
    df24 = pd.read_csv(files.py와 같은 폴더에 있는지 확인해주세요.")
            st.stop()
            
    # 각 연도 데이터 읽기
    df23 = pd.read_csv(files[2023])
    df24 = pd.read_csv(files[2024])
    df25 = pd.read_csv(files[2025])
    
    # 2023년 컬럼명 표준화 (요청사항 반영)
    # 2023년은 '개최장소'를 사용하므로, 공통 분석을 위해 '축제명'과 '전체방문객수' 위주로 정리
    df23 = df23[['축제명', '전체방문객수']].copy()
    df24 = df24[['축제명', '전체방문객수']].copy()
    df25 = df25[['축제명', '전체방문객수']].copy()
    
    # 데이터 병합 (축제명 기준)
    df = pd.merge(df24, df25, on='축제명', how='outer', suffixes=('_2024', '_2025'))
    df = pd.merge(df, df23, on='축제명', how='outer')
    df.rename(columns={'전체방문객수': '전체방문객수_2023'}, inplace=True)
    
    # 숫자형으로 변환 및 결측치 처리 (유성국화축제 2023 예외 처리 포함)
    for col in ['전체방문객수_2023', '전체방문객수_2024', '전체방문객수_2025']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
    return df

# 데이터 로드
try:
    df_raw = load_data()
except Exception as e:
    st.error(f"데이터를 처리하는 중 오류가 발생했습니다: {e}")
    st.stop()

# 3. 데이터 전처리 및 TOP 7 추출
# 3개년 평균 계산
df_raw['평균방문객수'] = df_raw[['전체방["2024"])
    df25 = pd.read_csv(files["2025"])
    
    # 2023년 예외 처리: '개최장소' 컬럼 무시하고 필요한 컬럼만 선택
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
# 유성국화축제(대전) 2023년 데이터는 NaN 또는 0으로 처리 (이미 merge 과정에서 매칭 안되면 NaN)
# 광복로 겨울빛 트리축제(부산) 2023년 0점은 그대로 유지

# 3개년 평균 계산 (NaN은 0으로 간주하고 계산)
df['평균방문객'] = df[['2023_방문객', '2024_방문객', '2025_방문객']].mean(axis=1, skipna=True)

# TOP 7 선정 (최신 연도인 2025년 방문객 기준 상위 7개)
top7 = df.sort_values(by='2025_방문객', ascending=False).head(7).문객수_2023', '전체방문객수_2024', '전copy()

# 단위 변환 (명 -> 만 명)
for col in ['2023_방문객', '2024_방문객', '2025_방문객', '평균방체방문객수_2025']].mean(axis=1)

# TOP 7 축제 선정문객']:
    top7[col + '_만명'] = top7[col] / 100 (평균 방문객수 기준 정렬)
df_top7 = df_raw.sort_values(by='평균방문객수', ascending=False).head(7).reset_index(drop=True)00

# 4. 시각화 (Plotly)
st.title("📊 지역 축제 방문객 TOP

# 단위 변환: 만 명 (소수점 1자리)
for col in ['전체방 7 추이 분석")
st.subheader("2023년 ~ 2025년 방문문객수_2023', '전체방문객수_2024', '전객 변화 및 3개년 평균")

fig = go.Figure()

# 막대 그래프 추가 (2023,체방문객수_2025', '평균방문객수']:
    df_top 2024, 2025)
years = ['2023', '2024', '2025']
colors = ['#D3D3D3', '#907[f'{col}_label'] = (df_top7[col] / 10000).round(1)

# 4. 시각화 (Plotly)
st.title("📊 지역 축제 데이터 분석CAF9', '#1E88E5'] # 연해지는 회색에서 진한 파랑으로

for 대시보드")
st.subheader("지역 축제 방문객 TOP 7 — 3개년 추이 비교")

fig = go.Figure()

years = [2023, 2024, 2025 year, color in zip(years, colors):
    col_name = f'{year}_방문객_만명'
    
    # 툴팁(hover) 설정
    hover_text = []
    ]
colors = ['#AB63FA', '#EF553B', '#00CC96'] #for i, row in top7.iterrows():
        val = row[col_name]
        name = row['축제명 시인성 높은 팔레트

# 막대 그래프 추가 (각 연도별)
for i, year']
        if pd.isna(val) and name == '유성국화축제':
            hover_text.append("데이터 없음")
        elif val == 0 and name == '광복로 겨울빛 in enumerate(years):
    col_name = f'전체방문객수_{year}'
    label_col 트리축제' and year == '2023':
            hover_text.append("미개최 (데이터 없음)") = f'{col_name}_label'
    
    # 텍스트 레이블 생성 (예외 처리
        else:
            hover_text.append(f"{val:.1f}만 명")

    fig.add_ 로직 포함)
    text_labels = []
    for idx, row in df_top7.iterrows():
        val = row[label_col]
        festival = row['축제명']
        
        # 예trace(go.Bar(
        x=top7['축제명'],
        y=top7[col_name],
        name=f'{year}년',
        marker_color=color,
        text=[f"{v외 1: 유성국화축제(2023 데이터 없음)
        if year == 2023:.1f}" if not pd.isna(v) and v > 0 else "" for v in top7[col and "유성국화축제" in festival and val == 0:
            text_labels.append("데이터 없음")
        # 예외 2: 광복로 겨울빛 트리축제(202_name]],
        textposition='outside',
        hovertemplate='%{x}<br>' + f'{3 미개최)
        elif year == 2023 and "광복로" in festival and val == 0:
            text_labels.append("0 (미개최)")
        else:
            year}년: ' + '%{customdata}<extra></extra>',
        customdata=hover_text
    text_labels.append(f"{val}만")

    fig.add_trace(go.Bar(
))

# 꺾은선 그래프 추가 (평균)
fig.add_trace(go.Scatter(
            x=df_top7['축제명'],
        y=df_top7[col_name]x=top7['축제명'],
    y=top7['평균방문객_만명 / 10000,
        name=f'{year}년',
        marker_color=colors['],
    name='3개년 평균',
    mode='lines+markers+text',
    line=dict(colori],
        text=text_labels,
        textposition='outside',
        hovertemplate='%{x='#FF7043', width=3, dash='dot'),
    text=[f"{v:.1f}<br>%{json_name}: %{y}만 명<extra></extra>'
    ))

# 꺾은선}" for v in top7['평균방문객_만명']],
    textposition='top center',
    hovertemplate 그래프 추가 (3개년 평균)
fig.add_trace(go.Scatter(
    x=df_top7['='%{x}<br>3개년 평균: %{y:.1f}만 명<extra></extra>'
축제명'],
    y=df_top7['평균방문객수'] / 1000))

# 레이아웃 설정
fig.update_layout(
    barmode='group',
    xaxis0,
    name='3개년 평균',
    mode='lines+markers+text',
    line=dict(color_tickangle=-45,
    xaxis_title="축제명",
    yaxis_title="방='royalblue', width=4, dash='dot'),
    text=df_top7['평균방문객수_label문객 수 (단위: 만 명)",
    legend_title="구분",
    margin=dict(l'].apply(lambda x: f"<b>{x}만</b>"),
    textposition='top center',
    yaxis=20, r=20, t=50, b=100),
    height=6='y'
))

# 레이아웃 설정
fig.update_layout(
    xaxis_tickangle00,
    hovermode="x unified"
)

# 차트 출력
st.plotly_chart(fig,=-45,
    xaxis_title="축제명",
    yaxis_title="방문객 수 (단위: use_container_width=True)

# 5. 하단 정보 영역
st.caption("출처: 문화체 만 명)",
    legend_title="구분",
    barmode='group',
    height=6육관광부 지역축제 개최계획 현황 (2023~2025)")

00,
    margin=dict(t=50, b=100),
    hovermode="col1, col2 = st.columns(2)

with col1:
    st.info("💡 **축제의 생명력 및 지속성 검증**\n\n3개년 동안 방문객이 꾸준히 유지되거나 성장한 축제를 식별하여, 단발성 유행에 그치지 않고 지역의 고정x unified"
)

# 차트 출력
st.plotly_chart(fig, use_container_width=True)

 자산으로 자리 잡은 '앵커(Anchor) 축제'가 무엇인지 정량적으로 입증합니다.")

with col2:
    st.info("🎯 **전국구 축제의 하한선(Baseline)# 5. 하단 정보 표기
st.caption("출처: 문화체육관광부 지역축 설정**\n\nTOP 7 축제의 최소 방문객 기준을 파악함으로써, 향후 다른 지제 개최계획 현황 (2023~2025)")

st.info("💡 **인자체들이 '성공적인 지역 축제'의 목표치를 설정할 수 있는 벤치마크 가이드를 제공합니다.")