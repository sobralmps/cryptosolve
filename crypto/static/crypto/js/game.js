function checar(form){

    cryptotext = form.cryptotext.value;

    if (cryptotext == "hello world"){
        window.location.href="../ldbg";
        alert("Indo para fase 2");
    }

    else if (cryptotext == "desenvolvimento web"){
        window.location.href="../ziex";
        alert("Indo para fase 3");
    }

    else if (cryptotext == "supremo"){
        window.location.href="../yuckzd";
        alert("Indo para fase 4");
    }

    else if (cryptotext == "segunda"){
        window.location.href="../vwtto";
        alert("Indo para fase 5");
    }

    else if (cryptotext == "serpente"){
        window.location.href="../xmiu";
        alert("Indo para fase 6");
    }

    else if (cryptotext == "hello2world"){
        window.location.href="../jmix";
        alert("Indo para fase 7");
    }

    else if (cryptotext == "primeiro"){
        window.location.href="../coko";
        alert("Indo para fase 8");
    }

    else if (cryptotext == "para sempre"){
        window.location.href="../swvg";
        alert("Indo para fase final");
    }

    else if (cryptotext == "ultima"){
        alert("Uau, voce completou todas as fases!")
        window.location.href="../wqb";
    }

    else {
        alert("Incorreto.")
    }

    return false;

}
