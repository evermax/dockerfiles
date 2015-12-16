FROM maven:3.3.3-jdk-8
MAINTAINER Maxime Lasserre "maxlasserre@free.fr"

ADD state.xml /tmp/state.xml

RUN wget http://download.netbeans.org/netbeans/8.0.2/final/bundles/netbeans-8.0.2-javase-linux.sh -O /tmp/netbeans.sh -q && \
    chmod +x /tmp/netbeans.sh && \
    echo 'Installing netbeans' && \
    /tmp/netbeans.sh --silent --state /tmp/state.xml && \
    rm -rf /tmp/*

ADD run /usr/local/bin/netbeans

CMD /usr/local/bin/netbeans
