function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Weekly_Fixtures: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
          var weekly_fixs = JSON.parse(http.responseText);
          var mainHtml = '';
          mainHtml = '<h2 class="weekly_fixtures">Weekly Fixtures</h2>';
          mainHtml += '<ul class="nav flex-column list-group">';
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week: </b>'+ weekly_fixs[2].week_no + '</li>';
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week start date: </b>'+ weekly_fixs[2].start_date + '</li>';
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week end date: </b>'+ weekly_fixs[2].end_date + '</li>';
          for (i = 0; i < weekly_fixs.length; i++) {
            if (weekly_fixs[i].id) {
              mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Fixture id: </b>'+ weekly_fixs[i].id + ', <b>Fixture: </b>' + weekly_fixs[i].fixture + '</li>';
            }
          }
          mainHtml += '<a href="http://localhost:8000/admin_update/admin_get_weekly_tables/'+ weekly_fixs[2].week_no +'">'+ '<b>New current week is: </b>' + weekly_fixs[2].week_no +'</a>';
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
