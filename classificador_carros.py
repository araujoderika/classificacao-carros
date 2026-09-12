import pandas as pd  # ajuda a ler tabelas (como um Excel)
from sklearn.neighbors import KNeighborsClassifier  # o "cérebro" que aprende
from sklearn.model_selection import train_test_split  # separa exemplos pra estudar e pra testar

# 1. Abrimos o álbum de figurinhas com os exemplos de carros
carros = pd.read_csv(
    r"C:\Users\arauj\OneDrive\Desktop\Estudos Gerais\projetos-erika\projetos\1-classificacao-carros\carros.csv"
)
print("Aqui está o nosso álbum de carros:")
print(carros)

# 2. Separamos as "pistas" (potência e velocidade) da "resposta" (tipo do carro)
pistas = carros[["potencia_cv", "velocidade_max_kmh"]]
resposta = carros["tipo"]

# 3. Separamos uma parte dos carros pra ENSINAR o computador
#    e guardamos uma partinha pra TESTAR se ele aprendeu direito
pistas_treino, pistas_teste, resposta_treino, resposta_teste = train_test_split(
    pistas, resposta, test_size=0.3, random_state=42
)

# 4. Criamos o "cérebro" do computador (ele vai olhar os 3 carros mais
#    parecidos que já conhece pra decidir o tipo do carro novo)
cerebro = KNeighborsClassifier(n_neighbors=3)

# 5. Agora é hora de ESTUDAR! O computador olha os exemplos e aprende
cerebro.fit(pistas_treino, resposta_treino)

# 6. Vamos ver se ele aprendeu bem, testando com carros que ele não viu
palpites = cerebro.predict(pistas_teste)
print("\nO computador chutou:", list(palpites))
print("A resposta certa era:", list(resposta_teste))

# 7. Agora o mais legal: vamos inventar um carro novo e perguntar pro
#    computador que tipo de carro ele acha que é!
carro_misterioso = [[450, 290]]  # 300 cv de potência, 250 km/h de velocidade máxima
palpite = cerebro.predict(carro_misterioso)
print(f"\n🔍 Carro misterioso (300cv, 250km/h) -> o computador acha que é: {palpite[0]}")

