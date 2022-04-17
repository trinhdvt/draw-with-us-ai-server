FROM pytorch/torchserve:0.5.3-cpu

USER root
RUN chmod 777 -R .

COPY src/deployment/model_store/drawclassifier.mar model-store/

COPY src/deployment/config.properties config.properties

CMD ["torchserve", "--start" , "--model-store", "model-store" , "--models" , "drawclassifier.mar", "--foreground"]
