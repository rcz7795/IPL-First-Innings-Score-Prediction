function onPageLoad() {

    $(window).load(function() {
      console.log("document loaded");

      $.get("{{ url_for('get_team1_names') }}",
        function (data, status) {
          console.log("got response for get_team1_names request");
          console.log(data)
          if(data) {
              var team1 = data.team1;
              console.log(team1)
              var uiTeam1 = document.getElementById("uiTeam1");
              $('#uiTeam1').empty();
              for(var i in team1) {
                  var opt = new Option(team1[i]);
                  $('#uiTeam1').append(opt);
              }
          }
      });

      $.get("{{ url_for('get_team2_names') }}",
        function (data, status) {
          console.log("got response for get_team2_names request");
          console.log(data)
          if(data) {
              var team2 = data.team2;
              console.log(team2)
              var uiTeam2 = document.getElementById("uiTeam2");
              $('#uiTeam2').empty();
              for(var i in team2) {
                  var opt = new Option(team2[i]);
                  $('#uiTeam2').append(opt);
              }
          }
      });

      $.get("{{ url_for('get_venue_names') }}",
        function (data, status) {
          console.log("got response for get_venue_names request");
          if(data) {
              var venue = data.venue;
              var uiVenue = document.getElementById("uiVenue");
              $('#uiVenue').empty();
              for(var i in venue) {
                  var opt = new Option(venue[i]);
                  $('#uiVenue').append(opt);
              }
          }
      });

      $.get("{{ url_for('get_overs_names') }}",
        function (data, status) {
          console.log("got response for get_overs_names request");
          if(data) {
              var overs = data.overs;
              var uiOvers = document.getElementById("uiOvers");
              $('#uiOvers').empty();
              for(var i in overs) {
                  var opt = new Option(overs[i]);
                  $('#uiOvers').append(opt);
              }
          }
      });

      $.get("{{ url_for('get_wickets_names') }}",
        function (data, status) {
          console.log("got response for get_wickets_names request");
          if(data) {
              var wickets = data.wickets;
              var uiWickets = document.getElementById("uiWickets");
              $('#uiWickets').empty();
              for(var i in wickets) {
                  var opt = new Option(wickets[i]);
                  $('#uiWickets').append(opt);
              }
          }
      });


    });
}

window.onload = onPageLoad;
