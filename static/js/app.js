const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;

// chat bot
const openButton = document.querySelector('.chatbox__button');
const chatBox = document.querySelector('.chatbox__support');
const sendButton = document.querySelector('.send__button')

var state = false;

openButton.addEventListener('click', () => {
    state = !state

        //shor or hide the box
        if (state) {
            chatBox.classList.add('chatbox--active')
        } else {
            chatBox.classList.remove('chatbox--active')
        }
});

var wss_protocol = window.location.protocol == "https:" ? "wss://" : "ws://";
  var chatSocket = new WebSocket(
    wss_protocol + window.location.host + "/ws/chat/"
  );
  var messages = [];

//   chatSocket.onopen = function (e) {
//     document.querySelector("#chat-header").innerHTML =
//       "Welcome to Django Chatbot";
//   };

  chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var message = data["text"];
    messages.unshift(message);

    var str = '';
    messages.slice().forEach(function (msg) {
      if (msg.source == "user"){
        str += '<div class="messages__item messages__item--operator">' + msg.msg + '</div>'
      }
      else {
        str += '<div class="messages__item messages__item--visitor">' + msg.msg + '</div>'
      }
    });

    const chatmessage = chatBox.querySelector('.chatbox__messages');
     
    if(chatmessage){
        chatmessage.innerHTML = str;
    } else {
        console.log("Cannot do element.innerHTML. The current value of element is ",chatmessage)
    }
   
  };

  chatSocket.onclose = function (e) {
    alert("Socket closed unexpectedly, please reload the page.");
  };

  document.querySelector("#chat-message-input").focus();
  document.querySelector("#chat-message-input").onkeyup = function (e) {
    if (e.keyCode === 13) {
      // enter, return
      document.querySelector("#chat-message-submit").click();
    }
  };

  document.querySelector("#chat-message-submit").onclick = function (e) {
    var messageInputDom = document.querySelector("#chat-message-input");
    var message = messageInputDom.value;
    chatSocket.send(
      JSON.stringify({
        text: message,
      })
    );

    messageInputDom.value = "";
  };