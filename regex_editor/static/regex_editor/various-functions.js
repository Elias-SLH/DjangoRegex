function regexType() {
  var regex_type = document.querySelector('input[name="regex_type"]:checked').value;
  var sub = document.getElementById('substitution');
  if (regex_type == "sub") {
      sub.style.display = "block";
      sub.required = true;
    } else {
      sub.style.display = "none";
      sub.required = false;
    }
}


function displaySub() {
  var regex_type = document.querySelector('input[name="regex_type"]:checked').value;
  var sub = document.getElementById('substitution');
  if (regex_type == "sub") {
      sub.style.display = "block";
      sub.required = true;
    } else {
      sub.style.display = "none";
      sub.required = false;
    }
}
window.onload = displaySub;
