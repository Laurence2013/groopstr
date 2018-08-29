function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Get_Member_Team_Info: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var get_players = JSON.parse(http.responseText);
        console.log(get_players);
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
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_1[1] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position: </b>'+ get_players[1].player_1[2] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 2: </b>'+ get_players[1].player_1[3] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 3: </b>'+ get_players[1].player_1[4] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player valuation: </b>'+ get_players[1].player_1[5] +'</li>';
        mainHtml += '<br />';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_2[1] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position: </b>'+ get_players[1].player_2[2] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 2: </b>'+ get_players[1].player_2[3] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 3: </b>'+ get_players[1].player_2[4] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player valuation: </b>'+ get_players[1].player_2[5] +'</li>';
        mainHtml += '<br />';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_3[1] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position: </b>'+ get_players[1].player_3[2] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 2: </b>'+ get_players[1].player_3[3] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 3: </b>'+ get_players[1].player_3[4] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player valuation: </b>'+ get_players[1].player_3[5] +'</li>';
        mainHtml += '<br />';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player name: </b>'+ get_players[1].player_4[1] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position: </b>'+ get_players[1].player_4[2] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 2: </b>'+ get_players[1].player_4[3] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player position 3: </b>'+ get_players[1].player_4[4] +'</li>';
        mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><b>Player valuation: </b>'+ get_players[1].player_4[5] +'</li>';
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
