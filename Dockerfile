FROM python:3
ADD test.py /
RUN pip install schedule
RUN pip install requests
RUN pip install time
RUN pip install matplotlib
RUN pip install numpy
RUN pip install jdatetime
CMD ["python", "./test.py"]
