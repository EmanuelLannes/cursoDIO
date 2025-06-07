# Desafio Azure Speech Studio e Language Studio

Este repositório contém as anotações e insights adquiridos durante o laboratório prático de Azure Speech Studio e Language Studio. O objetivo principal deste laboratório é aprofundar o uso dessas ferramentas para análise de fala e linguagem natural, e desenvolver soluções baseadas em inteligência artificial para voz e linguagem.

## 🎯 Objetivo

- **Praticar e aprofundar o uso das ferramentas Azure Speech Studio e Language Studio.**
- **Desenvolver soluções baseadas em IA focadas na análise de fala e linguagem natural.**
- **Criar um repositório de anotações e insights adquiridos, servindo como material de apoio para estudos e futuras implementações.**

## 🛠️ Ferramentas Usadas

- **Azure Speech Studio:** Transformação de áudio em texto (Speech-to-Text), geração de fala (Text-to-Speech), e análise de fala.
- **Azure Language Studio:** Análise de sentimentos, extração de entidades, classificação de texto, e identificação de intenções.

## 📁 Estrutura do Repositório

/notebooks -> Notebooks Jupyter com experimentos práticos
/scripts -> Scripts para automação das APIs
/insights -> Anotações e aprendizados do laboratório
README.md -> Documento explicativo


## 🚀 Passos Seguidos no Laboratório

1. **Configuração do Ambiente**
   - Criação da conta no [Azure](https://azure.microsoft.com/)
   - Criação dos serviços Speech e Language Studio
   - Obtenção das chaves de API

2. **Exploração do Azure Speech Studio**
   - Conversão de áudio para texto (Speech-to-Text)
   - Análise de características da fala
   - Geração de áudio a partir de texto (Text-to-Speech)

3. **Exploração do Azure Language Studio**
   - Análise de Sentimentos
   - Extração de Entidades Nomeadas
   - Classificação de Texto
   - Análise de Intenções

4. **Desenvolvimento de Soluções**
   - Chatbots de voz
   - Análise automatizada de feedbacks
   - Integração com front-ends simples (React/HTML)

5. **Documentação**
   - Registro completo dos testes, códigos e descobertas

## 💡 Insights Adquiridos

- **Precisão do Speech-to-Text:** A qualidade do áudio e o sotaque influenciam a acurácia. Modelos customizados melhoram resultados.
- **Análise de Sentimentos:** Efetiva para feedbacks, mas é sensível a linguagem coloquial.
- **Text-to-Speech:** As vozes são naturais e variadas, permitindo experiências mais humanas em aplicações como assistentes virtuais.

## 🧪 Exemplos de Uso

### 🎙️ 1. Transcrição em tempo real com microfone

```
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="YOUR_KEY", region="YOUR_REGION")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Fale algo...")

result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Você disse: {}".format(result.text))

```
## 🧾 2. Extração de Entidades Nomeadas
```
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "YOUR_ENDPOINT"
key = "YOUR_KEY"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = ["A Microsoft foi fundada por Bill Gates e Paul Allen em Albuquerque."]
response = client.recognize_entities(documents=documents)[0]

for entity in response.entities:
    print(f"Texto: {entity.text} | Categoria: {entity.category} | Subcategoria: {entity.subcategory}")
```
## ✅ Conclusão
O laboratório proporcionou uma experiência prática valiosa na utilização das ferramentas Azure Speech Studio e Language Studio.
Aprendemos a integrar a inteligência artificial em processos de análise de fala e linguagem natural, desenvolvendo soluções mais inteligentes e eficientes para diversas aplicações.

## 🔗 Referências
-Documentação Language Studio
-Documentação Speech Studio

# Emanuel Siqueira Lannes
