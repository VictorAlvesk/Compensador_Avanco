# Compensador de Avanço – Exemplo 4

**Aluno:** Victor Alves Freire De Queiroz
**Matrícula:** 202307122

Projeto de um compensador do tipo avanço para o Exemplo 4 do material *SC_Cap4_05a_avanco.pdf*, fazendo o tempo de acomodação ficar 2 vezes menor que o do sistema sem compensação (C = 1) e o máximo sobressinal ficar em 25%.

## Arquivos

- `compensador_avanco.py` – código do projeto
- `requirements.txt` – bibliotecas necessárias

## Como executar

É preciso ter o Python 3 instalado. Abra o terminal na pasta do projeto e rode:

**Linux / Mac**

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python compensador_avanco.py
```

**Windows**

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python compensador_avanco.py
```

**Google Colab / Jupyter**

Em uma célula, rode `!pip install control`. Depois cole o código do `compensador_avanco.py` na célula seguinte e execute.

## O que aparece

No terminal são mostrados os parâmetros do compensador e os dados da resposta ao degrau, com e sem compensação. Em seguida abre o gráfico comparando as duas respostas, que também é salvo como `resposta_degrau_avanco.png`.

## Como foi feito

1. Sem compensação, os polos dominantes ficam em s = −0,3994 ± j1,9198, o que dá Ts ≈ 4/σ = 10,015 s.
2. Para Ts 2x menor, σ passa a 0,7988. Para MSS = 25%, ζ = 0,4037. Com isso, o polo desejado é s1 = −0,7988 ± j1,8102.
3. O zero do compensador foi colocado em −2, cancelando o polo da planta (T = 0,5).
4. Pela condição de ângulo, o polo do compensador precisa contribuir com 36,70°, o que o coloca em s = −3,2272 e dá α = 0,6197.
5. Pela condição de módulo, sai o ganho K.

## Resultados

Parâmetros obtidos:

- K = 0,6829
- α = 0,6197
- T = 0,5

C(s) = 0,6829 · (1 + 0,5s) / (1 + 0,3099s) = 1,1020 · (s + 2) / (s + 3,2272)

| | Sem compensação | Com avanço |
|---|---|---|
| Máximo sobressinal | 48,34 % | 23,29 % |
| Tempo de acomodação | 8,913 s | 4,428 s |
| Tempo de pico | 1,834 s | 1,933 s |

O tempo de acomodação ficou 2,01 vezes menor. O sobressinal ficou em 23,3%, perto dos 25% pedidos. A pequena diferença vem do terceiro polo em malha fechada (em s ≈ −5,63), que não entra na aproximação de segunda ordem usada no projeto.

## Problemas comuns

- **`No module named 'control'`**: o ambiente virtual não está ativado. Rode o comando `activate` de novo.
- **`Permissão negada` ao ativar no Linux**: falta o `source` na frente do comando.
- **Erro envolvendo NumPy e SciPy**: acontece quando os pacotes são misturados com os do sistema. Usando o ambiente virtual como descrito acima, isso não ocorre.
