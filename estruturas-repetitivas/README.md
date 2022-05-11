## PARTE 3: ESTRUTURAS REPETITIVAS

### Exercício 3.1:
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha
incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser
impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.

Exemplos:

| Entrada: | Saída:           |
|----------|------------------|
| 2200     | Senha Invalida   |
| 1020     | Senha Invalida   |
| 2022     | Senha Invalida   |
| 2002     | Acesso Permitido |

| Entrada: | Saída:           |
|----------|------------------|
| 2020     | Senha Invalida   |
| 1031     | Senha Invalida   |
| 2002     | Acesso Permitido |

### Exercício 3.2:
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando
essas informações conforme exemplo (use a palavra "in" para dentro do intervalo, e "out" para fora do intervalo).

Exemplos:

| Entrada:                          | Saída:        |
|-----------------------------------|---------------|
| 5<br>14<br>123<br>10<br>-25<br>32 | 2 in<br>3 out |
| 4<br>86<br>35<br>20<br>7          | 1 in<br>3 out |