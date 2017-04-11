$(function() {
  var $player = $('#player').first();
  var $progess = $('#progress p').first();
  var $transcript = $('#transcript').first();

  $.get('/download-youtube-video').done(function(data) {
    $progess.text('Procesando el video vía IBM Watson...');

    $.get('/watson-process-audio').done(function(data) {
      $progess.text('');

      $('#loading').hide();

      $player.html(generateYouTubeIframe(data.video_id));

      var paragraphs = generateTranscript(data);

      for (var i = 0; i < paragraphs.length; i++) {
        $transcript.append(paragraphs[i]);
      }
    }).fail(function() {
      $progess.text('¡Ocurrió un error al intentar procesar el video!');
    });
  }).fail(function() {
    $progess.text('¡Ocurrió un error al intentar descargar el video!');
  });
});


function generateYouTubeIframe(videoId) {
  var template = [
    '<iframe width="560" height="315" src="http://www.youtube.com/embed/',
    videoId,
    '?autoplay=true" frameborder="0">',
  ].join('');

  return $(template);
}


function generateTranscript(data) {
  var paragraphs = [];

  for (var i = 0; i < data.results.length; i++) {
    var text = data.results[i]['alternatives'][0]['transcript'];

     paragraphs = paragraphs.concat($('<p>' + text + '</p>'));
  }

  return paragraphs;
};
