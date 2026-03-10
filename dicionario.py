

matricula1 = 2026001
nome1 = "Ana Silva"
telefone1 = "9999-8888"

aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva",
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruno": "Bruno"
    "@joão": "João"
}

print(contato)
print(type(contato))

print(contato["@camila"])

print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))

print("Original: ", contato)

contato["@Giovanna"] = "Giovanna"
print("Após add: ", contato)

contato["@paola"] = "Paola OLiveira"
print("Após add: ", contato)

contato.update(
    {
        "@bruna": "Bruna Marquezine",
        "@camila": "Camila Q."
    }
)

removido = contato.pop("@sheron")
print(f"Removido: {removido}")
print("Após o pop: ", contato)

del contato["@paola"]
print("Após clear: ", contato)

print("Número de contato: ", len(contato))

contato.pop("@camila")
print("Após remover um: ", len(contato))

if "@João" in contato:
    print(f"Encontrado: {contato['@joao']}")

if "@inexistente" in contato
vazio = {}


dados = {
    "nome": "João",
    "idade": 25,
    "altura": 1.70,
    "ativo": True
}

print("Após atualização")

("Vazio: ", vazio)
