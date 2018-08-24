function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Get_Week: function() {
    var http = new XMLHttpRequest();
    var week_ids_arr = []
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var csrftoken = Cookies.get('csrftoken');
        var weekly_fixs = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h2 class="weekly_fixtures">All weeks in a season</h2>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_get_current_week/" method="POST">';
        for (i = 0; i < weekly_fixs.length; i++) {
          week_ids_arr.push(weekly_fixs[i].week_no);
          if (weekly_fixs[i].is_current_week == false) {
            mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week: </b>'+ weekly_fixs[i].week_no + ' -- ' +
            '<b>Start date: </b>'+ weekly_fixs[i].start_date + ' -- ' + '<b>End date:</b>' + weekly_fixs[i].end_date + ' -- ' +'<b>Check this week to True:</b> '+
            '<input type="radio" id="check_w" name="which_check_week" value="'+ weekly_fixs[i].id +'"> </li>';
            mainHtml += '<input name="csrfmiddlewaretoken" value='+ csrftoken +' type="hidden">'
          } else {
            mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Week: </b>'+ weekly_fixs[i].week_no + ' -- ' +
            '<b>Start date: </b>'+ weekly_fixs[i].start_date + ' -- ' + '<b>End date:</b>' + weekly_fixs[i].end_date + ' -- ' +'<b>This is already current week:</b> '+
            '<input type="radio" id="check_w" name="which_check_week" value="'+ weekly_fixs[i].id +'" disabled> </li>';
            mainHtml += '<input name="csrfmiddlewaretoken" value='+ csrftoken +' type="hidden">'
          }
        }
        mainHtml += '<input type="submit" value="Submit the new current week">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_week.innerHTML = mainHtml;
        var pass_week_ids = new CreateANewRequest();
        pass_week_ids.Get_Fixtures(week_ids_arr);
      }
    }
    http.open("GET", "admin_get_weekly_fixtures", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_week.innerHTML = 'Season games ...';
  },
  Get_Fixtures: function(e) {
    if (e != undefined) {
      var http = new XMLHttpRequest();
      http.onreadystatechange = function() {
        if (http.readyState == 4 && http.status == 200) {
            var weekly_fixtures = JSON.parse(http.responseText);
            var mainHtml = '';
            mainHtml = '<h2 class="weekly_fixtures">Fixtures in each week</h2>';
            mainHtml += '<ul class="nav flex-column list-group">';
            for (i = 0; i < e.length; i++) {
              mainHtml += '<h4>'+' <b>Week: </b> '+e[i] +'</h4>';
              for (j = 0; j < weekly_fixtures.length; j++) {
                if (e[i] == weekly_fixtures[j].week_no) {
                  mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'
                  +' <b>Fixture: </b> '+ weekly_fixtures[j].fixture +' -- <b>Date of game: </b> '+ weekly_fixtures[j].date_of_game +' -- <b>Competition: </b> '+ weekly_fixtures[j].competition +
                  '</li>';
                }
              }
            }
            mainHtml += '</ul>';
            get_fixtures.innerHTML = mainHtml;
        }
      }
      http.open("GET", "admin_get_fixtures", true);
      http.setRequestHeader('Content-type', 'application/json', true);
      http.send();
      get_fixtures.innerHTML = 'Weekly fixtures ...';
    }
  },
  Get_Goals: function() {
    var http = new XMLHttpRequest();
    console.log(http);
    http.open("GET", "admin_get_current_week", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_goals_table.innerHTML = 'Goals ...';
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
  if (document.getElementById('get_goals_table')) {
    main.Get_Goals();
  }
}
