# Conda 베이스 이미지 사용
FROM continuumio/miniconda3:latest

# 작업 디렉토리 설정
WORKDIR /home/jovyan

# Conda 환경 생성 (필요한 라이브러리만 설치)
RUN conda create -n data_dashboard python=3.9 && \
    conda clean --all -f -y  # Conda 환경 정리

# Conda 초기화
RUN conda init bash

# 필요한 패키지 설치 (Jupyter, Streamlit, pandas 등)
RUN conda install -n data_dashboard -c conda-forge jupyter pandas numpy matplotlib streamlit=1.20.0 && \
    conda clean --all -f -y

# Elasticsearch 라이브러리 설치 (pip)
RUN bash -c "source /opt/conda/etc/profile.d/conda.sh && conda activate data_dashboard && pip install elasticsearch"

# 작업 디렉토리 설정
WORKDIR /home/jovyan/streamlit

# Jupyter와 Streamlit 포트 설정
EXPOSE 8888 8501

# 호스트의 app.py 파일을 컨테이너로 복사
COPY ./streamlit/app.py /home/jovyan/streamlit/app.py

# Conda 환경을 활성화하고 Jupyter와 Streamlit 실행
CMD ["bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate data_dashboard && jupyter notebook --NotebookApp.token='' --NotebookApp.password='' --ip=0.0.0.0 --port=8888 --allow-root & conda run -n data_dashboard streamlit run /home/jovyan/streamlit/app.py --server.address=0.0.0.0"]
