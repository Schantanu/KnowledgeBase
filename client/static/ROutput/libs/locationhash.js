// addEventListener support for IE8
function bindEvent(element, eventName, eventHandler) {
  if (element.addEventListener) {
      element.addEventListener(eventName, eventHandler, false);
  } else if (element.attachEvent) {
      element.attachEvent('on' + eventName, eventHandler);
  }
}

// Send Message
var sendMessage = function (message) {
window.parent.postMessage(message, '*');
};

// Send a message to the Parent on hashchange event
bindEvent(window, 'hashchange', function () {
var hash = window.location.hash
var hashString = hash.replace("_", "-");
sendMessage('locHash:' + hashString);
});

// Listen to message from Parent
bindEvent(window, 'message', function (e) {
var message = e.data;
if (typeof message !== 'string') return
if (message.startsWith('parentHash:')) {
  var locationHash = message.substring(message.indexOf('#'))
  var hashstr = locationHash.replace("_", "-");
  window.location.hash = hashstr;
}
});
