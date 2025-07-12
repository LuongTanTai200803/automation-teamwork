# Sử dụng Python 3.11
FROM python:3.11-slim

# Tạo thư mục app
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Cài đặt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source vào image
COPY . .

# Gunicorn sẽ chạy Flask app
CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgi:app"]
