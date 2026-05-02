FROM python:3.9-slim

# वर्किंग डायरेक्टरी सेट करना
WORKDIR /app

# सिस्टम की ज़रूरी फाइलें इंस्टॉल करना
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt को कॉपी करना और लाइब्रेरी इंस्टॉल करना
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# बाकी सारा कोड कॉपी करना
COPY . .

# बॉट को स्टार्ट करने वाली कमांड (अब यह main.py को रन करेगा)
CMD ["python", "main.py"]
