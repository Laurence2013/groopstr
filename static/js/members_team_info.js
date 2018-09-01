function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Get_Member_Team_Info: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var csrftoken = Cookies.get('csrftoken');
        var get_players = JSON.parse(http.responseText);
        var len_array = Object.keys(get_players[1]).length;
        var mainHtml = '';
        mainHtml = '<h2 class="weekly_fixtures">All weeks in a season</h2>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Username: </b>'+ get_players[0].username +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Credits left: </b>'+ get_players[0].credits_left +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Calculate team points: </b>'+ get_players[0].calculate_team_points +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Prize money - Bought Sold: </b>'+ get_players[0].prize_money_minus_bought_sold +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Profit gained players sold: </b>'+ get_players[0].profit_gained_players_sold +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Total cost players bought: </b>'+ get_players[0].total_cost_players_bought +'</li>';
        mainHtml += '</ul>';
        mainHtml += '<h3 class="weekly_fixtures">Players</h3>';
        mainHtml += '<ul class="nav flex-column list-group">';
        mainHtml += '<form name="_csrf" action="http://localhost:8000/members/get_right_member/" method="POST">';
        mainHtml += '<input name="csrfmiddlewaretoken" value='+ csrftoken +' type="hidden">';
        if (get_players[1].player_1[6] == false) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_1[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_1[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_1[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_1[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_1[5]
          +'<br />'+'<input type="checkbox" name="player_id" value="'+get_players[1].player_1[0]+'" /> Check if you want this player to play'+'</li>';
        } else {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_1[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_1[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_1[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_1[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_1[5]
          +'<br />'+'<b>This place cannot play</b>';
        }

        mainHtml += '<br />';
        if (get_players[1].player_2[6] == false) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_2[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_2[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_2[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_2[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_2[5]
          +'<br />'+'<input type="checkbox" name="player_id" value="'+get_players[1].player_2[0]+'" /> Check if you want this player to play'+'</li>';
        } else {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_2[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_2[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_2[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_2[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_2[5]
          +'<br />'+'<b>This place cannot play</b>';
        }
        mainHtml += '<br />';
        if (get_players[1].player_3[6] == false) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_3[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_3[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_3[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_3[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_3[5]
          +'<br />'+'<input type="checkbox" name="player_id" value="'+get_players[1].player_3[0]+'" /> Check if you want this player to play'+'</li>';
        } else {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_3[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_3[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_3[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_3[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_3[5]
          +'<br />'+'<b>This place cannot play</b>';
        }
        mainHtml += '<br />';
        if (get_players[1].player_4[6] == false) {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_4[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_4[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_4[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_4[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_4[5]
          +'<br />'+'<input type="checkbox" name="player_id" value="'+get_players[1].player_4[0]+'" /> Check if you want this player to play'+'</li>';
        } else {
          mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_4[1]
          +'<br />'+'<b>Player position: </b>'+ get_players[1].player_4[2]
          +'<br />'+'<b>Player position 2: </b>'+ get_players[1].player_4[3]
          +'<br />'+'<b>Player position 3: </b>'+ get_players[1].player_4[4]
          +'<br />'+'<b>Player valuation: </b>'+ get_players[1].player_4[5]
          +'<br />'+'<b>This place cannot play</b>';
        }

        mainHtml += '<br />';
        mainHtml += '<input type="submit" value="Submit players to play">';
        mainHtml += '</form>';
        mainHtml += '</ul>';
        members_info.innerHTML = mainHtml;
      }
    }
    http.open("GET", "get_right_member", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    members_info.innerHTML = 'Member Team Info ...';
  },
}
window.onload = function() {
  main = new CreateANewRequest();
  if (document.getElementById('members_info')) {
    main.Get_Member_Team_Info();
  }
}
