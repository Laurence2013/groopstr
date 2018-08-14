function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Weekly_Fixtures: function() {
    var http = new XMLHttpRequest();
    console.log(http);
    http.onreadystatechange = function() {
      if(http.readyState == 4 && http.status == 200){
          var weekly_fixs = JSON.parse(http.responseText);
          console.log(weekly_fixs);
          var mainHtml = '';
          mainHtml = '<h2 class="weekly_fixtures">Weekly Fixtures</h2>';
          mainHtml += '<ul class="nav flex-column list-group">';
          for (i = 0; i < weekly_fixs.length; i++) {
            mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><a id="link-colour" class="nav-link active" href="'+ weekly_fixs[i].id +'">'+ weekly_fixs[i].fixture + '</a></li>';
          }
          mainHtml += '</ul>';
          weekly_fixtures.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_fixtures", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    weekly_fixtures.innerHTML = 'Weekly Fixtures ...';
  },
}
window.onload = function() {
  main = new CreateANewRequest();
  if (document.getElementById('weekly_fixtures')) {
    main.Weekly_Fixtures();
  }
}
