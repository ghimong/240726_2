import streamlit as st
import matplotlib.pyplot as plt
st.title('나의 에니어그램은 무엇일까?')
import numpy as np

# 질문 리스트 (18가지)
questions = [
    "나는 항상 더 나은 방법을 찾으려고 노력한다.",
    "나는 다른 사람들을 돕는 것을 좋아한다.",
    "나는 목표를 달성하기 위해 열심히 노력한다.",
    "나는 나만의 특별한 스타일을 가지고 있다.",
    "나는 항상 새로운 지식을 추구한다.",
    "나는 신뢰할 수 있는 친구가 되기를 원한다.",
    "나는 항상 새로운 경험을 찾는다.",
    "나는 내 의견을 강하게 주장한다.",
    "나는 평화를 유지하기 위해 노력한다.",
    "나는 작은 세부사항에도 신경을 쓴다.",
    "나는 규칙과 절차를 중요하게 생각한다.",
    "나는 사람들과 깊이 있는 대화를 즐긴다.",
    "나는 경쟁에서 승리하는 것을 좋아한다.",
    "나는 독창적인 아이디어를 내는 것을 즐긴다.",
    "나는 문제를 해결하기 위해 다양한 접근법을 시도한다.",
    "나는 충성심이 강하고 믿음직한 사람이다.",
    "나는 항상 낙관적이고 긍정적인 태도를 유지한다.",
    "나는 위험을 감수하는 것을 두려워하지 않는다."
]

# 애니어그램 유형별 점수 초기화
score = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

# 스트림릿 앱 설정
st.title("애니어그램 성격 테스트")
st.write("다음 질문에 답변해 주세요:")

# 사용자 응답 수집
for i, question in enumerate(questions):
    st.write(f"{i+1}. {question}")
    answer = st.radio("", ["전혀 그렇지 않다", "그렇지 않다", "보통이다", "그렇다", "매우 그렇다"], key=f"q{i}")

    # 점수 계산 (간단한 예시로 각 질문마다 특정 유형에 점수를 부여)
    if i in [0, 9, 10]:
        score['1'] += answer == "매우 그렇다"
    elif i in [1, 11]:
        score['2'] += answer == "매우 그렇다"
    elif i in [2, 12]:
        score['3'] += answer == "매우 그렇다"
    elif i in [3, 13]:
        score['4'] += answer == "매우 그렇다"
    elif i in [4, 14]:
        score['5'] += answer == "매우 그렇다"
    elif i in [5, 15]:
        score['6'] += answer == "매우 그렇다"
    elif i in [6, 16]:
        score['7'] += answer == "매우 그렇다"
    elif i in [7, 17]:
        score['8'] += answer == "매우 그렇다"
    elif i in [8]:
        score['9'] += answer == "매우 그렇다"

# 결과 계산
if st.button("결과 보기"):
    max_score = max(score.values())
    result_type = [key for key, value in score.items() if value == max_score]

    # 애니어그램 유형별 설명과 추천 정보
    results_info = {
        '1': ("유형 1: 개혁가", "화이트, 네이비 블루", "깔끔하고 클래식한 스타일", "유형 7(열정가), 유형 9(평화주의자)", "유형 8(도전자)"),
        '2': ("유형 2: 조력자", "핑크, 라벤더", "로맨틱하고 따뜻한 느낌의 패션", "유형 9(평화주의자), 유형 3(성취자)", "유형 5(탐구자)"),
        '3': ("유형 3: 성취자", "골드, 레드", "세련되고 현대적인 스타일", "유형 2(조력자), 유형 6(충성가)", "유형 4(개인주의자)"),
        '4': ("유형 4: 개인주의자", "퍼플, 블랙", "예술적이고 독특한 스타일", "유형 5(탐구자), 유형 9(평화주의자)", "유형 3(성취자)"),
        '5': ("유형 5: 탐구자", "그레이, 딥 블루", "지적이고 심플한 스타일", "유형 4(개인주의자), 유형 6(충성가)", "유형 2(조력자)"),
        '6': ("유형 6: 충성가", "그린, 브라운", "실용적이고 안정적인 스타일", "유형 3(성취자), 유형 9(평화주의자)", "유형 7(열정가)"),
        '7': ("유형 7: 열정가", "오렌지, 옐로우", "밝고 활기찬 스타일", "유형 1(개혁가), 유형 6(충성가)", "유형 6(충성가)"),
        '8': ("유형 8: 도전자", "블랙, 레드", "강렬하고 자신감 있는 스타일", "유형 2(조력자), 유형 7(열정가)", "유형 1(개혁가)"),
        '9': ("유형 9: 평화주의자", "베이지, 파스텔톤", "편안하고 자연스러운 스타일", "유형 1(개혁가), 유형 2(조력자)", "유형 3(성취자)")
    }

    st.write(f"당신의 애니어그램 유형은: 유형 {', '.join(result_type)}")

    for r_type in result_type:
        st.write(f"{results_info[r_type][0]}")
        st.write(f"- **어울리는 색깔:** {results_info[r_type][1]}")
        st.write(f"- **스타일:** {results_info[r_type][2]}")
        st.write(f"- **잘 맞는 친구:** {results_info[r_type][3]}")
        st.write(f"- **피해야 할 친구:** {results_info[r_type][4]}")

    # 점수를 퍼센트로 변환
    total_questions = len(questions)
    percent_score = {key: (value / total_questions) * 100 for key, value in score.items()}

    # 방사형 그래프 그리기
    labels = list(percent_score.keys())
    stats = list(percent_score.values())

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    stats += stats[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='blue', alpha=0.25)
    ax.plot(angles, stats, color='blue', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    st.pyplot(fig)

# 스트림릿 앱 실행
if __name__ == "__main__":
    st.run()