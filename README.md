# AzureStreamAnalyticsStock

Monitora o preço das ações da Amazon em tempo real usando um script Python e o Azure Event Hubs.
O Event Hubs é usado como entrada do Stream Analytics. As saídas podem ser usadas como: alertas e ações(Event Hubs, Service Bus, Azure functions); dashboards dinâmicos (Power BI do Azure - Power BI desktop não suportado); data warehousing (Synapse Analytics) e armazenamento, como no caso, para o Data Lake. 
<br />Dados extraídos em streaming da NASDAQ: AMZN<br />

## Arquitetura geral do Azure Stream Analytics
<p align="center">
<img src="https://github.com/LeandroRFausto/AzureStreamAnalyticsStock/blob/main/stock_Amazon/image/arquitetura.png"/>
</p>

### Recursos utilizados:
* Visual Studio para a construção do script Python.
* Data Lake Gen2 para armazenar os dados de streaming.
* Event hubs que recebe os dados do script via biblioteca Python.
* Stream Analytics que recebe os dados em tempo real e no caso, envia para o armazenamento. 

### Preparo preliminar do ambiente
* Criar uma conta Azure, uma subscription e um resource group usado como um contêiner do projeto.
* Criar um namespace do Event Hubs.
* Criar um Stream Analytics job

### Construção do script
Cria um programa em Python que recebe dados em streaming das ações da Amazon e o ingere no Event Hub.

Programa no link abaixo:

https://github.com/LeandroRFausto/AzureStreamAnalyticsStock/blob/main/stock_Amazon/code/PythonSendToAzure.py

## Configurações
### Event Hubs
Após a criação é necessário ir ao recurso, navegar até "shared access policies", adicionar nova política e copiar o "Connection string primary key" para incluir no script Python. 
<p align="center">
<img src="https://github.com/LeandroRFausto/AzureStreamAnalyticsStock/blob/main/stock_Amazon/image/eventhub.png"/>
</p>

### Stream Analytics
Informar a subscrição e o Event Hub namespace criado. Ao salvar é necessário configurar a entrada (Event Hub criado) e a saída, que no caso é um Data Lake. É necessário informar o storage account a ser utilizado. 

Em Query, é possível fazer consultas simples e verificar os eventos sendo recepcionados.
<p align="center">
<img src="https://github.com/LeandroRFausto/AzureStreamAnalyticsStock/blob/main/stock_Amazon/image/tabela_consulta.png"/>
</p> 

Com as devidas configurações feitas, basta iniciar o Stream Analytics.
<p align="center">
<img src="https://github.com/LeandroRFausto/AzureStreamAnalyticsStock/blob/main/stock_Amazon/image/streamAnalytics.png"/>
</p> 

O recurso enviará o streaming para o armazenamento. Não é possível, até o momento, enviar as saídas em tempo real para monitoramento no Power BI Desktop.
<p align="center">
<img src="https://github.com/LeandroRFausto/AzureStreamAnalyticsStock/blob/main/stock_Amazon/image/armazenamento.png"/>
</p> 
