function CreateANewRequest(){}

CreateANewRequest.prototype = {
  Weekly_Fixtures: function() {
    var http = new XMLHttpRequest();
    console.log(http);
    // http.onreadystatechange = function() {
    //   if(http.readyState == 4 && http.status == 200){
    //       var cat_links = JSON.parse(http.responseText);
    //       var mainHtml = '';
    //       mainHtml = '<h2 class="category_nav">Popular Categories</h2>';
    //       mainHtml += '<ul class="nav flex-column list-group">';
    //       for (i = 0; i < cat_links.length; i++) {
    //         mainHtml += '<li id="backg-colour" class="nav-item list-group-item"><a id="link-colour" class="nav-link active" href="'+ cat_links[i].pk +'">'+ cat_links[i]['fields'].cat_list + '</a></li>';
    //       }
    //       mainHtml += '</ul>';
    //       category_links.innerHTML = mainHtml;
    //   }
    // }
    http.open("GET", "admin_get_fixtures", true);
    http.setRequestHeader('Content-type', 'application/json', true);
    http.send();
    weekly_fixtures.innerHTML = 'Weekly Fixtures ...';
  },
}
window.onload = function() {
  main = new CreateANewRequest();
  if (document.getElementById('weekly_fixtures')) {
    main.Weekly_Fixtures();
  }
}
