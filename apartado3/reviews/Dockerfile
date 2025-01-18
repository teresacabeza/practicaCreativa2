# Dockerfile para Reviews
FROM websphere-liberty:20.0.0.6-full-java8-ibmjava

ENV SERVERDIRNAME reviews

COPY ./reviews-wlpcfg/servers/LibertyProjectServer /opt/ibm/wlp/usr/servers/defaultServer/

RUN /opt/ibm/wlp/bin/installUtility install --acceptLicense /opt/ibm/wlp/usr/servers/defaultServer/server.xml && \
    chmod -R g=rwx /opt/ibm/wlp/output/defaultServer/

ARG service_version
ARG enable_ratings
ARG star_color
#version 3 estrellas en rojo
ENV SERVICE_VERSION ${service_version:-v3}  
ENV ENABLE_RATINGS ${enable_ratings:-false}
ENV STAR_COLOR ${star_color:-black}

CMD ["/opt/ibm/wlp/bin/server", "run", "defaultServer"]