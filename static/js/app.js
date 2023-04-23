// Popovers
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

// Datepicker
var datepickers = [].slice.call(document.querySelectorAll('[data-datepicker]'))
var datepickersList = datepickers.map(function (el) {
    return new Datepicker(el, {
        buttonClass: 'btn'
      });
})

function showYELbox() {
  var p = document.getElementById("YEL")
  var checkBox = document.getElementById("YEL-insurance");
  if (checkBox.checked == true){
    p.style.display = "block"
  }
  else {
    p.style.display = "None"
  };
}

function displaySalary(){
  var p = document.getElementById("salary");
  var p1 = document.getElementById("alert-pay");
  
  var amount = document.getElementById("amount").value;
  var taxPercent = document.getElementById("tax-percent").value;
  var vatRate = document.getElementById('vat-rates');
  var YELcheckBox = document.getElementById("YEL-insurance");

  if (vatRate.checked == true) {
    var amountWoVAT = (amount/1.24).toFixed(2);
    var VATamount = (amount - amountWoVAT).toFixed(2);

    var invoiceVATHeader = p.querySelector('#invoice-VAT');
    invoiceVATHeader.innerHTML = 'VAT tax' + ' (24%)'
    var VAT = p.querySelector('#invoice2');
    VAT.innerHTML = '-' + VATamount + ' €';
    var afterVAT = p.querySelector('#after-VAT2');
    afterVAT.innerHTML = '<strong>'+amountWoVAT + ' €</strong>';

    var taxIncome = (amountWoVAT*taxPercent/100).toFixed(2);
    var netIncome = (amountWoVAT*(100 - taxPercent)/100).toFixed(2);
    
    var incomeTax = p.querySelector('#incomeTax2');
    incomeTax.innerHTML = '-' + taxIncome + ' €';
    var afterIncomeTax = p.querySelector('#afterIncomeTax2');
    afterIncomeTax.innerHTML = '<strong>'+ netIncome + ' €</strong>';

  }
  else {
    var VAT = p.querySelector('#invoice2');
    VAT.innerHTML =   '-0 €';
    var invoiceVATHeader = p.querySelector('#invoice-VAT');
    invoiceVATHeader.innerHTML = 'VAT tax' + ' (0%)'
    var afterVAT = p.querySelector('#after-VAT2');
    afterVAT.innerHTML = '<strong>'+ amount + ' €</strong>'; 
    var taxIncome = (amount*taxPercent/100).toFixed(2);
    var netIncome = (amount*(100 - taxPercent)/100).toFixed(2);
    var incomeTax = p.querySelector('#incomeTax2');
    incomeTax.innerHTML = '-' + taxIncome + ' €';
    var afterIncomeTax = p.querySelector('#afterIncomeTax2');
    afterIncomeTax.innerHTML = '<strong>'+ netIncome + ' €</strong>';
    }

  var YELinsHeader = document.getElementById('YEL-ins1')
  var YELinsAmount = document.getElementById('YEL-ins2')
  var receivedIncome = document.getElementById('receive')
  
  if (YELcheckBox.checked == true) {
    var age = document.getElementById('age').value;
    var dateParts = document.getElementById('YEL-input-date').value;
    var YELStartingDate = new Date(dateParts)
    const today = new Date()
    var monthDiff = (today.getFullYear() - YELStartingDate.getFullYear())*12 + (today.getMonth() - YELStartingDate.getMonth())

    
    if (age >= 18 && age <= 52 || age >62) {
      var YELpercent = 24.1

      if (monthDiff <= 48) {
        var YELdiscountPercent = (YELpercent * 0.78).toFixed(2);
        var YELdiscountAmount = (netIncome * YELdiscountPercent/100).toFixed(2) ;
        YELinsHeader.innerHTML = 'Discounted Contribution ('+ YELdiscountPercent + '%)';
        YELinsAmount.innerHTML = '-' + YELdiscountAmount + ' €';

        var receiveAmount = (netIncome - YELdiscountAmount).toFixed(2)
      }
      else {
        var YELAmount = (netIncome * YELpercent/100).toFixed(2)
        YELinsHeader.innerHTML = 'Contribution ('+ YELpercent + '%)'
        YELinsAmount.innerHTML = '-' + YELAmount + ' €';

        var receiveAmount = (netIncome - YELAmount).toFixed(2)
      } }
    else {
      var YELpercent = 25.6

      if (monthDiff <= 48) {
        var YELdiscountPercent = (YELpercent * 0.78).toFixed(2);
        var YELdiscountAmount = (netIncome * YELdiscountPercent/100).toFixed(2) ;
        YELinsHeader.innerHTML = 'Discounted Contribution ('+ YELdiscountPercent + '%)';
        YELinsAmount.innerHTML = YELdiscountAmount + ' €';
        var receiveAmount = (netIncome - YELdiscountAmount).toFixed(2)
      }
      else {
        var YELAmount = (netIncome * YELpercent/100).toFixed(2);
        YELinsHeader.innerHTML = 'Contribution ('+ YELpercent + '%)';
        YELinsAmount.innerHTML = YELAmount + ' €';
        var receiveAmount = (netIncome - YELAmount).toFixed(2)
      }
    }
  }
  else {
    YELinsHeader.innerHTML = 'Not liable (0%)';
    YELinsAmount.innerHTML = '-0 €';
    var receiveAmount = netIncome
  }
  
  var incomeTaxHeader = p.querySelector('#incomeTax1');
  incomeTaxHeader.innerHTML = 'Income tax ('+ taxPercent + '%)';

  receivedIncome.innerHTML = '<strong>'+ receiveAmount + ' € </strong>';
  p1.style.display = "block";
  p.style.display = "block";
};



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