# 🏎️ Adivinhador de Carros

## O que é isso?

Imagina que você é um detetive de carros. Alguém te fala só duas coisas:
"esse carro tem tanta **potência** (força do motor)" e "ele anda até tal
**velocidade máxima**" — e você tem que adivinhar se é um **Sedan**,
uma **SUV** ou um carro **Esportivo**, sem nem ver a foto!

Um carro esportivo (tipo Ferrari) costuma ter muita potência e ser
bem rápido. Uma SUV é mais forte e "grandona", mas não é tão veloz.
Um sedan é mais equilibrado, nem tão forte nem tão fraco.

Vamos ensinar o computador a virar esse detetive!
Aqui trabalharemos a
**classificação**. 🕵️‍♀️✨

## Como o computador aprende?

1. Damos pro computador uma "tabela de exemplos" de carros que já
   sabemos o tipo (tipo um álbum de figurinhas com a resposta atrás)
2. Ele estuda e percebe padrões (ex: "muita potência + muito rápido
   = provavelmente é esportivo")
3. Quando aparece um carro novo, ele usa o que aprendeu pra adivinhar
   o tipo, mesmo nunca tendo visto esse carro antes

## Como rodar esse projeto

1. Instale o Python no seu computador (se ainda não tiver)
2. Abra o terminal na pasta desse projeto
3. Digite:
   ```
   pip install scikit-learn pandas
   ```
4. Depois digite:
   ```
   python classificador_carros.py
   ```
5. Veja o computador virar um detetive de carros! 🪄

## Arquivos

- `classificador_carros.py` → o "cérebro" que aprende e adivinha
- `carros.csv` → o álbum de figurinhas com exemplos de carros
