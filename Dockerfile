FROM python:3.9-slim
WORKDIR /app

# मैट्रिक्स ओवरराइड: ज़बरदस्ती कंपाइलर हथियारों को इंजेक्ट करना!
RUN apt-get update && \
    apt-get install -y gcc g++ python3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# डार्क सिस्टम को फायर करो!
CMD ["python", "kkk.py"]
