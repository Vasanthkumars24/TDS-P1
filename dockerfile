FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]