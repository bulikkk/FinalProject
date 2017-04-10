
document.addEventListener("DOMContentLoaded", function() {
	var train = document.querySelector('form');

  	train.addEventListener('submit', function(e){
    e.preventDefault();


	});
});


  		document.querySelector('#team-form').classList.toggle('hidden');
  		document.querySelector('#loader-sign').classList.toggle('hidden');
  		document.querySelector('#loader-info').classList.toggle('hidden');


document.addEventListener("DOMContentLoaded", function(){

  var form = document.querySelector('form');

  form.addEventListener('submit', function(e){
  e.preventDefault();
  console.log("form");
  var email = document.querySelector('#email');
  var name = document.querySelector('#name');
  var surname = document.querySelector('#surname');
  var pass1 = document.querySelector('#pass1');
  var pass2 = document.querySelector('#pass2');
  var agree = document.querySelector('#agree');
  console.log(pass1);

  if(email.value.indexOf("@") == -1)
  {
  console.log("No kidding give me an email folk");
  email.style.borderColor = "red";
  return false;
  }
  if(name.value.length <= 5)
  {
  console.log("No kidding give me an email folk");
  name.style.borderColor = "red";
  return false;
  }
  if(surname.value.length <= 5)
  {
  console.log("No kidding give me an email folk");
  surname.style.borderColor = "red";
  return false;
  }

  if(pass1.value.length < 5 || pass1.value != pass2.value) {
  pass1.style.borderColor = "red";
  pass2.style.borderColor = "red";
  return false;

  form.submit();

  });

});