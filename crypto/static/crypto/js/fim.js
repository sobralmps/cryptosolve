function theend(){
    var nome = prompt("Digite o seu nome:");
    alert(nome + ", voce passou pela ultima fase.\n\nEm breve havera mais fases!\n\nA nossa equipe lhe parabeniza pelo feito, aqui fica uma pequena lembranca!");
    document.getElementById("header").innerHTML = "Congratulations";
    document.getElementById("footer").innerHTML = '<marquee scrollamount="50">' + nome + '</marquee>';
}