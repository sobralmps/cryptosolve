function gerarquests(){

    var quest1 = new Array ();
    var quest2 = new Array ();
    var quest3 = new Array ();

    quest1[0] = "Passar pelas duas primeiras fases";
    quest1[1] = "Passar pela ultima fase";
    quest1[2] = "Passar a parte com cifra de Cesar";

    quest2[0] = "Entender a cifra Nihilist";
    quest2[1] = "Entender o que e cifra de Vigenere";
    quest2[2] = "Entender o que e cifra de Cesar";

    quest3[0] = "Nenhuma";
    quest3[1] = "Encontrar o easteregg da pagina final";
    quest3[2] = "Nenhuma";

    var x = Math.floor(3*Math.random());
    var y = Math.floor(3*Math.random());
    var z = Math.floor(3*Math.random());

    document.getElementById("Quest1").innerHTML = quest1[x];
    document.getElementById("Quest2").innerHTML = quest2[y];
    document.getElementById("Quest3").innerHTML = quest3[z];
}