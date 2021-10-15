FROM python:3.6
USER root
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN apt-get update && apt-get -y install locales
RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG pt_BR.UTF-8  
ENV LANGUAGE pt_BR:pt  
ENV LC_ALL pt_BR.UTF-8
ENV MODE dev
ENV TOKEN -
RUN pip install -r requirements.txt
RUN python ./popula_banco.py
CMD python ./docevendas_bot.py