(function() {
  var http = new XMLHttpRequest();
  http.open("GET", "get_all_stats", true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.onreadystatechange = function() {
    if (http.readyState == 4 && http.status == 200) {
      var get_all_stats = JSON.parse(http.responseText);
      console.log(get_all_stats);
      var get_week = get_all_stats.filter(function(stats){
        if (stats[0].name === 'weeks') {
          return stats[0];
        }
      });
      var mainHtml = '';
      mainHtml += '<h5><b>Check all </b>'+ get_week[0][0].name  +':</h5>';
      mainHtml += '<select id="week_no" name="week_no">';
      mainHtml += '<option>Select a week</option>';

      let get_week_stats = function(week_len, week_no, sub_week_no) {
        if (week_no === week_len) return;
        mainHtml += '<option value="'+ get_week[0][week_no][sub_week_no].id +'">Week: '+ get_week[0][week_no][sub_week_no].week_no +'</option>';
        get_week_stats(week_len, week_no + 1, sub_week_no + 1);
      }
      get_week_stats(get_week[0].length, week_no = 1, sub_week_no = 0);
      mainHtml += '</select>';
      get_all_stats_table.innerHTML = mainHtml;

      document.getElementById('week_no').onclick = function EventHandler() {
        console.log(this.value);
      }
    }
  }
  http.send();
  get_all_stats_table.innerHTML = 'All stats tables...';
})();
