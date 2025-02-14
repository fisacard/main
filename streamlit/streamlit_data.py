# import pandas as pd
# import streamlit as st


# # 🔹 거래 데이터 가져오기 함수 (CSV 파일을 사용)
# def fetch_transactions(user_info, file_path="output_test.csv"):
#     try:
#         # CSV 파일 읽기
#         df = pd.read_csv(file_path)

#         # 조건에 맞는 데이터 필터링 (멤버십 조건 제거)
#         filtered_df = df[
#             (df["AGE"] == int(user_info["AGE"]))  # AGE는 숫자이므로 int로 비교
#             & (df["SEX_CD"] == user_info["SEX_CD"])  # SEX_CD는 숫자 비교
#             & (df["LIFE_STAGE"] == user_info["LIFE_STAGE"])
#         ]

#         # 디버깅: 필터링된 데이터 출력
#         st.write(f"Filtered Data (first 5 rows):\n{filtered_df.head()}")

#         # 필요한 컬럼만 추출
#         transactions = filtered_df[["date", "category", "amount", "merchant"]]

#         return transactions
#     except Exception as e:
#         print(f"❌ 오류 발생: {e}")
#         return pd.DataFrame()


# # 🔹 소비 패턴 분석 함수
# def analyze_spending(df, user_info):
#     tips = []
#     if df.empty:
#         return ["해당 조건에 맞는 소비 내역이 없습니다."]

#     total_spent = df["amount"].sum()
#     category_spent = df.groupby("category")["amount"].sum()
#     top_merchants = df["merchant"].value_counts().head(3).index.tolist()

#     # 1️⃣ 연령대별 주요 소비 패턴
#     tips.append(
#         f"{user_info['age_range']} 연령대는 '{category_spent.idxmax()}' 소비가 가장 많아요!"
#     )

#     # 2️⃣ 성별 소비 차이
#     tips.append(
#         f"{user_info['gender']} 고객은 '{category_spent.idxmax()}' 카테고리에 가장 많이 소비해요!"
#     )

#     # 3️⃣ 라이프스타일(life_stage)별 소비 분석
#     if user_info["life_stage"] == "싱글":
#         tips.append("혼자 사는 고객님들은 배달음식 소비가 많아요! 😃")
#     elif user_info["life_stage"] == "기혼":
#         tips.append("기혼 고객님들은 대형마트, 키즈카페 지출이 많아요! 🏡")
#     elif user_info["life_stage"] == "직장인":
#         tips.append("직장인 고객님들은 점심, 커피 지출이 많아요! ☕")

#     return tips


# # 🔹 Streamlit 대시보드
# st.title("💳 소비 트렌드 분석 및 맞춤형 추천 시스템")

# # 사용자 정보 입력
# age_range = st.selectbox("연령대", ["20", "25", "30", "35", "40"])  # AGE 값은 숫자로
# gender = st.radio("성별", ["남성", "여성"])
# life_stage = st.selectbox(
#     "라이프스타일",
#     [
#         "UNI",
#         "NEW_JOB",
#         "NEW_WED",
#         "CHILD_BABY",
#         "CHILD_TEEN",
#         "CHILD_UNI",
#         "GOLLIFE",
#         "SECLIFE",
#         "RETIR",
#     ],
# )

# # 성별 코드를 1(남성)과 2(여성)로 변환
# gender_code = 1 if gender == "남성" else 2

# user_info = {
#     "age_range": age_range,
#     "gender": gender,
#     "gender_code": gender_code,  # 성별 코드 추가
#     "life_stage": life_stage,
# }

# # 데이터 가져오기 & 분석
# if st.button("🔍 소비 패턴 분석 시작"):
#     df = fetch_transactions(user_info)
#     insights = analyze_spending(df, user_info)

#     st.subheader("📊 소비 트렌드 분석 결과")
#     for insight in insights:
#         st.write(f"- {insight}")

# # 잘 출력됐음
# import pandas as pd
# import streamlit as st


# def fetch_transactions(user_info, file_path="output_test.csv"):
#     try:
#         # CSV 파일 읽기
#         df = pd.read_csv(file_path)

#         # 1. AGE 필터링 (정수형으로 변환 후 비교)
#         filtered_df = df[df["AGE"] == int(user_info["AGE"])]
#         st.write(f"Filtered by AGE:\n{filtered_df.head()}")

#         # 2. SEX_CD 필터링
#         filtered_df = filtered_df[filtered_df["SEX_CD"] == user_info["SEX_CD"]]
#         st.write(f"Filtered by SEX_CD:\n{filtered_df.head()}")

#         # 3. LIFE_STAGE 필터링
#         filtered_df = filtered_df[filtered_df["LIFE_STAGE"] == user_info["LIFE_STAGE"]]
#         st.write(f"Filtered by LIFE_STAGE:\n{filtered_df.head()}")

#         return filtered_df[
#             [
#                 "YEAR",
#                 "QUARTER",
#                 "SEQ_int",
#                 "AGE",
#                 "SEX_CD",
#                 "LIFE_STAGE",
#                 "TOT_USE_AM",
#                 "CRDSL_USE_AM",
#             ]
#         ]

#     except Exception as e:
#         st.error(f"❌ 오류 발생: {e}")
#         return pd.DataFrame()


# # 테스트 사용자 정보
# user_info = {
#     "AGE": "25",  # 예시 나이
#     "SEX_CD": 2,  # 예시 성별 (2: Female)
#     "LIFE_STAGE": "NEW_JOB",  # 예시 라이프스타일
# }

# # 트랜잭션 데이터 가져오기
# transactions = fetch_transactions(user_info)


import streamlit as st
import pandas as pd


# 데이터 불러오기 (예시로 CSV 파일을 사용)
file_path = r"C:/ITStudy/06_ELK/elk-fisa04/02_streamlit_elk/streamlit-search/output_test.csv"  # 경로를 본인 파일에 맞게 수정
# CSV 파일 읽기
df = pd.read_csv(file_path)

# Streamlit UI
st.title("Card Consumption Analysis")

# 사용자 입력 받기
AGE = st.selectbox(
    "AGE",
    [
        "20",
        "25",
        "30",
        "35",
        "40",
        "45",
        "50",
        "55",
        "60",
        "65",
        "70",
        "75",
        "80",
        "85",
    ],
)
SEX_CD = st.selectbox("SEX_CD", ["Male", "Female"])
LIFE_STAGE = st.selectbox(
    "LIFE_STAGE",
    [
        "UNI",
        "NEW_JOB",
        "NEW_WED",
        "CHILD_BABY",
        "CHILD_TEEN",
        "CHILD_UNI",
        "GOLLIFE",
        "SECLIFE",
        "RETIR",
    ],
)

# 필터링된 데이터를 표시
if AGE:
    # AGE 값으로 필터링 (AGE는 숫자 값으로 비교)
    if AGE == "20":
        df = df[df["AGE"] >= 20 & (df["AGE"] <= 24)]
    elif AGE == "25":
        df = df[df["AGE"] >= 25 & (df["AGE"] <= 29)]
    elif AGE == "30":
        df = df[df["AGE"] >= 30 & (df["AGE"] <= 34)]
    elif AGE == "35":
        df = df[df["AGE"] >= 35 & (df["AGE"] <= 39)]
    elif AGE == "40":
        df = df[df["AGE"] >= 40 & (df["AGE"] <= 44)]
    elif AGE == "45":
        df = df[df["AGE"] >= 45 & (df["AGE"] <= 49)]
    elif AGE == "50":
        df = df[df["AGE"] >= 50 & (df["AGE"] <= 54)]
    elif AGE == "55":
        df = df[df["AGE"] >= 55 & (df["AGE"] <= 59)]
    elif AGE == "60":
        df = df[df["AGE"] >= 60 & (df["AGE"] <= 64)]
    elif AGE == "65":
        df = df[df["AGE"] >= 65 & (df["AGE"] <= 69)]
    elif AGE == "70":
        df = df[df["AGE"] >= 70 & (df["AGE"] <= 74)]
    elif AGE == "75":
        df = df[df["AGE"] >= 75 & (df["AGE"] <= 79)]
    elif AGE == "80":
        df = df[df["AGE"] >= 80 & (df["AGE"] <= 84)]
    elif AGE == "85":
        df = df[df["AGE"] >= 85 & (df["AGE"] <= 89)]

    # SEX 필터링
    if SEX_CD == "Male":
        df = df[df["SEX_CD"] == 1]
    else:
        df = df[df["SEX_CD"] == 2]

    # LIFE_STAGE 필터링
    life_stage_mapping = {
        "UNI": "University",
        "NEW_JOB": "New Job",
        "NEW_WED": "Newly Married",
        "CHILD_BABY": "Child (Baby)",
        "CHILD_TEEN": "Child (Teen)",
        "CHILD_UNI": "Child (University)",
        "GOLLIFE": "Golden Life",
        "SECLIFE": "Second Life",
        "RETIR": "Retirement",
    }

    # life_stage_selected 값을 영어로 매핑
    # 필터링
    df_filtered = df[df["LIFE_STAGE"] == LIFE_STAGE]

    # # 결과 출력
    # st.write(df)
    # st.write(df["LIFE_STAGE"].unique())
    # st.write(f"Selected Life Stage: {LIFE_STAGE}")
    # st.write(df_filtered)

    # 🔹 소비 패턴 분석 함수
    def analyze_spending(df, user_info):
        tips = []
        # # if df.empty:
        # #     return ["해당 조건에 맞는 소비 내역이 없습니다."]

        # # 전체 소비 금액을 계산 (TOT_USE_AM 컬럼 사용)
        # total_spent = df["TOT_USE_AM"].sum()

        # # 1️⃣ 연령대별 주요 소비 패턴
        # category_spent = df.groupby("AGE")["TOT_USE_AM"].sum()
        # tips.append(
        #     f"{user_info['AGE']} 연령대는 '{category_spent.idxmax()}' 소비가 가장 많아요!"
        # )
        # 해당 연령대 데이터를 필터링
        # 사용자 입력 연령대 (예: 20)

        # 해당 연령대 데이터를 필터링
        age_filtered_df = df[df["AGE"] == AGE]

        # 소비 카테고리 목록 (INTERIOR_AM, INSUHOS_AM, 등)
        categories = [
            "INTERIOR_AM",
            "INSUHOS_AM",
            "OFFEDU_AM",
            "TRVLEC_AM",
            "FSBZ_AM",
            "SVCARC_AM",
            "DIST_AM",
            "PLSANIT_AM",
            "CLOTHGDS_AM",
            "AUTO_AM",
            "FUNITR_AM",
            "APPLNC_AM",
            "HLTHFS_AM",
            "BLDMNG_AM",
            "ARCHIT_AM",
            "OPTIC_AM",
            "AGRICTR_AM",
            "LEISURE_S_AM",
            "LEISURE_P_AM",
            "CULTURE_AM",
            "SANIT_AM",
            "INSU_AM",
            "OFFCOM_AM",
            "BOOK_AM",
            "RPR_AM",
            "HOTEL_AM",
            "GOODS_AM",
            "TRVL_AM",
            "FUEL_AM",
            "SVC_AM",
            "DISTBNP_AM",
            "DISTBP_AM",
            "GROCERY_AM",
            "HOS_AM",
            "CLOTH_AM",
            "RESTRNT_AM",
            "AUTOMNT_AM",
            "AUTOSL_AM",
            "KITWR_AM",
            "FABRIC_AM",
            "ACDM_AM",
            "MBRSHOP_AM",
        ]

        # 카테고리 한글 이름 매핑
        category_name_mapping = {
            "INTERIOR_AM": "가전/가구/주방용품",
            "INSUHOS_AM": "보험/병원",
            "OFFEDU_AM": "사무통신/서적/학원",
            "TRVLEC_AM": "여행/레져/문화",
            "FSBZ_AM": "요식업",
            "SVCARC_AM": "용역/수리/건축자재",
            "DIST_AM": "유통",
            "PLSANIT_AM": "보건위생",
            "CLOTHGDS_AM": "의류/신변잡화",
            "AUTO_AM": "자동차/연료/정비",
            "FUNITR_AM": "가구",
            "APPLNC_AM": "가전제품",
            "HLTHFS_AM": "건강식품",
            "BLDMNG_AM": "건물및시설관리",
            "ARCHIT_AM": "건축/자재",
            "OPTIC_AM": "광학제품",
            "AGRICTR_AM": "농업",
            "LEISURE_S_AM": "레져업소",
            "LEISURE_P_AM": "레져용품",
            "CULTURE_AM": "문화/취미",
            "SANIT_AM": "보건/위생",
            "INSU_AM": "보험",
            "OFFCOM_AM": "사무/통신기기",
            "BOOK_AM": "서적/문구",
            "RPR_AM": "수리서비스",
            "HOTEL_AM": "숙박업",
            "GOODS_AM": "신변잡화",
            "TRVL_AM": "여행업",
            "FUEL_AM": "연료판매",
            "SVC_AM": "용역서비스",
            "DISTBNP_AM": "유통업비영리",
            "DISTBP_AM": "유통업영리",
            "GROCERY_AM": "음식료품",
            "HOS_AM": "의료기관",
            "CLOTH_AM": "의류",
            "RESTRNT_AM": "일반/휴게음식",
            "AUTOMNT_AM": "자동차정비/유지",
            "AUTOSL_AM": "자동차판매",
            "KITWR_AM": "주방용품",
            "FABRIC_AM": "직물",
            "ACDM_AM": "학원",
        }

        # 각 카테고리에서 해당 연령대의 소비 금액을 합산
        category_spent = age_filtered_df[categories].sum()

        # 가장 많이 소비된 카테고리 찾기
        most_spent_category = category_spent.idxmax()
        most_spent_amount = category_spent.max()

        # 한글 카테고리 이름으로 변환
        most_spent_category_korean = category_name_mapping[most_spent_category]

        # 결과 출력
        tips.append(
            f"{AGE}~{int(AGE)+4} 연령대는 '{most_spent_category_korean}' 카테고리에서 가장 많은 소비를 했어요!"
        )

        #     # 2️⃣ 성별 소비 차이
        #     tips.append(
        #         f"{user_info['SEX_CD']} 고객은 '{category_spent.idxmax()}' 카테고리에 가장 많이 소비해요!"
        #     )

        #     # 3️⃣ 라이프스타일(life_stage)별 소비 분석
        #     if user_info["LIFE_STAGE"] == "University":
        #         tips.append("대학생 고객님들은 외식 및 카페 지출이 많아요! ☕")
        #     elif user_info["LIFE_STAGE"] == "New Job":
        #         tips.append("새로운 직장에 다니는 고객님들은 점심, 커피 지출이 많아요! 🍽️")
        #     elif user_info["LIFE_STAGE"] == "Newly Married":
        #         tips.append("신혼 고객님들은 가전제품 및 가구에 많은 지출을 해요! 🏠")

        return tips


# def analyze_spending(df, user_info):
#     tips = []

#     # 전체 소비 금액을 계산 (TOT_USE_AM 컬럼 사용)
#     total_spent = df["TOT_USE_AM"].sum()

#     # # 1️⃣ 연령대별 주요 소비 패턴
#     # # 필터링된 데이터에서 연령대별 총 소비 계산
#     # category_spent = df.groupby("AGE")["TOT_USE_AM"].sum()

#     # # 최대 소비 연령대 확인
#     # most_spent_age = category_spent.idxmax()  # 가장 많은 소비가 발생한 연령대
#     # tips.append(
#     #     f"{user_info['AGE']} 연령대는 '{most_spent_age}' 연령대에서 소비가 가장 많아요!"
#     # )

#     # # 2️⃣ 성별 소비 차이
#     # sex_spent = df.groupby("SEX_CD")["TOT_USE_AM"].sum()
#     # sex_most_spent = sex_spent.idxmax()  # 성별에서 가장 많은 소비가 발생한 성별
#     # tips.append(
#     #     f"{user_info['SEX_CD']} 고객은 '{sex_most_spent}' 성별에서 가장 많이 소비해요!"
#     # )

#     # 3️⃣ 라이프스타일별 소비 분석
#     # life_stage_spent = df.groupby("LIFE_STAGE")["TOT_USE_AM"].sum()
#     # life_stage_spent_max = (
#     #     life_stage_spent.idxmax()
#     )  # 라이프스타일별 가장 많이 소비한 라이프스타일
#     # tips.append(
#     #     f"{user_info['LIFE_STAGE']} 라이프스타일은 '{life_stage_spent_max}' 라이프스타일에서 가장 많은 소비를 보여요!"
#     # )

#     # # 라이프스타일 기반 추가 소비 패턴
#     # if user_info["LIFE_STAGE"] == "University":
#     #     tips.append("대학생 고객님들은 외식 및 카페 지출이 많아요! ☕")
#     # elif user_info["LIFE_STAGE"] == "New Job":
#     #     tips.append("새로운 직장에 다니는 고객님들은 점심, 커피 지출이 많아요! 🍽️")
#     # elif user_info["LIFE_STAGE"] == "Newly Married":
#     #     tips.append("신혼 고객님들은 가전제품 및 가구에 많은 지출을 해요! 🏠")

#     return tips


# 사용자 정보
user_info = {
    "AGE": AGE,
    "SEX_CD": SEX_CD,
    "LIFE_STAGE": life_stage_mapping.get(LIFE_STAGE, LIFE_STAGE),
}

# 소비 패턴 분석 실행
if st.button("🔍 소비 패턴 분석 시작"):
    insights = analyze_spending(df_filtered, user_info)

    # 분석 결과 출력
    st.subheader("📊 소비 패턴 분석 결과")
    for insight in insights:
        st.write(f"- {insight}")
