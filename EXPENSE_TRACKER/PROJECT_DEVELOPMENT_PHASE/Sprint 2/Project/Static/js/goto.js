
function goto(){
    var name=
        document.forms.f1.uname.value;
    var pass=
    document.forms.f1.pwd.value;

    if( name == "IBM2022" && pass == "Batch03"){
        return true;
        document.innerHTML="/dashboard";
    }

    return true;

}
