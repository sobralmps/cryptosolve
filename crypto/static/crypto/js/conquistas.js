function conquistas(){

    var conq1 = 1;
    var conq2 = 1;
    var conq3 = 1;

    var conquistas = new Array();

    conquistas[0] = "Completou as fases com cifra de Vigenere";
    conquistas[1] = "Completou as fases com cifra de Cesar";
    conquistas[2] = "Completou a ultima fase";

    document.getElementById("principal").innerHTML = "Pagina ainda em desenvolvimento!";

    if (conq1 == 1){
        document.getElementById("Conquista1").innerHTML = conquistas[0];
    }
    if (conq2 == 1){
        document.getElementById("Conquista2").innerHTML = conquistas[1];
    }
    if (conq3 == 1){
        document.getElementById("Conquista3").innerHTML = conquistas[2];
    }

}