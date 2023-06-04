# Aula 0

## Criando Código com Python

- O VS Code é um tipo especial de editor de texto chamado compilador. Na parte superior, você notará um editor de texto e na parte inferior, verá um terminal onde poderá executar comandos.
- No terminal, você pode executar `code ola.py` para iniciar a codificação.
- No editor de texto acima, você pode digitar `print("olá, mundo")`. Este é um programa canônico famoso que quase todos os codificadores escrevem durante o processo de aprendizado.
- Na janela do terminal, você pode executar comandos. Para executar este programa, você precisará mover o cursor para a parte inferior da tela, clicando na janela do terminal. Agora você pode digitar um segundo comando na janela do terminal. Ao lado do cifrão, digite `python ola.py` e pressione a tecla `⏎ Enter` no teclado.
- Lembre-se, os computadores realmente só entendem zeros e uns. Portanto, quando você executar `python ola.py`, o python interpretará o texto que você criou `ola.py` e o traduzirá em zeros e uns que o computador possa entender.
- O resultado da execução do `python ola.py` programa é `olá, mundo`.
- Parabéns! Você acabou de criar seu primeiro programa.

## Funções

- Funções são verbos ou ações que o computador ou a linguagem de computador já saberão executar.
- Em seu `ola.py` programa, a `print` função sabe como imprimir na janela do terminal.
- A `print` função recebe argumentos. Neste caso, `"olá, mundo"` são os argumentos que a `print` função recebe.

## Bugs

- Bugs são uma parte natural da codificação. São erros, problemas para você resolver! Não desanime! Isso faz parte do processo de se tornar um grande programador.
- Imagine em nosso `ola.py` programa aquele aviso digitado acidentalmente `print("olá, mundo"` que perdemos o final `)` exigido pelo compilador. Se eu cometer esse erro propositalmente, o compilador exibirá um erro na janela do terminal!
- Frequentemente, as mensagens de erro informam sobre seu erro e fornecem pistas sobre como corrigi-lo. No entanto, muitas vezes o compilador não é desse tipo.

## Melhorando seu primeiro programa em Python

- Podemos personalizar seu primeiro programa Python.

- Em nosso editor de texto `ola.py` podemos adicionar outra função. `input` é uma função que recebe um prompt como argumento. Podemos editar nosso código para dizer

```python
input("Qual o seu nome? ")
print("olá, mundo")
```

- Esta edição sozinha, no entanto, não permitirá que seu programa produza o que seu usuário insere. Para isso, precisaremos apresentá-lo às variáveis

### Variáveis

- Uma variável é apenas um recipiente para um valor dentro de seu próprio programa.

- Em seu programa, você pode introduzir sua própria variável editando-a para ler

```python
nome = input("Qual o seu nome? ")
print("olá, mundo")
```

Observe que esse `=` sinal de igual no meio `nome = input("Qual o seu nome? ")` tem um papel especial na programação. Este sinal de igual atribui literalmente o que está à direita ao que está à esquerda. Portanto, o valor retornado por `input("Qual o seu nome? ")` é atribuído a `nome`.

- Se você editar seu código da seguinte maneira, notará um erro

```python
nome = input("Qual o seu nome? ")
print("olá, nome")
```

- O programa retornará `olá, nome` na janela do terminal independentemente do que o usuário digitar.

- Editando ainda mais nosso código, você pode digitar

```python
nome = input("Qual o seu nome? ")
print("olá,")
print(nome)
```

- O resultado na janela do terminal seria

```prompt
Qual o seu nome? David
olá
David
```

- Estamos cada vez mais perto do resultado que pretendemos!

- Você pode aprender mais na documentação do Python sobre [tipos de dados](https://docs.python.org/3/library/datatypes.html).

### Comentários

- Os comentários são uma forma de os programadores rastrearem o que estão fazendo em seus programas e até mesmo informarem outras pessoas sobre suas intenções para um bloco de código. Resumindo, são notas para você e para outras pessoas que verão seu código!

- Você pode adicionar comentários ao seu programa para poder ver o que ele está fazendo. Você pode editar seu código da seguinte maneira:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")
print("ola,")
print(nome)
```

- Os comentários também podem servir como lista de tarefas para você.

### Pseudocódigo

- Pseudocódigo é um tipo importante de comentário que se torna um tipo especial de lista de tarefas, especialmente quando você não entende como realizar uma tarefa de codificação. Por exemplo, em seu código, você pode editá-lo para dizer:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")

# Exiba olá
print("olá,")

# Exiba o nome inserido
print(nome)
```

## Melhorando ainda mais seu primeiro programa Python

- Podemos editar ainda mais nosso código da seguinte maneira:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")

# Exiba olá e o nome inserido
print("olá, " + nome)
```

- Acontece que algumas funções levam muitos argumentos.

- Podemos usar uma vírgula `,` para passar vários argumentos editando nosso código da seguinte maneira:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")

# Exiba olá e o nome inserido
print("olá,", nome)
```

A saída no terminal, se digitássemos “David”, seríamos `hello, David`. Sucesso.

## Strings e Parâmetros

- Uma string, conhecida como `str` em Python, é uma sequência de texto.

- Retrocedendo um pouco em nosso código de volta ao seguinte, houve um efeito colateral visual de ter o resultado exibido em várias linhas:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")
print("olá,")
print(nome)
```

- As funções recebem argumentos que influenciam seu comportamento. Se olharmos a documentação, [`print`](https://docs.python.org/3/library/functions.html#print) você perceberá que podemos aprender muito sobre os argumentos que a função print recebe.

- Olhando para esta documentação, você aprenderá que a função de impressão inclui automaticamente um pedaço de código `end='\n'`. O \n indica que a função de impressão criará automaticamente uma quebra de linha ao ser executada. A função print recebe um argumento chamado end` e o padrão é criar uma nova linha.

- No entanto, podemos tecnicamente fornecer um argumento para `end` nós mesmos de modo que uma nova linha não seja criada!

- Podemos modificar nosso código da seguinte maneira:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")
print("olá,", end="")
print(nome)
```

Ao fornecer, `end=""` estamos sobrescrevendo o valor padrão de `end` tal forma que nunca crie uma nova linha após esta primeira instrução de impressão. Fornecendo o nome como “David”, a saída na janela do terminal será `olá, David`.

- Parâmetros, portanto, são argumentos que podem ser obtidos por uma função.

- Você pode aprender mais na documentação do Python em [print](https://docs.python.org/3/library/functions.html#print).

### Um pequeno problema com as aspas

- Observe como adicionar aspas como parte de sua string é um desafio.
- `print("olá,"amigo"")` não funcionará e o compilador lançará um erro.
- Geralmente, existem duas abordagens para corrigir isso. Primeiro, você pode simplesmente alterar as aspas para aspas simples.
- Outra abordagem mais comumente usada seria codificar como `print("olá, \"amigo\"")`. As barras invertidas informam ao compilador que o seguinte caractere deve ser considerado uma aspa na string e evita um erro do compilador.

## Formatando Strings

- Provavelmente, a maneira mais elegante de usar strings seria a seguinte:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")
print(f"olá, {nome}")
```

Observe o `f` em `print(f"olá, {nome}")`. Este `f` é um indicador especial para o Python tratar esta string de uma maneira especial, diferente das abordagens anteriores que ilustramos nesta palestra. Espere que você use esse estilo de strings com bastante frequência neste curso.

## Mais Strings

- Você nunca deve esperar que seu usuário coopere como pretendido. Portanto, você precisará garantir que a entrada de seu usuário seja corrigida ou verificada.

- Acontece que embutido em strings está a capacidade de remover espaços em branco de uma string.

- Ao utilizar o método `strip` em `nome` as `nome = nome.strip()`, ele removerá todos os espaços em branco à esquerda e à direita da entrada do usuário. Você pode modificar seu código para ser:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")

# Remova os espaços em branco da string
nome = nome.strip()

# Exiba a saída
print(f"olá, {nome}")
```

Executando novamente este programa, independentemente de quantos espaços você digitar antes ou depois do nome, todos os espaços em branco serão removidos.

- Usando o método `title`, o título seria o nome do usuário:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")

# Remova os espaços em branco da string
nome = nome.strip()

# Capitalizar a primeira letra de cada palavra
nome = nome.title()

# Exiba a saída
print(f"olá, {nome}")
```

- A essa altura, você pode estar muito cansado de digitar `python` repetidamente na janela do terminal. Você usa a seta para cima do seu teclado para recordar os comandos de terminal mais recentes que você fez.

- Observe que você pode modificar seu código para ser mais eficiente:

```python
# Pergunte ao usuário o nome dele
nome = input("Qual o seu nome? ")

# Remova o espaço em branco do str e coloque
# em maiúscula a primeira letra de cada palavra
nome = nome.strip().title()

# Exiba a saída
print(f"olá, {nome}")
```

Isso cria o mesmo resultado do seu código anterior.

- Poderíamos até ir mais longe!

```python
# Pergunte ao usuário seu nome, remova os espaços em branco
# do str e coloque em maiúscula a primeira letra de cada palavra
nome = input("Qual o seu nome? ").strip().title()

# Exiba a saída
print(f"olá, {nome}")
```

- Você pode aprender mais sobre strings na documentação do Python em [`str`](https://docs.python.org/3/library/stdtypes.html#str)

## Inteiros ou int

- Em Python, um número inteiro é chamado de `int`.

- No mundo da matemática, estamos familiarizados com os operadores +, -, *, / e %. Esse último operador `%` ou operador de módulo pode não ser muito familiar para você.

- Você não precisa usar a janela do editor de texto em seu compilador para executar o código Python. No seu terminal, você pode executar `python` sozinho. Você será apresentado `>>>` na janela do terminal. Você pode então executar um código interativo ao vivo. Você pode digitar `1+1` e ele executará esse cálculo. Este modo não será comumente usado durante este curso.

- Abrindo o VS Code novamente, podemos digitar `code calculadora.py` no terminal. Isso criará um novo arquivo no qual criaremos nossa própria calculadora.

- Primeiro, podemos declarar algumas variáveis.

```python
x = 1
y = 2

z = x + y

print(z)
```

Naturalmente, quando executamos, `python calculadora.py` obtemos o resultado na janela do terminal de `3`. Podemos tornar isso mais interativo usando o `input` função.

```python
x = input("Qual o valor de x? ")
y = input("Qual o valor de y? ")

z = x + y

print(z)
```

- Executando este programa, descobrimos que a saída está incorreta como `12`. Por que isso pode ser?

- Anteriormente, vimos como o `+` sinal concatena duas strings. Como a entrada do teclado do computador entra no compilador como texto, ela é tratada como string. Nós, portanto, precisamos converter essa entrada de uma string para um número inteiro. Podemos fazê-lo da seguinte forma:

```python
x = input("Qual o valor de x? ")
y = input("Qual o valor de y? ")

z = int(x) + int(y)

print(z)
```

O resultado agora está correto. O uso de `int(x)`, é chamado de “casting” onde um valor é temporariamente alterado de um tipo de variável (neste caso uma string) para outro (aqui, um inteiro).

- Podemos melhorar ainda mais nosso programa da seguinte forma:

```python
x = int(input("Qual o valor de x? "))
y = int(input("Qual o valor de y? "))

print(x + y)
```

Isso ilustra que você pode executar funções em funções. A função mais interna é executada primeiro e, em seguida, a externa é executada. Primeiro, a função `input` é executada. Em seguida, a função `int`.

- Você pode aprender mais na Documentação do Python sobre [`int`](https://docs.python.org/3/library/functions.html?highlight=float#int).

## Legibilidade vence

- Ao decidir sobre sua abordagem para uma tarefa de codificação, lembre-se de que pode-se fazer um argumento razoável para muitas abordagens para o mesmo problema.
- Independentemente da abordagem que você adota para uma tarefa de programação, lembre-se de que seu código deve ser legível. Você deve usar comentários para dar a si mesmo e aos outros pistas sobre o que seu código está fazendo. Além disso, você deve criar o código de forma que seja legível.

## Noções básicas de Ponto Flutuante

- Um valor de ponto flutuante é um número real que possui um ponto decimal, como `0.52`.

- Você pode alterar seu código para suportar *floats* da seguinte maneira:

```python
x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))

print(x + y)
```

Essa alteração permite que seu usuário insira `1.2` e `3.4` apresente um total de `4.6`.

- Vamos imaginar, entretanto, que você queira arredondar o total para o inteiro mais próximo. Olhando para a documentação do Python, `round` você verá que os argumentos disponíveis são `round(number[n, ndigits])`. Esses colchetes indicam que algo opcional pode ser especificado pelo programador. Portanto, você poderia `round(n)` arredondar um dígito para o inteiro mais próximo. Como alternativa, você pode codificar da seguinte maneira:

```python
# Obtém a entrada do usuário
x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))

# Cria um resultado arredondado
z = round(x + y)

# Exiba a saída
print(z)
```

A saída será arredondada para o inteiro mais próximo.

- E se quiséssemos formatar a saída de números longos? Por exemplo, em vez de ver `1000`, você pode querer ver `1,000`. Você pode modificar seu código da seguinte maneira:

```python
# Obtém a entrada do usuário
x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))

# Cria um resultado arredondado
z = round(x + y)

# Exiba a saída
print(f"{z:,}")
```

Embora bastante enigmático, isso `print(f"{z:,}")` cria um cenário em que a saída `z` incluirá vírgulas onde o resultado pode parecer `1,000` ou `2,500`.

## Mais sobre Pontos Flutuantes

- Como podemos arredondar valores de ponto flutuante? Primeiro, modifique seu código da seguinte maneira:

```python
# Obtém a entrada do usuário
x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))

# Calcula o resultado
z = x / y

# Exiba a saída
print(z)
```

Ao inserir `2` como x e `3` como y, o resultado z `0.6666666666` aparentemente se torna infinito, como poderíamos esperar.

- Vamos imaginar que queremos arredondar isso para baixo, poderíamos modificar nosso código da seguinte forma:

```python
# Obtém a entrada do usuário
x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))

# Calcula o resultado e arredonda
z = round(x / y, 2)

# Exiba a saída
print(z)
```

Como poderíamos esperar, isso arredondará o resultado para as duas casas decimais mais próximas.

- Também poderíamos usar `fstring` para formatar a saída da seguinte maneira:

```python
# Obtém a entrada do usuário
x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))

# Calcula o resultado
z = x / y

# Exiba a saída
print(f"{z:.2f}")
```

Esse código enigmático `fstring` exibe o mesmo que nossa estratégia de arredondamento anterior.

- Você pode aprender mais na documentação do Python sobre [`float`](https://docs.python.org/3/library/functions.html?highlight=float#float).

## Def

- Não seria legal criar nossas próprias funções?

- Vamos trazer de volta nosso código final `ola.py` digitando `code ola.py`na janela do terminal. Seu código inicial deve ter a seguinte aparência:

```python
# Pergunte ao usuário seu nome, remova os espaços em branco
# do str e coloque em maiúscula a primeira letra de cada palavra
nome = input("Qual o seu nome? ").strip().title()

# Exiba a saída
print(f"olá, {nome}")
```

Podemos melhorar nosso código para criar nossa própria função especial que diga “olá” para nós!

- Apagando todo nosso código em nosso editor de texto, vamos começar do zero:

```python
nome = input("Qual o seu nome? ")
ola()
print(nome)
```

Tentando executar este código, seu compilador lançará um erro. Afinal, não existe uma função definida para `ola`.

- Podemos criar nossa própria função chamada `ola` da seguinte forma:

```python
def ola():
    print("olá")

nome = input("Qual o seu nome? ")
ola()
print(nome)
```

Observe que tudo abaixo `def ola()` é indentado. Python é uma linguagem indentada. Ele usa indentação para entender o que faz parte da função acima. Portanto, tudo na função `ola` deve ser indentada. Quando algo não está indentado, ele o trata como se não estivesse dentro da função `ola`. Executando `python ola.py` na janela do terminal, você verá que sua saída não é exatamente como você deseja.

- Podemos melhorar ainda mais nosso código:

```python
# Cria nossa própria função
def ola(para):
    print("olá,", para)


# Saída usando nossa própria função
nome = input("Qual o seu nome? ")
ola(nome)
```

Aqui, nas primeiras linhas, você está criando sua função `ola`. Desta vez, no entanto, você está dizendo ao compilador que esta função recebe um único parâmetro: uma variável chamada `to`. Portanto, quando você chama `ola(nome)` o computador passa `nome` para a função `ola` como `to`. É assim que passamos valores para funções. Muito útil! Executando `python ola.py` na janela do terminal, você verá que a saída está muito mais próxima do nosso ideal apresentado anteriormente nesta palestra.

- Podemos alterar nosso código para adicionar um valor padrão a `ola`:

```python
# Cria nossa própria função
def ola(para="mundo"):
    print("olá,", para)


# Saída usando nossa própria função
nome = input("Qual o seu nome? ")
ola(nome)

# Saída sem passar os argumentos esperados
ola()
```

Teste você mesmo seu código. Observe como o primeiro `ola` se comportará conforme o esperado e o segundo ola, que não recebe um valor, será, por padrão, output `olá, mundo`.

- Não precisamos ter nossa função no início do nosso programa. Podemos movê-lo para baixo, mas precisamos informar ao compilador que temos uma função `main` e temos uma função `ola` separada.

```python
def main():

    # Saída usando nossa própria função
    nome = input("Qual o seu nome? ")
    ola(nome)

    # Saída sem passar os argumentos esperados
    ola()


# Cria nossa própria função
def ola(para="mundo"):
    print("olá,", para)
```

Isso por si só, no entanto, criará uma espécie de erro. Se executarmos `python ola.py` nada acontece! A razão para isso é que nada neste código está realmente chamando a função `main` e dando vida ao nosso programa.

- A seguinte modificação muito pequena chamará a função `main` e restaurará nosso programa para funcionar corretamente:

```python
def main():

    # Saída usando nossa própria função
    nome = input("Qual o seu nome? ")
    ola(nome)

    # Saída sem passar os argumentos esperados
    ola()


# Cria nossa própria função
def ola(para="mundo"):
    print("olá,", para)


main()
```

## Retornando Valores

- Você pode imaginar muitos cenários em que não deseja apenas que uma função execute uma ação, mas também que retorne um valor para a função principal. Por exemplo, em vez de simplesmente imprimir o cálculo de `x + y`, você pode querer uma função para retornar o valor desse cálculo para outra parte do seu programa. Esse “repasse” de um valor chamamos de valor `return`.

- Voltando ao nosso código `calculadora.py` digitando `code calculadora.py`. Apague todo o código lá. Refaça o código da seguinte forma:

```python
def main():
    x = int(input("Qual o valor de x? "))
    print("x ao quadrado é", quadrado(x))


def quadrado(n):
    return n * n


main()
```

Efetivamente, `x` é passado para `quadrado`. Em seguida, o cálculo de `x * x` é retornado à função principal.

## Resumindo

Através do trabalho desta única palestra, você aprendeu habilidades que usará inúmeras vezes em seus próprios programas. Você aprendeu sobre…

- Criando seus primeiros programas em Python;
- Funções;
- Bugs;
- Variáveis;
- Comentários;
- Pseudo-código;
- Strings;
- Parâmetros;
- Strings formatadas;
- Inteiros;
- Princípios de legibilidade;
- Ponto Flutuante;
- Criando suas próprias funções; e
- Valores de retorno.
