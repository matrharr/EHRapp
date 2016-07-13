$(document).ready(function() {
  console.log('test')
  $('form').on('submit', stopAction);
});

  var stopAction = function(e){
    e.preventDefault();
  }



