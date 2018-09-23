(function() {
  var http = new XMLHttpRequest();
  http.open("GET", "get_all_stats", true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.onreadystatechange = function() {
    if (http.readyState == 4 && http.status == 200) {
      var get_all_stats = JSON.parse(http.responseText);
      var get_name = get_all_stats.filter(function(stats){
        if (stats[0].name === 'weeks') {
          return stats[0].name;
        }
      });
      console.log(get_name);
    }
  }
  http.send();
  get_all_stats.innerHTML = 'All stats tables...';
})();
