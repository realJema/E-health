// function selection(e) {
//       $(e).button("toggle").addClass("fat")
// };

// $('.options-btn').on('click').toggleClass('selected')
$(function () { $('.popover-toggle').popover('toggle'); });

let sympt = []

// toggle class for symptomes
$('.symp').click(function (e) {
  $(this).toggleClass("btn-outline-primary")
  $(this).toggleClass("btn-primary")

  sympt.push($(this).text())

  console.log('The sympt', sympt)
  $("#symptomes").val(sympt);

  // console.log('The val', $(".sympt").val())

 });

var socket = io.connect('http://' + document.domain + ':' + location.port);
let user_name = null;
let user_input = 'connected';
socket.on( 'connect', function() {
  socket.emit( 'my event', {
    data: 'User Connected'
  } )
  var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    if (user_name === null) {
      user_name = $( 'input.username' ).val()
      $( 'input.username' ).hide()
    }

    user_input = $( 'input.message' ).val()
    socket.emit( 'my event', {
      user_name : user_name,
      message : user_input
    } )
    $( 'input.message' ).val( '' ).focus()
  } )
} )
socket.on( 'my response', function( msg ) {
  console.log( msg )
  if( typeof msg.user_name !== 'undefined' ) {
    $( 'h3' ).remove()
    $( 'div.message_holder' ).append( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
  }
})