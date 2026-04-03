let convidado = {
  nome: "Pedrinho",
  idade: 10,
  presente: "quebra-cabeça"
};

console.log(convidado.nome + " tem " + convidado.idade + " anos e trouxe um " + convidado.presente + " de presente!");

convidado.localizacao = "Sala de Estar";
console.log(convidado.nome + " está na " + convidado.localizacao + ".");


//Toda vez que criarmos uma class, precisamos criar a funcao constructor.

//Podemos também adicionar métodos, para adicionar inteligência para nossas
//classes. Que é uma função que trabalha no contexto da classe.

class formaDeBolo {
    constructor(saborDaMassa, saborRecheio){
        this.saborDaMassa = saborDaMassa
        this.saborRecheio = saborRecheio
    }

    escrever(){
        console.log(`Um delicioso bolo de ${this.saborDaMassa} com recheio de ${this.saborRecheio}.`)
    }

    assando(){
        console.log(`Bolo de ${this.saborDaMassa} no forno!`)
    }
}

let boloFesta = new formaDeBolo("Chocolate", "Nutella")
let boloPremium = new formaDeBolo("Morango", "Leite Ninho")

boloFesta.assando()
boloFesta.escrever()
boloPremium.assando()
boloPremium.escrever()


