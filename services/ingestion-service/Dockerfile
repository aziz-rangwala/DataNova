FROM python:3.9-slim
WORKDIR /app
COPY mock_data_generator.py .
RUN pip install kafka-python faker
CMD ["python", "mock_data_generator.py"]