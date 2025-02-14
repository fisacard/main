import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

# Elasticsearch 클라이언트 설정
es = Elasticsearch([{'host': 'es1', 'port': 9200, 'scheme': 'http'}])

# Elasticsearch에서 가져올 인덱스 이름 설정
index_name = 'your_index_name'  # 여기에는 Kibana에서 생성한 인덱스 이름을 넣어야 합니다.

# Elasticsearch에서 데이터 가져오는 함수
def get_data_from_elasticsearch(index_name):
    try:
        # Elasticsearch에서 데이터를 검색합니다.
        response = es.search(
            index=index_name,
            body={
                "query": {
                    "match_all": {}  # 모든 데이터를 가져오도록 설정
                },
                "_source": True,  # 모든 필드를 가져옵니다.
                "size": 10000  # 최대 10,000개의 문서 가져오기 (필요한 만큼 조절)
            }
        )

        # Elasticsearch에서 가져온 데이터를 DataFrame으로 변환
        hits = response['hits']['hits']
        df = pd.json_normalize([hit['_source'] for hit in hits])
        return df

    except NotFoundError as e:
        print(f"Elasticsearch에 연결할 수 없습니다: {e}")
        return pd.DataFrame()  # 빈 DataFrame 반환
    except Exception as e:
        print(f"데이터 가져오기 중 오류 발생: {e}")
        return pd.DataFrame()  # 빈 DataFrame 반환

# 데이터 가져오기
df = get_data_from_elasticsearch(index_name)

# 가져온 데이터 출력 (Streamlit에서 사용할 수 있도록)
if not df.empty:
    print(f"데이터 {len(df)}개를 성공적으로 가져왔습니다.")
    print(df.head())
else:
    print("데이터를 가져오는 데 실패했습니다.")
