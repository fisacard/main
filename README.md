# FISA CARD



## ⚒️ Tools
- **프로그래밍 언어 및 라이브러리**
  
![Python](https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)
![Kibana](https://img.shields.io/badge/Kibana-005571?style=for-the-badge&logo=Kibana&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B.svg?&style=for-the-badge&logo=streamlit&logoColor=white)

 
- **CICD**

 ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)



- **버전 관리 및 협업 도구**
  
 ![GitHub](https://img.shields.io/badge/github-181717.svg?&style=for-the-badge&logo=github&logoColor=white) 
 ![Slack](https://img.shields.io/badge/slack-4A154B.svg?&style=for-the-badge&logo=slack&logoColor=white)


 # 💳 소비 트렌드 분석 및 맞춤형 추천 시스템

이 프로젝트는 사용자 데이터를 기반으로 소비 패턴을 분석하고, 이를 바탕으로 맞춤형 추천을 제공하는 시스템입니다. 
<br>소비 데이터는 카드 사용 내역을 포함하고 있으며, 사용자의 연령대, 성별, 라이프스타일에 맞춘 분석을 통해 유용한 인사이트를 제공합니다.

## 🚀 기능

1. **사용자 정보 기반 필터링**  
   사용자가 제공한 연령대, 성별, 라이프스타일에 맞춰 거래 데이터를 필터링합니다.

2. **소비 패턴 분석**  
   필터링된 데이터를 바탕으로 주요 소비 패턴을 분석하고, 이를 시각적으로 출력합니다.

3. **카테고리별 소비 금액 분석**  
   특정 카테고리에서 발생한 소비 금액을 분석하여, 각 카테고리의 소비 동향을 파악합니다.

## 🛠️ 설치 및 실행 방법

### 1. Docker Compose 설치

이 프로젝트는 Docker Compose를 이용하여 쉽게 실행할 수 있습니다. 
Docker와 Docker Compose가 설치된 환경에서 실행할 수 있습니다.

## 2. 필요 파일 설정

프로젝트 디렉토리 내에 `output_test.csv`라는 카드 사용 내역 파일이 필요합니다. 

## 3. Anaconda 환경에서 실행

`anaconda` 서비스는 JupyterLab 환경에서 실행되며, 데이터를 분석하고 시각화하는데 사용됩니다.
<br>웹 브라우저에서 [http://localhost:8888](http://localhost:8888)로 접근할 수 있습니다. 

## 4. Kibana 대시보드

Elasticsearch와 Kibana는 데이터 분석 및 시각화를 위한 도구로, 웹 브라우저에서 [http://localhost:5601](http://localhost:5601)로 Kibana 대시보드에 접근할 수 있습니다.

## 🔧 주요 구성

- **Elasticsearch**: 데이터 저장 및 검색을 위한 분산 검색 엔진
- **Kibana**: Elasticsearch 데이터를 시각화하는 대시보드 툴
- **Anaconda**: JupyterLab 환경에서 데이터 분석 및 시각화를 위한 Python 환경

## 📈 사용 방법

### 1. 사용자 정보 입력

Streamlit UI를 통해 사용자 정보를 입력합니다. (연령대, 성별, 라이프스타일)

- **연령대**: 20대, 30대, 40대 등
- **성별**: 남성, 여성
- **라이프스타일**: 대학생, 직장인, 신혼 등

### 2. 분석 실행

사용자가 선택한 정보에 따라 거래 데이터를 필터링하고, 해당 조건에 맞는 소비 패턴을 분석합니다.

### 3. 결과 확인

소비 패턴 분석 결과는 다양한 인사이트로 제공됩니다.

- 연령대별 주요 소비 카테고리
- 성별 소비 차이
- 라이프스타일에 따른 소비 분석


## 📚 분석 및 시각화


- **Kibana**에서 Elasticsearch 데이터를 시각화하여, 소비 패턴을 더욱 직관적으로 이해할 수 있습니다.
- **Streamlit**을 사용하여 인터랙티브한 웹 대시보드를 제공합니다.


