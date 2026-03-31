/*Operadores Relacionais*/

let marca = "Apple"
console.log(marca !== "Samsung")

// = é atribuição
// == é para comparar o valor
// === é para comparar o valor e o tipo da variável
// !== é diferente ?


//guardar o valor em uma variável de resultado TRUE?FALSE
let cpfBloqueado = "123.445.222-45"
let cpfUsuario = "222.111.222-09"
let ehCPFBloqueado = cpfUsuario === cpfBloqueado

console.log("O usuario está barrado ? " + ehCPFBloqueado)

let CPFPermitido = "222.555.333-02"
let CPFDoUsuario = "222.555.333-02"

let ehBloqueado = CPFDoUsuario !== CPFPermitido

console.log("é um usuario invalido ? " + ehBloqueado)

/*Verificando idade com operadores*/
let idadeMinima = 18
let idadeCliente = 18
let idadePermitidaValida = idadeCliente >= idadeMinima

console.log(idadePermitidaValida)


let idadeDeCorte = 50
let idadeUsuario = 45

let resultadoEhTerceiraIdade = idadeDeCorte <= idadeUsuario
console.log(resultadoEhTerceiraIdade)
