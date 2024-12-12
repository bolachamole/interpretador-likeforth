O interpretador likeForth, como qualquer interpretador Forth, interage com uma VM Forth, que suporta operações primitivas sobre duas pilhas: uma pilha de dados D e uma pilha de retorno R.
Asim, as instruções passadas ao interpretador modificam uma dessas pilha de dados.

Cada instrução refere-se a uma palavra previamente definida ou definida pelo usuário. Por exemplo:
```
3 4 +
```
há três palavras nessa instrução: os números 3 e 4 e o sinal +. 3 e 4 são inseridos na pilha de dados D, enquanto palavra + indica que os números no topo da pilha (4 e 3, 4 no topo) serão desempilhados,
somados (+) e o resultado (7) será inserido na pilha. Assim, assumindo que a pilha D esteja vazia antes dessa instrução, após a execução de "3 4 +", ela passa a ter um único elemento: 7.
