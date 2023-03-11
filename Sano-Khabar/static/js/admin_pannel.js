//add more title
function OpenDiv() {
    var obox = document.getElementById("form1");
    obox.classList.toggle("form2");
}
// Added Title Sub Page
function myFunction() {
    var new_box = document.getElementById("add_new");
    new_box.classList.toggle("mystyle");
}
//titles name changing
function openform(abc, ids) {
    var myElement = document.getElementById("_category_id");
    myElement.value = ids;

    document.getElementById("popup_myForm").style.display = "block";
    
}

function closeform() {
    document.getElementById("popup_myForm").style.display = "none";
}
//merging_ss_edit_news
function myFunction() {
    var new_box = document.getElementById("add_new");
    new_box.classList.toggle("mystyle");
}
//for notification popup
function openform_noti() {
    document.getElementById("popup_myForm_noti").style.display = "block";
}

function closeform_noti() {
    document.getElementById("popup_myForm_noti").style.display = "none";
}
