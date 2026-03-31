/*Operadores Lógicos*/

// AND ( && )
let idade = 18
let vistoVerificado = false
let results =  (idade >= 18) && (vistoVerificado === true) 
console.log(results)

// AND ( && ) - 100 moedas coletadas E 1 item estrela
let moedasColetadas = 99
let item = "estrela"
let resultado = (moedasColetadas >= 100) && (item === "estrela")
console.log(resultado)

// OR ( || ) - nosso boneco só pode sair se tiver sem chuva OU com guarda Chuva
let clima = "chuva"
let acessorio = "guarda chuva"
let podeSairAgora = (clima !== "chuva") || (acessorio === "guarda chuva")
console.log("nosso personagem pode sair ? " + podeSairAgora)

// OR ( || ) - nosso boneco só pode sair se tiver sem chuva OU com guarda Chuva
let weather= "chuva"
let acess = "guarda chuva"
let podeSair = (weather !== "chuva") || (acess === "guarda chuva")
console.log("nosso personagem pode sair ? " + podeSair)

// NOT  ( !) - nega uma afirmação
let tempo = "chuva"
let horario = 8
let resultados = !((tempo !== "chuva") && (horario > 6))
console.log(resultados)