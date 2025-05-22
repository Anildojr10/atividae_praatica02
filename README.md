# 📚 Registro de Notas da Turma

Este é um programa em Python que permite a um professor registrar as notas dos alunos de uma turma, garantindo que apenas notas válidas (de 0 a 10) sejam consideradas. Ao final, o programa calcula e exibe a média da turma.

## ✅ Funcionalidades

- Permite o registro de múltiplas notas.
- Valida se a nota está entre 0 e 10.
- Ignora entradas inválidas ou fora do intervalo permitido.
- Encerra o registro quando o usuário digita `fim`.
- Calcula e exibe a média da turma.

## 🧠 Como funciona

1. O usuário é instruído a digitar notas ou a palavra `fim`.
2. Cada entrada é validada:
   - Se for um número entre 0 e 10, é adicionada à lista de notas.
   - Se for inválida, uma mensagem de erro é exibida.
3. Ao digitar `fim`, o programa calcula a média das notas registradas.

## ▶️ Como executar

1. Certifique-se de ter o Python instalado na sua máquina (versão 3.x).
2. Clone este repositório ou copie o arquivo Python.
3. Execute o programa via terminal ou prompt de comando:

```bash
python registrar_notas.py
```

## 💡 Exemplo de uso

```plaintext
Digite as notas dos alunos. Para encerrar, digite 'fim'.
Nota: 8
Nota: 9.5
Nota: 12
Nota inválida. Digite um valor entre 0 e 10.
Nota: sete
Entrada inválida. Digite um número ou 'fim'.
Nota: 7
Nota: fim
Média da turma: 8.17
```

## 🛠️ Requisitos

- Python 3.x

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
