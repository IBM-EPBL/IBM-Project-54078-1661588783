
function loogin(){
    var name=
        document.forms.f1.uname.value;
    var pass=
    document.forms.f1.pwd.value;

    if( name == "IBM2022" && pass == "Batch03"){
       
        document.getElementById("lgn").onclick = function () {
        window.location.replace("/dashboard");
    }
    }
    return true;

}
