function checar(form){
    cryptotext = form.cryptotext.value;
    if (cryptotext == "hello world"){
        alert("Indo para a fase 02")
        window.location.href="../embreve";
        }
    else {
        alert("Incorreto.")
        }
    return false;
    }
