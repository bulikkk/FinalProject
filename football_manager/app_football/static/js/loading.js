//     var img = $('img.loader');
//     var btn = $('button.submit');
//
//     btn.on('click', function(){
//         $('.team-form').addClass('hidden');
//         $('.loader').removeClass('hidden');
//     });

document.addEventListener("DOMContentLoaded", function() {
	var btn = document.querySelector('.submit');

  	btn.addEventListener('click', function(){
  		document.querySelector('.team-form').classList.toggle('hidden');
  		document.querySelector('.loader').classList.toggle('hidden');
});
});

// $('.loader').on('click', function() {
// 		// Animate loader off screen
// 		$('.loader').fadeIn("fast");
// 	});