FROM python:3

WORKDIR /Users/samihaal-bakri/PycharmProjects/DataS/visualization.py

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./visualization.py" ]