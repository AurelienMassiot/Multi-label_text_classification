FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install .
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["demo_multilabel_classification/ui/streamlit_prediction.py"]