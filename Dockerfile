FROM greycilik/cilikuserbot:buster

RUN git clone -b donubot https://github.com/Beller321/donubot /home/donubot/ \
    && chmod 777 /home/donubot \
    && mkdir /home/donubot/bin/

COPY ./sample_config.env ./config.env* /home/cilikuserbot/

WORKDIR /home/donubot/

CMD ["python3", "-m", "userbot"]
