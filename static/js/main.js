function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Get_Week: function() {
    var http = new XMLHttpRequest();
    var week_ids_arr = []
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
          var weekly_fixs = JSON.parse(http.responseText);
          console.log(weekly_fixs);
          var mainHtml = '';
          mainHtml = '<h2 class="weekly_fixtures">Weekly Fixtures</h2>';
          mainHtml += '<ul class="nav flex-column list-group">';
          for (i = 0; i < weekly_fixs.length; i++) {
            week_ids_arr.push(weekly_fixs[i].id);
            if (weekly_fixs[i].is_current_week == false) {
              mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week: </b>'+ weekly_fixs[i].week_no + ' -- ' +
              '<b>Start date: </b>'+ weekly_fixs[i].start_date + ' -- ' + '<b>End date:</b>' + weekly_fixs[i].end_date + ' -- ' +'<b>Check this week to True:</b> '+
              '<input type="radio" id="check_w" name="check_week" value="'+ weekly_fixs[i].id +'"> </li>';
            } else {
              mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week: </b>'+ weekly_fixs[i].week_no + ' -- ' +
              '<b>Start date: </b>'+ weekly_fixs[i].start_date + ' -- ' + '<b>End date:</b>' + weekly_fixs[i].end_date + ' -- ' +'<b>This is already current week:</b> '+
              '<input type="radio" id="check_w" name="check_week" value="'+ weekly_fixs[i].id +'" disabled> </li>';
            }
          }
          mainHtml += '</ul>';
          get_week.innerHTML = mainHtml;
          console.log(week_ids_arr);
          var pass_week_ids = new CreateANewRequest();
          pass_week_ids.Get_Fixtures('hello');
      }
    }
    http.open("GET", "admin_get_weekly_fixtures", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_week.innerHTML = 'Season games ...';
  },
  Get_Fixtures: function(e) {
    console.log(e);
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
    get_fixtures.innerHTML = 'Weekly fixtures ...';
  },
}
window.onload = function() {
  main = new CreateANewRequest();
  if (document.getElementById('get_week')) {
    main.Get_Week();
  }
  if (document.getElementById('get_fixtures')) {
    main.Get_Fixtures(undefined);
  }
}
