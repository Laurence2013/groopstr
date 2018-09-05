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
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var goals = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Goals scored</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_get_goals/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ goals[1].week_no_id_id +'">'
        for (i = 1; i < goals.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + goals[i].player_name
          + '<br /><b>Week number: </b>' + goals[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ goals[i].player_id +'">'
          + '<input type="text" name="goals" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + goals[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_goals_table.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_goals", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_goals_table.innerHTML = 'Goals ...';
  },
  Get_Goals_Assist: function() {
    var http = new XMLHttpRequest();
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var goals_assists = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Goals Assists</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_get_goals_assist/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ goals_assists[1].week_no_id_id +'">'
        for (i = 1; i < goals_assists.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + goals_assists[i].player_name
          + '<br /><b>Week number: </b>' + goals_assists[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ goals_assists[i].player_id +'">'
          + '<input type="text" name="goals_assists" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + goals_assists[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_goals_assist_table.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_goals_assist", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_goals_assist_table.innerHTML = 'Goals Assist...';
  },
  Get_Man_Of_The_Match: function() {
    var http = new XMLHttpRequest();
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var man_of_the_match = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Man of the Match</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_man_of_the_match/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ man_of_the_match[1].week_no_id_id +'">'
        for (i = 1; i < man_of_the_match.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + man_of_the_match[i].player_name
          + '<br /><b>Week number: </b>' + man_of_the_match[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ man_of_the_match[i].player_id +'">'
          + '<input type="text" name="man_of_the_match" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + man_of_the_match[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_man_of_the_match_table.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_man_of_the_match", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_man_of_the_match_table.innerHTML = 'Man of the Match...';
  },
  Get_Own_Goals: function() {
    var http = new XMLHttpRequest();
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var own_goals = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Own Goals</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_own_goals/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ own_goals[1].week_no_id_id +'">'
        for (i = 1; i < own_goals.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + own_goals[i].player_name
          + '<br /><b>Week number: </b>' + own_goals[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ own_goals[i].player_id +'">'
          + '<input type="text" name="own_goals" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + own_goals[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_own_goals.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_own_goals", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_own_goals.innerHTML = 'Own Goals...';
  },
  Get_Yellow_Cards: function() {
    var http = new XMLHttpRequest();
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var yellow_cards = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Yellow Cards</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_yellow_cards/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ yellow_cards[1].week_no_id_id +'">'
        for (i = 1; i < yellow_cards.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + yellow_cards[i].player_name
          + '<br /><b>Week number: </b>' + yellow_cards[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ yellow_cards[i].player_id +'">'
          + '<input type="text" name="yellow_cards" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + yellow_cards[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_yellow_cards.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_yellow_cards", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_yellow_cards.innerHTML = 'Yellow Cards...';
  },
  Get_Red_Cards: function() {
    var http = new XMLHttpRequest();
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var red_cards = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Red Cards</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_red_cards/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ red_cards[1].week_no_id_id +'">'
        for (i = 1; i < red_cards.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + red_cards[i].player_name
          + '<br /><b>Week number: </b>' + red_cards[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ red_cards[i].player_id +'">'
          + '<input type="text" name="red_cards" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + red_cards[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_red_cards.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_red_cards", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_red_cards.innerHTML = 'Red Cards...';
  },
  Get_Clean_Sheets: function() {
    var http = new XMLHttpRequest();
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var clean_sheets = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Clean Sheets</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_clean_sheets/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ clean_sheets[1].week_no_id_id +'">'
        for (i = 1; i < clean_sheets.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + clean_sheets[i].player_name
          + '<br /><b>Week number: </b>' + clean_sheets[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ clean_sheets[i].player_id +'">'
          + '<input type="text" name="clean_sheets" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + clean_sheets[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_clean_sheets.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_clean_sheets", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_clean_sheets.innerHTML = 'Clean Sheets...';
  },
  Get_Form: function() {
    var http = new XMLHttpRequest();
    var csrftoken = Cookies.get('csrftoken');
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var form = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Form</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/admin_update/admin_form/" method="POST">';
        mainHtml += '<input type="hidden" name="week_no" value="'+ form[1].week_no_id_id +'">'
        for (i = 1; i < form.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + form[i].player_name
          + '<br /><b>Week number: </b>' + form[i].week_no_id_id
          + '<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
          + '<input type="hidden" name="player_id" value="'+ form[i].player_id +'">'
          + '<input type="text" name="form" value="'+ 0 +'">'
          + '<br /><b>Total points: </b>' + form[i].points +'</li>';
        }
        mainHtml += '<input type="submit" value="Submit">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        get_form.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_form", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_form.innerHTML = 'Form...';
  },
  Get_Goalkeepers: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var goalkeepers = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Goalkeepers</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        for (i = 0; i < goalkeepers.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + goalkeepers[i].player_name
          + '<br /><b>Player position: </b>' + goalkeepers[i].player_position_1
          + '<br /><b>Team: </b>' + goalkeepers[i].real_football_team
          + '<br /><b>Current valuation: </b>' + goalkeepers[i].current_player_value
          + '<br /><b>Total points: </b>' + goalkeepers[i].total_points
        }
        mainHtml += '</ul>';
        get_goalkeepers.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_goalkeepers", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_goalkeepers.innerHTML = 'Goalkeepers...';
  },
  Get_Defenders: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var defenders = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Defenders</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        for (i = 0; i < defenders.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + defenders[i].player_name
          + '<br /><b>Player position: </b>' + defenders[i].player_position_1
          + '<br /><b>Team: </b>' + defenders[i].real_football_team
          + '<br /><b>Current valuation: </b>' + defenders[i].current_player_value
          + '<br /><b>Total points: </b>' + defenders[i].total_points
        }
        mainHtml += '</ul>';
        get_defenders.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_defenders", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_defenders.innerHTML = 'Defenders...';
  },
  Get_Midfielders: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var midfielders = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Midfielders</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        for (i = 0; i < midfielders.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + midfielders[i].player_name
          + '<br /><b>Player position: </b>' + midfielders[i].player_position_1
          + '<br /><b>Team: </b>' + midfielders[i].real_football_team
          + '<br /><b>Current valuation: </b>' + midfielders[i].current_player_value
          + '<br /><b>Total points: </b>' + midfielders[i].total_points
        }
        mainHtml += '</ul>';
        get_midfielders.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_midfielders", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_midfielders.innerHTML = 'Midfielders...';
  },
  Get_Forwards: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var forwards = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Forwards</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        for (i = 0; i < forwards.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'+ '<b>Player name: </b>' + forwards[i].player_name
          + '<br /><b>Player position: </b>' + forwards[i].player_position_1
          + '<br /><b>Team: </b>' + forwards[i].real_football_team
          + '<br /><b>Current valuation: </b>' + forwards[i].current_player_value
          + '<br /><b>Total points: </b>' + forwards[i].total_points
        }
        mainHtml += '</ul>';
        get_forwards.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_get_forwards", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_forwards.innerHTML = 'Forwards...';
  },
  Get_Players_Points: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var players_points = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Get Players points from each position</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        for (i = 0; i < players_points.length; i++) {
          for (j = 0; j < players_points[i].length; j++) {
            mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'
              + '<b>Players points: </b>' + players_points[i][j].players_points
              + '<b> Player ID: </b>' + players_points[i][j].player_id_id
              + '<b> Player position: </b>' + players_points[i][j].position
              + '<b> User ID: </b>' + players_points[i][j].user_id_id + '</li>';
          }
        }
        mainHtml += '</ul>';
        get_players_points.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_sort_points_players", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_players_points.innerHTML = 'Players points...';
  },
  Get_User_Players_Total_Points: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var players_points = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml = '<h5 class="weekly_fixtures">Get User total points for all his or her players</h5>';
        mainHtml += '<ul class="nav flex-column list-group">';
        for (i = 0; i < players_points.length; i++) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item">'
            + '<b>User ID: </b>' + players_points[i].user_id
            + '<b> Team Points: </b>' + players_points[i].user_team_points + '</li>';
        }
        mainHtml += '</ul>';
        get_user_total_points.innerHTML = mainHtml;
      }
    }
    http.open("GET", "admin_calc_user_points", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_user_total_points.innerHTML = 'User Players Total Points...';
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
  if (document.getElementById('get_goals_assist_table')) {
    main.Get_Goals_Assist();
  }
  if (document.getElementById('get_man_of_the_match_table')) {
    main.Get_Man_Of_The_Match();
  }
  if (document.getElementById('get_own_goals')) {
    main.Get_Own_Goals();
  }
  if (document.getElementById('get_yellow_cards')) {
    main.Get_Yellow_Cards();
  }
  if (document.getElementById('get_red_cards')) {
    main.Get_Red_Cards();
  }
  if (document.getElementById('get_clean_sheets')) {
    main.Get_Clean_Sheets();
  }
  if (document.getElementById('get_form')) {
    main.Get_Form();
  }
  if (document.getElementById('get_goalkeepers')) {
    main.Get_Goalkeepers();
  }
  if (document.getElementById('get_defenders')) {
    main.Get_Defenders();
  }
  if (document.getElementById('get_midfielders')) {
    main.Get_Midfielders();
  }
  if (document.getElementById('get_forwards')) {
    main.Get_Forwards();
  }
  if (document.getElementById('get_players_points')) {
    main.Get_Players_Points();
  }
  if (document.getElementById('get_user_total_points')) {
    main.Get_User_Players_Total_Points();
  }
}
