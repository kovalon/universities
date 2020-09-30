function checkFields(evt) {
    var name = document.getElementById("nameField");
    if(name.value === "") {
         alert("Fill in name");
         return false;
    }
    var address = document.getElementById("addressField");
    if(address.value === "") {
         alert("Fill in address");
         return false;
    }
    var subjects = document.getElementById("subjectsField");
    var subj_array = subjects.value.split(',');
    console.log(subj_array);
    if(subj_array.length < 2) {
         alert("Fill in subjects field at least two subjects");
         return false;
    }
    return true;
}