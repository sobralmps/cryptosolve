function conquistas(){

    var x = 0;
    var y = 0;
    var z = 0;

    var conquistas = new Array();

    conquistas[0] = "Completou as fases com cifra de Vigenere";
    conquistas[1] = "Completou as fases com cifra de Cesar";
    conquistas[2] = "Completou a ultima fase";

    if (x == 0){
        document.getElementById("Conquista1").innerHTML = conquistas[0];
    }
    if (y == 0){
        document.getElementById("Conquista2").innerHTML = conquistas[1];
    }
    if (z == 0){
        document.getElementById("Conquista3").innerHTML = conquistas[2];
    }

}