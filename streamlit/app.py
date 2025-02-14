import streamlit as st

# 대시보드 URL 목록 (여러 대시보드 URL 추가)
dashboard_urls = {
    "대시보드 1": "http://localhost:5601/app/dashboards#/view/520f9533-191c-47e2-a4c6-326f81045837?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now))",
    "대시보드 2": "http://localhost:5601/app/dashboards#/view/another_dashboard_id?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now))",
    "대시보드 3": "http://localhost:5601/app/dashboards#/view/yet_another_dashboard_id?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-15m,to:now))"
}

# Streamlit 사이드바에서 대시보드 선택하기
selected_dashboard = st.sidebar.selectbox("대시보드 선택", list(dashboard_urls.keys()))

# 선택된 대시보드의 URL 가져오기
kibana_dashboard_url = dashboard_urls[selected_dashboard]

# 선택한 대시보드를 iframe으로 띄우기
iframe_code = f'<iframe src="{kibana_dashboard_url}" width="100%" height="800" frameborder="0"></iframe>'

# Streamlit 화면에 iframe 표시
st.markdown(iframe_code, unsafe_allow_html=True)
