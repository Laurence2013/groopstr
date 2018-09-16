function CreateANewRequest(){}
function select_player() {
  var get_player = document.getElementById('player_name').value;
  console.log(get_player);
}

CreateANewRequest.prototype = {
  All_Stats_Tabl: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var all_stats_tables = JSON.parse(http.responseText);
        var mainHtml = '';
        mainHtml += '<h5 class="weekly_fixtures">Detailed search</h5>';
        mainHtml += '<select id="player_name" name="player_name" onchange="select_player()">';
        mainHtml += '<option value="choose_name" selected>Select a players name</option>';
        for (j = 0; j < all_stats_tables[9].length; j++) {
          if (all_stats_tables[9][j].name != 'players_name') {
            mainHtml += '<option value="'+ all_stats_tables[9][j].player_id +'">'+ all_stats_tables[9][j].player_name +'</option>';
          }
        }
        mainHtml += '</select>';
        mainHtml += '<br>';
        // for (i = 0; i < all_stats_tables.length; i++){
        //   if (all_stats_tables[i][0].name != 'weeks' && all_stats_tables[i][0].name != 'players_name') {
        //     console.log(all_stats_tables[i][0]);
        //   }
        // }
        get_all_stats.innerHTML = mainHtml;
      }
    }
    http.open("GET", "get_all_stats", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    get_all_stats.innerHTML = 'All stats tables...';
  },
}
window.onload = function() {
  main = new CreateANewRequest();
  if (document.getElementById('get_all_stats')) {
    main.All_Stats_Tabl();
  }
}
