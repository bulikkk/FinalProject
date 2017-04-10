
document.addEventListener("DOMContentLoaded", function() {
	var sub = document.querySelector('#submit');

  	sub.addEventListener('click', function(){
  		document.querySelector('#team-form').classList.toggle('hidden');
  		document.querySelector('#loader-sign').classList.toggle('hidden');
  		document.querySelector('#loader-info').classList.toggle('hidden');
	});
});
