var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    typeSpeed: 50,
    backSpeed: 20,
    backDelay: 700,
    onComplete: function(self) { self.cursor.remove() }
  });