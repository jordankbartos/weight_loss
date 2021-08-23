FROM jupyter/base-notebook:python-3.9.6

USER root
RUN apt-get update \
    && apt-get --assume-yes install dialog \
    vim \
    git \
    python3-pip

# VIM keybindings
USER 1000 
RUN mkdir -p $(jupyter --data-dir)/nbextensions \
    && cd $(jupyter --data-dir)/nbextensions \ 
    && git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding \
    && jupyter nbextension enable vim_binding/vim_binding \
    && mkdir dev

COPY requirements.txt requirements.txt
#ENV PATH="${PATH}:/home/appuser/.local/bin"
RUN pip3 install -r requirements.txt

RUN pip3 install -r requirements.txt

RUN git clone https://github.com/jordankbartos/my_config.git \
    && cd my_config \
    && sh configure.sh \
    && cd .. \
    && rm -rf my_config

