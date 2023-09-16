FROM continuumio/anaconda3

WORKDIR /python

COPY . .

RUN conda env create -f environment.yaml

CMD ["watchmedo", "shell-command", "--patterns=*.py", "--recursive", "--command", "python main.py", "--drop"]
