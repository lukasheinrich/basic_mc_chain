FROM lukasheinrich/madgraph-pythia-delphes
RUN yum install -y nano
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python
RUN pip install click pyyaml
COPY . /analysis
WORKDIR /analysis
RUN cd pylhe && pip install -e .
RUN mv nyuneu_UFO /code/madgraph-1.5.10/models
