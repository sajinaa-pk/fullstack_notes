function validation(){
    var fname=document.forms["fbform"]["FName"]; 
    var sname=document.forms["fbform"]["SName"];
    var num=document.forms["fbform"]["Num"];  
    var email=document.forms["fbform"]["Email"];
    var x=email.value;
    var atposition=x.indexOf('@');
    var dotposition=x.lastIndexOf('.');
    var psd=document.forms["fbform"]["Password"];
    var day=document.forms["fbform"]["Day"];
    var month=document.forms["fbform"]["Month"];
    var year=document.forms["fbform"]["Year"];
    var sex=document.forms["fbform"]["gender"];

    if(fname.value=="")
    {
        alert('First name required');
        fname.focus();
        return false;
    }
    if(sname.value=="")
    {
        alert('Surname required');
        sname.focus();
        return false;
    }
    if(num.value=="")
    {
        alert('Mobile number required');
        num.focus();
        return false;
    }
    if(num.value.length<10){
        alert("Required 10 digits")
        num.focus();
        return false;
    }
    if(email.value==""){
        alert("Email required")
        email.focus();
        return false;
    }
    if(atposition<1||dotposition<atposition+2||dotposition+2>=x.length)
    {
        alert('Please Enter a valid Email');
        email.focus();
        return false;
    }
    if(psd.value=="")
    {
        alert('Password is required');
        psd.focus();
        return false;
    }
    
    if(psd.value.length<8)
    {
        alert("Required min 8 Chars")
        psd.focus();
        return false;
    }
    if(day.value=="")
    {
        alert('birth day required');
        day.focus();
        return false;
    }
    if(month.value=="")
    {
        alert('birth month required');
        month.focus();
        return false;
    }
    if(year.value=="")
    {
        alert('birth year required');
        year.focus();
        return false;
    }
    if(sex.value=="")
    {
        alert('gender is required');
        sex.focus();
        return false;
    }
}