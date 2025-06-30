FROM Python 3.12.1

RUN pip install -r requirements.txt

RUN python app_core.py

