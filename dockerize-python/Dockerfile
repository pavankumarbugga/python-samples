FROM python:3.6.9

COPY mac-address-interface.py .
RUN pip install requests
ENTRYPOINT ["python", "./mac-address-interface.py"]
#CMD [ "44:38:39:ff:ef:57" ]