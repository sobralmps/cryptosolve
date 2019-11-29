function checar(form){
    cryptotext = form.cryptotext.value;
    if (cryptotext == "hello world"){
        alert("Indo para a fase 02")
        window.location.href="../endgame";
        }
    else {
        alert("Incorreto.")
        }
    return false;
    }
