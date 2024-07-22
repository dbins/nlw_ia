# NEXT LEVEL WEEK - Rocketseat
## Inteligência artificial

Neste repositório se encontra o código mostrado em aula. Neste evento foi feito uma API utilizando Python, Langchain e ChatGPT.

Foi mostrado o deploy na Amazon AWS

### Docker

Para enviar a aplicação para a hospedagem AWS é necessário primeiro criar um container Docker. Para criar uma imagem é necessário executar o seguinte comando:

```
docker build --platform linux/x86_64 -t travelagent .
```

Os testes foram feitos no Windows 10, foi necessário primeiro instalar o Docker Desktop e abrir ele antes de executar o comando. A imagem recem criada vai ficar disponível no Docker Desktop.


### Hospedagem AWS

Primeiro é necessário criar uma conta na Amazon AWS, o endereço é:

**aws.amazon.com**

Deve ser escolhido no menu "Pricing" a opção "free tier". Apesar de existir uma opção grátis, é necessário informar os dados do cartão de crédito.

Uma vez logado na AWS, devem ser seguidos os seguintes passos:

Primeiro serviço a utilizar é o Elastic Container (ECR)
- Criar repositório
- Depois usar o AWS Command Line Interface
- Comandos para testar:
- which aws
- aws --version
- aws configure

Para configurar. precisa ir primeiro no IAM console.
- ir em users
- entrar no seu usuário
- security credentials - access key
- create access key for use case CLI

Informar no configure o access key e o secret criados no IAM
- A region do configure é a us-east-2
- Deixar vazio o Default output format 

Dentro do repositório do ECR, clicar em Push Commnds.

Atenção para os comandos docker tag e docker push!

A integração do container Docker com o AWS será feita através de uma Lambda Function.

Ir no Lambda e criar uma função nova

Atribuir um nome de função e vincular a um container...
Escolher a imagem que foi enviada ao ECR
As variaveis de ambiente devem ser atribuidas dentro da Lambda Function (Environment Variables)
Não esquecer de Aumentar memória e timeout

criar teste: (test event)
A função espera receber um parâmetro question

```
{
	"question": "pergunta a ser feita"
}
```

Para usar fora do ambiente da AWS, é necessário configurar um ALB (Application Load Balance)

- Dentro do serviço EC2, selecionar Load Balancers 
- Marcar ipv4
- Criar um Application Load Balance
- Manter o VPC selecionado e marcar todos os subnets
- secutiry group default
- usar protocolo http: 
- criar target group:
- Selecionar como target group p lambda function
- Depois de criar o load balance ir na aba de segurança (security)
- editar inbound rules

Na pagina inicial, na aba DNS, tem o endereço externo para consumir a API
