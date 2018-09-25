(function() {
  let http = new XMLHttpRequest();
  http.open("GET", "get_all_stats", true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.onreadystatechange = function() {
    if (http.readyState == 4 && http.status == 200) {
      let get_all_stats = JSON.parse(http.responseText);
      let get_week = get_all_stats.filter(function(week){
        if (week[0].name === 'weeks') {
          return week;
        }
      });
      let get_stats_names = get_all_stats.filter(function(stats){
        if (stats[0].name != 'weeks' && stats[0].name != 'players_name') {
          return stats;
        }
      });
      let mainHtml = '';
      mainHtml += '<h5><b>Check all </b>'+ get_week[0][0].name  +':</h5>';
      mainHtml += '<select id="week_no" name="week_no">';
      let get_week_stats = function(week_len, week_no, sub_week_no) {
        if (week_no === week_len) return;
        mainHtml += '<option value="'+ get_week[0][week_no][sub_week_no].id +'">Week: '+ get_week[0][week_no][sub_week_no].week_no +'</option>';
        get_week_stats(week_len, week_no + 1, sub_week_no + 1);
      }
      get_week_stats(get_week[0].length, week_no = 1, sub_week_no = 0);
      mainHtml += '</select>';

      mainHtml += '<h5>Check which table you want to select:</h5>';
      mainHtml += '<select id="stats_tables" name="stats_tables">';
      let get_stats_table = function(stats_len, index) {
        if (index === stats_len) return;
        mainHtml += '<option value="'+ get_stats_names[index][0].name +'">Table: '+ get_stats_names[index][0].name +'</option>';
        get_stats_table(stats_len, index + 1);
      }
      get_stats_table(get_stats_names.length, index = 0);
      mainHtml += '</select>';
      mainHtml += '<br />';
      mainHtml += '<input type="button" id="get_statss" value="Get values" />'
      get_all_stats_table.innerHTML = mainHtml;

      function get_statistics() {
        let mainHtml1 = ''
        let get_week = document.getElementById('week_no');
        let get_stats = document.getElementById('stats_tables');
        let get_value = get_week[get_week.selectedIndex].value
        let get_stats_name = get_stats[get_stats.selectedIndex].value

        let get_correct_stats = function(index, stats_len){
          if (index === stats_len) return;
          try {
            if (get_all_stats[index][0].name === get_stats_name){
              mainHtml1 += '<h5 class="weekly_fixtures">'+ get_all_stats[index][0].name +'</h5>';
              mainHtml1 += '<ul class="nav flex-column list-group">';
              let get_stats_details = function(stats_index, table_num, stats_len) {
                if (stats_index === stats_len) return;
                if (get_all_stats[index][stats_index].table.week_no_id_id === parseInt(get_value)) {
                  console.log(get_all_stats[index][stats_index].table);
                  let player_name = function(p_id){
                    let get_player = function(player_len, index){
                      if (index === player_len) return;
                      console.log(index);
                      get_player(player_len, index + 1);
                    }
                    get_player(get_all_stats.length, index = 0);
                  }
                  player_name(get_all_stats[index][stats_index].table.player_id);
                  // mainHtml1 += '<li id="backg-colour" class="nav-item list-group-item"><b>ID: </b>'+ get_all_stats[index][stats_index].table.id
                  // + '<br /><b>Player ID: </b>'+ get_all_stats[index][stats_index].table.player_id +'</li>';
                }
                get_stats_details(stats_index + 1, table_num + 1, stats_len);
              }
              get_stats_details(stats_index = 1, table_num = 0, get_all_stats[index].length);
            }
          } catch (e) {
            console.log(e);
          }
          get_correct_stats(index + 1, stats_len);
        }
        get_correct_stats(index = 0, get_all_stats.length);
        mainHtml1 += '</ul>';
        get_all_stats_info.innerHTML = mainHtml1;
      }
      document.getElementById('get_statss').addEventListener('click', get_statistics);
    }
  }
  http.send();
  get_all_stats_table.innerHTML = 'All stats tables...';
})();
