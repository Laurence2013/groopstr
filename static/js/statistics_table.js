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
      get_all_stats_table.innerHTML = mainHtml;

      let get_all_statss = function(){
        document.getElementById('week_no').onclick = function EventHandler() {
          console.log(this.value);
        }
        document.getElementById('stats_tables').onclick = function EventHandler() {
          console.log(this.value);
        }
      }
      get_all_statss();
    }
  }
  http.send();
  get_all_stats_table.innerHTML = 'All stats tables...';
})();
