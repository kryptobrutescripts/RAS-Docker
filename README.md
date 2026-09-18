# RAS-Docker

Projeto desenvolvido para o trabalho de Redes e Administração de Sistemas (RASI).

## Aluno

Bruno Henrryke Marcelino de Souza

## GitHub

https://github.com/kryptobrutescripts/RAS-Docker

## Tecnologias

- Python
- Flask
- Docker
- Kali Linux

## Estrutura

```text
flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Executar com Docker

Na pasta do projeto:

```bash
docker build -t flask-app .
```

Depois:

```bash
docker run -d --name flask-app -p 5000:5000 flask-app
```

Verificar o container:

```bash
docker ps
```

Ver os logs:

```bash
docker logs flask-app
```

## Acessar a aplicação

Na própria máquina:

```text
http://127.0.0.1:5000
```

Em outra máquina da rede, use o IP da máquina que está executando o Docker:

```text
http://IP_DA_MAQUINA:5000
```

## Rotas

- `/` — página inicial
- `/sobre` — informações sobre o projeto
- `/contato` — página de contato

Exemplo:

```text
http://IP_DA_MAQUINA:5000/sobre
http://IP_DA_MAQUINA:5000/contato
```

## Parar e remover o container

```bash
docker stop flask-app
docker rm flask-app
```
