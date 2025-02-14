import streamlit as st
import pandas as pd

# 스트림릿 페이지 제목
st.title("💱 카테고리별 소비금액 분석")

# 로컬 경로에서 CSV 파일 읽기 (파일 경로를 직접 지정)
file_path = r'C:/ITStudy/fisacard/main/output_test.csv'   

# CSV 파일 읽기
try:
    df = pd.read_csv(file_path)
    
    # 사이드바에서 카테고리 선택
    category = st.sidebar.selectbox(
        "분석할 카테고리를 선택하세요",
        (
            "가전/가구/주방용품", "보험/병원", "사무통신/서적/학원", "여행/레저/문화", 
            "요식업", "용역/수리/건축자재", "유통", "보건위생", "의류/신변잡화", 
            "자동차/연료/정비", "기타"
        )
    )

    # 각 카테고리에 따른 컬럼 정의
    category_columns = {
        "가전/가구/주방용품": ['INTERIOR_AM', 'APPLNC_AM', 'KITWR_AM'],
        "보험/병원": ['INSU_AM', 'HOS_AM'],
        "사무통신/서적/학원": ['OFFEDU_AM', 'OFFCOM_AM', 'BOOK_AM', 'ACDM_AM'],
        "여행/레저/문화": ['TRVLEC_AM', 'LEISURE_S_AM', 'LEISURE_P_AM', 'CULTURE_AM', 'HOTEL_AM', 'TRVL_AM'],
        "요식업": ['FSBZ_AM', 'HLTHFS_AM', 'GROCERY_AM', 'RESTRNT_AM'],
        "용역/수리/건축자재": ['SVCARC_AM', 'BLDMNG_AM', 'ARCHIT_AM', 'OPTIC_AM', 'RPR_AM', 'SVC_AM'],
        "유통": ['DIST_AM', 'DISTBNP_AM', 'DISTBP_AM'],
        "보건위생": ['PLSANIT_AM'],
        "의류/신변잡화": ['CLOTHGDS_AM', 'CLOTH_AM', 'FABRIC_AM', 'GOODS_AM'],
        "자동차/연료/정비": ['AUTO_AM', 'FUEL_AM', 'AUTOMNT_AM', 'AUTOSL_AM'],
        "기타": ['AGRICTR_AM', 'MBRSHOP_AM']
    }

    # 선택한 카테고리의 데이터 요약
    st.subheader(f"{category} 카테고리 요약")

    # 해당 카테고리 컬럼들로 데이터 선택
    selected_columns = category_columns.get(category, [])
    if selected_columns:
        df_category = df[selected_columns]

        # 총 소비금액 (각 카테고리의 소비금액 합산)
        df_category['total_am'] = df_category.sum(axis=1)

        # 기본 통계량 (최대, 최소, 평균, 표준편차)
        stats = df_category.describe()
        st.write(stats)

        # 각 카테고리별 상세 통계 정보 (한글명 사용)
        for column in selected_columns:
            korean_name = column_translation.get(column, column)  # 컬럼명에 대응하는 한글명 얻기
            st.write(f"💰 {korean_name} 소비금액:")
            st.write(f'''최대값: {df_category[column].max()}, 최소값: {df_category[column].min()}, 평균값: {df_category[column].mean()}, 표준편차: {df_category[column].std()}''')

        st.write(f"💰 총 소비금액:")
        st.write(f'''최대값: {df_category['total_am'].max()}, 최소값: {df_category['total_am'].min()}, 평균값: {df_category['total_am'].mean()}, 표준편차: {df_category['total_am'].std()}''')

except Exception as e:
    st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
