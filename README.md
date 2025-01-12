O interpretador likeForth, como qualquer interpretador Forth, interage com uma VM Forth, que suporta operações primitivas sobre duas pilhas: uma pilha de dados D e uma pilha de retorno R. Asim, as instruções passadas ao interpretador modificam uma dessas pilha de dados.

# Instruções
Cada instrução, utilizando a notação polonesa inversa, refere-se a uma palavra previamente definida ou definida pelo usuário. Em geral, todos os comandos consomem os elementos da pilha que utilizam, com poucas exceções.

Exemplo:
```
3 4 +
```
há três palavras nessa instrução: os números 3 e 4 e o sinal +.
3 e 4 são inseridos na pilha de dados D, enquanto + indica que os números no topo da pilha serão desempilhados, somados (4+3, note a notação polonesa inversa) e o resultado será inserido na pilha.
Assim, assumindo que a pilha D esteja vazia antes dessa instrução, ela passa a ter um único elemento após a execução de ```3 4 +```: 7.

# Palavras reconhecidas
Itálico representa sequências escritas pelo usuário.
| Palavra                  | Definição                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| : *palavra* *seq* ;      | Define *palavra* como *seq* (sequência de outras palavras)                                                   |
| *número real qualquer*   | Insere um número na pilha de dados D                                                                         |
| .                        | Remove o elemento do topo de D e exibe-o na tela                                                             |
| ." *string* "            | Exibe *string* na tela                                                                                       |
| acceptn                  | Lê um número real do teclado e o insere na pilha D                                                           |
| cr                       | Salta uma linha (mesmo que imprimir ```\n``` em C)                                                           |
| .s                       | Exibe pilhas D e R na tela                                                                                   |
| .d                       | Exibe palavras criadas pelo usuário na tela                                                                  |
| + - * / % sqrt           | Empilha em D o resultado da soma, subtração, multiplicação, divisão, resto ou raíz quadrada, respectivamente |
| true                     | Empilha -1 em D                                                                                              |
| false                    | Empilha 0 em D                                                                                               |
| > >= < <= eq neq         | Empilha 0 ou -1 em D de acordo com os operadores >, >=, <, <=, =, !=, respectivamente                        |
| or and                   | Empilha 0 ou -1 em D de acordo com os operadores relacionais or e and, respectivamente                       |
| drop                     | Desempilha valor no topo da pilha D                                                                          |
| swap                     | Troca os dois primeiros valores no topo de D (a b -> b a)                                                    |
| dup                      | Duplica o valor no topo de D (a b -> a a)                                                                    |
| rot                      | Rotaciona os três primeiros valores no topo da pilha D (a b c d -> a d b c)                                  |
| pick                     | Copia n-esimo valor pro topo de D (```2 PICK``` a b c -> a b c a)                                            |
| over                     | Copia número abaixo do topo de D para o topo (a b –> a b a)                                                  |
| >r                       | Move o topo de D para a pilha de resultados R                                                                |
| r>                       | Move o topo de R para a pilha de dados D                                                                     |
| r@                       | Copia o topo de R para a pilha de dados D                                                                    |
| begin *seq* *cond* until            | Repete *seq* até a condição *cond* ser satisfeita                                                 |
| *E B* do *seq* loop                 | Repete *seq* enquanto *B* < *E* (*E* indica o fim, *B* o início)                                  |
| i                                   | Empilha em D o valor corrente de *B* da instrução do                                              |
| *cond* if *seq1* [else *seq2*] then | Executa *seq1* se *cond* é verdadeira (senão, executa *seq2*). ```else``` é opcional              |
| ( *string* )                        | Comentários                                                                                       |
| rand                                | Empilha um valor aleatório entre 0 e o valor no topo da pilha D (não inclui esse valor)           |
| clear                               | Limpa as pilhas                                                                                   |
| bye                                 | Encerra o interpretador                                                                           |
