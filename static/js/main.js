function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Get_Week: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
          var weekly_fixs = JSON.parse(http.responseText);
          console.log(weekly_fixs);
          var mainHtml = '';
          // mainHtml = '<h2 class="weekly_fixtures">Weekly Fixtures</h2>';
          // mainHtml += '<ul class="nav flex-column list-group">';
          // var is_once_only = false;
          // for (i = 0; i < weekly_fixs.length; i++) {
          //   if (weekly_fixs[i].week_no && is_once_only == false) {
          //     mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week: </b>'+ weekly_fixs[i].week_no + '</li>';
          //     mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week start date: </b>'+ weekly_fixs[i].start_date + '</li>';
          //     mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week end date: </b>'+ weekly_fixs[i].end_date + '</li>';
          //     is_once_only = true;
          //   }
          //   if (weekly_fixs[i].id) {
          //     mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Fixture id: </b>'+ weekly_fixs[i].id + ', <b>Fixture: </b>' + weekly_fixs[i].fixture + '</li>';
          //   }
          // }
          // mainHtml += '<a href="http://localhost:8000/admin_update/admin_get_weekly_tables/'+ weekly_fixs[2].week_no +'">'+ '<b>Update Player_Week_Table: </b>' + weekly_fixs[2].week_no +'</a>';
          // mainHtml += '</ul>';
          get_week.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_weekly_fixtures", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_week.innerHTML = 'Season games ...';
  },
  Get_Fixtures: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
          var weekly_fixtures = JSON.parse(http.responseText);
          console.log(weekly_fixtures);
          var mainHtml = '';
          // mainHtml += '<ul class="nav flex-column list-group">';
          // mainHtml += '</ul>';
          // mainHtml += '<div class="row">';
          // mainHtml += '<div class="col-6 col-sm-6">';
          // mainHtml += '<h4>Player Form</h4>';
          // for (i = 0; i < weekly_forms.length; i++) {
          //   mainHtml += '<p>'+ 'ID: ' +weekly_forms[i].player_id + ' - Name: ' + weekly_forms[i].player_name + ' - Points: ' + weekly_forms[i].points + ' - Total Points: ' + weekly_forms[i].total_points + ' - Week no: ' + weekly_forms[i].week_no_id_id +'</p>';
          // }
          // mainHtml += '</div>';
          // mainHtml += '<div class="col-6 col-sm-6">.col-6 .col-sm-3</div>';
          // mainHtml += '<div class="w-100"></div>';
          // mainHtml += '<div class="col-6 col-sm-6">.col-6 .col-sm-3</div>';
          // mainHtml += '<div class="col-6 col-sm-6">.col-6 .col-sm-3</div>';
          // mainHtml += '</div>';
          get_fixtures.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_fixtures", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_fixtures.innerHTML = 'Weekly Fixtures ...';
  },
}
window.onload = function() {
  main = new CreateANewRequest();
  if (document.getElementById('get_week')) {
    main.Get_Week();
  }
  if (document.getElementById('get_fixtures')) {
    main.Get_Fixtures();
  }
}
