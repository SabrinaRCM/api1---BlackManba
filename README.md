<div align="center">
    <img src="./resources/logo.jpg" width="320" />
    <div height="2"></div>
</div>


# 💥 WEBBOT  BLACK MAMBA💥

## Descrição: escreva uma descrição detalhada do projeto sob o seu ponto de vista.
O Bot Black Mamba tem como diretriz apontar um bom momento para comprar ou vender uma ação.
Para isso o bot irá capturar os dados em tempo real do valor de uma ação e comparar com os históricos de variações dessa mesma ação em outros períodos em conjunto com uma mapeamento das notícias que podem influenciar o valor da ação.

Queremos auxiliar pessoas com vontade de iniciar sua vida como Traders casuais porém não possuem o tempo necessário para aprender sobre investimentos, o nosso Bot auxilia os usuários a entrarem nesse universo com mais segurança e com certo amparo.


## Tecnologias: não cite apenas as tecnologias, mas descreva o contexto em que foram utilizadas, por que foram escolhidas e pontos fortes de adequação com o projeto e etc.

* Python 3.7 - Linguagem principal;
* Zen of Python - boas práticas para o Projeto;
* PyCharm e/ou Visual Studio Code - IDE's;
* Power Bi - Interface da aplicação;
* MySQL - Banco de Dados;
* Conceitos do SCRUM - Norteador do Projeto.
* Principais Bibliotecas Python:  
    **PyMySQL** - interação com nosso Banco de Dados;  
    **Selenium** - navegação pela Web através do WebDriver do Google Chrome;  
    **Beautiful Soup** - interação com o html dos sites para permitir as raspagens de dados;  
    **Pandas / Matplotlib** - ferramentas para gerar e plotar graficos;  
    **Email / Telegram-bot** - envio de alertas e notificações;
    
 ##  - Contribuições individuais: esta parte é central! Descreva suas contribuições individuais de forma aprofundada, colocando trechos de código que você fez numerando as linhas e comentando estas linhas, coloque diagramas por exemplo de arquitetura que você fez explicando decisões arquiteturais (por que foi feito desta forma?), e etc... (as possibilidades são grandes, além das coisas já citadas você podem pensar em outras como, por exemplo, citar tecnologias que foram empregadas e não ficaram boas, explicar por que não deu certo, como você pensou na solução e etc - se você pensar em solução de problemas encontrará muitos tópicos que teve problemas e conseguiu resolver e poderá aprofundar esta escrita o máximo possível).
 
 
 ##  - Aprendizados efetivos: essa parte também é central Enfatizar aqueles aprendizados que você sabe fazer com autonomia! Mostrar como esses aprendizados foram aplicados no API e, agora que você domina isso, como você poderá aplicar futuramente em seus próximos projetos como seus próximos projetos profissionais. Mostrar que estes aprendizados podem ser aplicados em novos projetos (até porque você utilizará estes portfólios para conseguir novos empregos de acordo com suas metas profissionais).

## **O que o usuário pode fazer ?** 🔑

* Criar uma conta via Telegram (normal ou usuário “Gold");
* Consultar gráfico em tempo real;
* Consultar gráfico do histórico das ações;

## **Getting Ready for Action** 🚂
### **Pré Requisitos**
* Possuir o Python instalado na máquina;
* Possuir o PIP instalado e atualizado;
* Possuir o GIT instalado;
* Ter alguma IDE compatível com Python instalada;

**1)** Baixar nosso projeto na máquina através do comando:  
> git clone https://gitlab.com/lucasdlg5/webbot_blackmamba

**2)** Abrir o projeto atráves da IDE desejada. 

**3)** Selecionar o Interpretador Python na versâo 3.7.4.

**4)** Instalar as bibliotecas que utilizaremos através do comando:
> pip install -r req.txt


## **How does it actually Works ?** 👷

**1)** Através de uma raspagem o bot obteve o histórico do periodo de 1 ano (histórico diário desde 09-2018) com os valores da ação do Banco Inter para efeito comparativo do usuário;  

**2)** Em tempo real a aplicação faz raspagem do valor da Ação do Banco Inter pelo site https://br.tradingview.com e armazena os dados em um banco de dados MySQL (cloud);  

**3)** Além dos valores da ação a aplicação coleta notícias sobre o Banco Inter no Twitter, à fim de manter o usuário atualizado;  

**4)** A aplicação monitora os valores e através de uma regra de négocio simplificada sugere ao usuário à comprar / vender ação.  
