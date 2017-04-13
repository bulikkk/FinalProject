document.addEventListener("DOMContentLoaded", function() {
  	var new_teams = document.querySelector('#new-teams');

  	new_teams.addEventListener('click', function() {
        document.querySelector('#finish-form').classList.toggle('hidden');
        document.querySelector('#loader-sign').classList.toggle('hidden');
        document.querySelector('#loader-info').classList.toggle('hidden');
    });
});