FROM jupyter/scipy-notebook
VOLUME [ "c:\\jupyter\\work", "/home/jovyan/work" ]
EXPOSE 8888
COPY requirements.txt /
RUN pip install -r /requirements.txt