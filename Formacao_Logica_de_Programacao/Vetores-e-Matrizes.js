
//Definindo Vetores=arrays, e definindo o index entre []
let pokemon = ["Pikachu" , "Charmander", "Bulbassaur"]
console.log(pokemon[0])


//Usandop um  vetor dentro de outro vetor, temos uma matriz.
let timePokemon = [
  ["Pikachu", "M", 1],
  ["Charmander", "M", 3],
  ["Bulbassaur", "M", 5]
]

//No caso de matrizes, temos 2 indexes para preencher nos []. Lembrando que é
//sempre alocado como linha/coluna.

console.log("O pokemon " + timePokemon[0][0] + " é do sexo " +  timePokemon[0][1] + 
" e está no nível: " + timePokemon[0][2] )