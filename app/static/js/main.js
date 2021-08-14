$(document).ready(function () {
  // initialize form to get autocomplete from google
  function initialize() {
    var origin = document.getElementById("origin");
    var destination = document.getElementById("destination");
    new google.maps.places.Autocomplete(origin);
    new google.maps.places.Autocomplete(destination);
  }

  google.maps.event.addDomListener(window, "load", initialize);

  $("#getDistance").on("keypress", function (event) {
    const keyPressed = event.keyCode || event.which;
    if (keyPressed === 13) {
      event.preventDefault();
      return false;
    }
  });

  // handling submit form using this to call http request
  $("#getDistance").submit(function (event) {
    event.preventDefault();
    $("#destination").css("border", "1px solid #CED4DA");
    $("#error").text("");
    $("#errorResult").text("");
    var origin = $("#origin").val();
    var destination = $("#destination").val();
    var url = `${window.location.origin}/get-distance`;

    // return error if the destinationo is empty
    if (destination === "") {
      $("#destination").css("border", "1px solid red");
      $("#error").text("* destination could not be empty!");
      return;
    }

    $("#result").text("Calculating...");
    $.post(url, { origin: origin, destination: destination })
      .done(function (data) {
        $("#result").text(
          `Distance: ${data?.distance != null ? data?.distance : "..."} KM`
        );
      })
      .fail(function (data) {
        $("#result").text("");
        var resp = data.responseJSON;
        if (resp.includes("HTTPSConnectionPool")) {
          $("#errorResult").text(
            `Something went wrong! Please try another address`
          );
          return;
        }
        $("#errorResult").text(`${data.responseJSON}`);
      });

    return;
  });
});
