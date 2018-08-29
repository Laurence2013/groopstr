function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Get_Member_Team_Info: function() {
    var http = new XMLHttpRequest();
    http.onreadystatechange = function() {
      if (http.readyState == 4 && http.status == 200) {
        var get_players = JSON.parse(http.responseText);
        console.log(get_players);
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
