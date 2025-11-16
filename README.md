# Guia de Uso

## Requisitos:

- Conta AWS 
- Usuário AWS com permissões necessárias:
  - `AmazonS3FullAccess`
  - `IAMFullAccess` (ou política equivalente para alterar ACL e Bucket Policy)
  - `AmazonEC2FullAccess` (para criar instâncias EC2, grupos de segurança, volumes etc)
  - `AWSLambda_FullAccess` (para criar e executar funções Lambda)
  - `CloudWatchFullAccess` (para configurar eventos e logs)

- **AWS CLI** instalada ([guia de instalação](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html))
- **Terraform** instalado ([guia de instalação](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli))

***Configure as credenciais AWS***

Opção 1 – Usando aws configure:

```bash
aws configure
```
Informe:


```
AWS Access Key ID: SEU_ACCESS_KEY
AWS Secret Access Key: SEU_SECRET_KEY
Default region name: us-east-1
Default output format: json
```
Opção 2 – Usando variáveis de ambiente:
```
export AWS_ACCESS_KEY_ID="SEU_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="SEU_SECRET_KEY"
export AWS_DEFAULT_REGION="us-east-1"
```

---

# Desafio 1

Objetivo: Provisionar um bucket S3 para hospedar uma site estático simples.

### Acesse a pasta do desafio 1
   ```bash
   cd servico01
   ```

Comandos do Terraform

```
terraform init  # inicia o terraform e instala as dependencias
terraform plan # analisa o plano de execução
terraform apply # inicia a bucket 

# Digite yes para confirmar.

# Para evitar custos:

terraform destroy

# Digite yes para confirmar

# Coloque no seu browser a url que apareceu no console
```
### ⚠️ A aplicação só funciona via HTTP, não HTTPS.

---

# Desafio 2

Objetivo: Provisionar uma aplicação em container rodando na cloud AWS.


### Acesse a pasta do desafio 2
   ```bash
   cd servico02
   ```

Comandos do Terraform

```
terraform init  
terraform plan 
terraform apply 

# Digite yes para confirmar.

# Para evitar custos:

terraform destroy

# Digite yes para confirmar

# Coloque no seu browser a url que apareceu no console
```

### ⚠️ A aplicação só funciona via HTTP, não HTTPS.


#  Desafio 3

Objetivo: Configurar uma rotina diária usando Lambda + CloudWatch Events que insere automaticamente um arquivo com timestamp no bucket S3.


### Acesse a pasta do desafio 3
   ```bash
   cd servico03
   ```

Comandos do Terraform

```
terraform init
terraform plan
terraform apply
Digite yes para confirmar.

Para evitar custos
terraform destroy
Digite yes para confirmar
```

---

Made by [Allan Rodrigues](https://github.com/allanrodriguest) 