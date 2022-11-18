function check_form() {
    var fname =
        document.forms.fm.fname.value;
    var lname =
        document.forms.fm.lname.value;

    var gender =
        document.forms.fm.gender.value;

    var dob =
        document.forms.fm.dob.value;

    var fa =
        document.forms.fm.saddress.value;
    var la =
        document.forms.fm.caddress.value;

    var city =
        document.forms.fm.city.value;
    var region =
        document.forms.fm.region.value;

    var pin =
        document.forms.fm.pin.value;
    var country =
        document.forms.fm.country.value;

    var phone =
        document.forms.fm.mobile.value;
    var email =
        document.forms.fm.mail.value;

    var course =
        document.forms.fm.course.value;
    var fit =
        document.forms.fm.vehicle.value;

    var access =
        document.forms.fm.acesories.value;

    var uname =
        document.forms.fm.uid.value;
    var password =
        document.forms.fm.password.value;

    var regEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/g;  //Javascript reGex for Email Validation.
    var regPhone=/^\d{10}$/;                                        // Javascript reGex for Phone Number validation.
    var regName = /\d+$/g;                                    // Javascript reGex for Name validation

    if (fname == ""  || lname == "" || regName.test(fname)|| regName.test(lname) ) {
        window.alert("Please enter your name properly.");
        name.focus();
        return false;
    }

    if (fa == "" || la == "")  {
        window.alert("Please enter your address.");
        fa.focus();
        la.focus();
        return false;
    }
     
    if (email == "" || !regEmail.test(email)) {
        window.alert("Please enter a valid e-mail address.");
        email.focus();
        return false;
    }
      
    if (password == "") {
        alert("Please enter your password");
        password.focus();
        return false;
    }

    if(password.length <6){
        alert("Password should be atleast 6 character long");
        password.focus();
        return false;

    }
    if (phone == "" || !regPhone.test(phone)) {
        alert("Please enter valid phone number.");
        phone.focus();
        return false;
    }

    if (course=" ") {
        alert("course should not be empyt");
        course.focus();
        return false;
    }

    return true;
}