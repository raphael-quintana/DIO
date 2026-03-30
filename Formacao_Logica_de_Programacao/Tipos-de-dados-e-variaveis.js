/*console.log seria o equivalente ao print() do python, ou printf() do C.*/
console.log("Digite o nome do seu jogador:")

/*let declara uma variável*/
let nickname = "DoomSlayer"

/*concantenando uma mensagem fixa + uma variável*/
console.log("Bem vindx " + nickname)
console.log(nickname + " entrou no servidor")

/*const declara uma constante.*/
const message = "Hellwalker says: "

/*saida concatenando a constante e a mensagem seguinte*/
console.log(message + "Rip and Tear!")
console.log(message + "Boom!")

/*concatenando variáveis e constantes*/

let poteCafe = "Café Pilão"
let poteAcucar = "Açúcar União"
let poteBiscoito = "Biscoito Maizena"
const mensagemDaVovo = "Na cozinha hoje tem: "

console.log(mensagemDaVovo + 
    poteCafe + " - " +
    poteAcucar + " - " +
    poteBiscoito
)

poteCafe = "Café Brasileiro"

console.log(mensagemDaVovo + 
    poteCafe + " - " +
    poteAcucar + " - " +
    poteBiscoito
)

//pokemon
let nomePokemon = "pikachu"
let pokemonSexo = "M"

let nivelPokemon = 20
let pontosDeVidaPokemon = 45

let selecionavel = false