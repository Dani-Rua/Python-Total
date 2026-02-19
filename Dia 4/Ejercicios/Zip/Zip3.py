spanish = ["uno","dos","tres","cuatro","cinco"]
port = ["um","dois","três","quatro","cinco"]
english = ["one","two","three","four","five"]

cobinado = list(zip(spanish,port,english))
print(cobinado)

for spanish,port,english in cobinado:
    print(spanish,port,english)