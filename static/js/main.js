window.addEventListener("scroll", function() {
  var navbar1 = document.querySelector(".topp");
  var navbar2 = document.querySelector(".topp2");

  if (window.scrollY > 0) {
    navbar1.classList.add("hidden");
    navbar2.style.marginTop = "10px";
  } else {
    navbar1.classList.remove("hidden");
    navbar2.style.marginTop = "0";
  }
});


function updateInput(rangeId, inputId, unit) {
    var range = document.getElementById(rangeId);
    var input = document.getElementById(inputId);
    input.value = range.value;
    input.dispatchEvent(new Event('input'));
  }
  
  function hesapla() {
    var aylikEmekHaqqi = parseFloat(document.getElementById("aylikEmekHaqqi").value);
    var emekHaqqiRange = parseFloat(document.getElementById("emekHaqqiRange").value);
    var mebleg = parseFloat(document.getElementById("mebleg").value);
    var meblegRange = parseFloat(document.getElementById("meblegRange").value);
    var muddet = parseInt(document.getElementById("muddet").value);
    var muddetRange = parseInt(document.getElementById("muddetRange").value);

    var aylikOdeme = (meblegRange  / muddetRange);

    if (!isNaN(aylikOdeme)) {
      document.getElementById("aylikOdeme").textContent = aylikOdeme.toFixed(2);
    } else {
      document.getElementById("aylikOdeme").textContent = "";
    }
  }
  function calculate() {
    var currency = document.getElementById("currency").value;
    var amount = parseFloat(document.getElementById("amount").value);

    // Örnek XML dosyası yerine gerçek URL'nizi kullanın
    var url = "https://www.cbar.az/currencies/13.07.2023.xml";

    // XML dosyasını almak için XMLHttpRequest kullanabilirsiniz
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var xmlResponse = xhr.responseXML;
        var rates = xmlResponse.getElementsByTagName("ValType");

        for (var i = 0; i < rates.length; i++) {
          var currencyCode = rates[i].getElementsByTagName("Valute")[0].getElementsByTagName("Code")[0].textContent;
          var buyValue = parseFloat(rates[i].getElementsByTagName("Valute")[0].getElementsByTagName("Value")[0].textContent);
          var sellValue = parseFloat(rates[i].getElementsByTagName("Valute")[0].getElementsByTagName("Value")[1].textContent);

          if (currencyCode === currency) {
            document.getElementById("buyRate").textContent = "Alış Değeri: " + buyValue.toFixed(2);
            document.getElementById("sellRate").textContent = "Satış Değeri: " + sellValue.toFixed(2);
            break;
          }
        }
      }
    };
    xhr.send(null);
  }
  const rangeInputs = document.querySelectorAll('input[type="range"]')

function handleInputChange(e) {
  let target = e.target
  const min = target.min
  const max = target.max
  const val = target.value
  target.style.backgroundSize = (val - min) * 100 / (max - min) + '% 100%'
  }
rangeInputs.forEach(input => {
  input.addEventListener('input', handleInputChange)
})


var previousPage = document.referrer; // Get the URL of the previous page

function toggleMenu() {
    var menu = document.getElementById("menu");
    var menuButton = document.getElementById("menuButton");

    if (menu.style.display === "none") {
        menu.style.display = "block";
        menuButton.innerHTML = "<i class='fa fa-times'></i>";
    } else {
        menu.style.display = "none";
        menuButton.innerHTML = "<i class='fa fa-bars'></i>";
    }
}

// Handle the back button press
window.onpopstate = function(event) {
    toggleMenu();
    if (event.state !== null && event.state.previousPage) {
        history.back(); // Go back to the previous page
    }
};

// Set the menu display based on the previous page
if (previousPage === "") {
    toggleMenu(); // Show menu if there is no previous page
}


var rates = {"bank":{"usd":{"buy":"1.6950","sell":"1.7015","cash_buy":"1.6950","cash_sell":"1.7015"},"eur":{"buy":"1.8600","sell":"1.9550","cash_buy":"1.8600","cash_sell":"1.9550"},"rub":{"buy":"0.0160","sell":"0.0220","cash_buy":"0.0160","cash_sell":"0.0220"},"gbp":{"buy":"2.1000","sell":"2.3400","cash_buy":"2.1000","cash_sell":"2.3400"}},"mb":{"usd":{"buy":"1.7000","sell":"1.7000"},"eur":{"buy":"1.9087","sell":"1.9087"},"rub":{"buy":"0.0188","sell":"0.0188"},"gbp":{"buy":"2.2254","sell":"2.2254"}}},
            calculate = function () {
                var c = $('.calculator'),
                    cash = $('.change_rates .select_content a.active').data('cash'),
                    from = c.find('select[name=from]').val(),
                    to = c.find('select[name=to]').val(),
                    curr = from === "azn" ? to : from,
                    buy = cash ? rates['bank'][curr]['cash_buy']  :  rates['bank'][curr]['buy'],
                    sell = cash ? rates['bank'][curr]['cash_sell'] : rates['bank'][curr]['sell'] ,
                    input_value = $('.input_value').val(),
                    input_result = $('.input_result'),
                    result = from === "azn"
                        ? (parseInt(input_value) / sell).toFixed(2) 
                        : (parseInt(input_value) * buy).toFixed(2) ;
    
                    console.log('Buy:'+buy);
                if(result=='NaN') result='Alıram';
    
                input_result.html(result);
            },
            table = function () {
                var cash = $('.change_rates .select_content a.active').data('cash')
                $('.cr_item_buy.table_buy_rate').map((index, item) => {
                    var item = $(item);
                    item.html(item.data((cash ? '' : 'no') + 'cash'));
                })
    
                $('.cr_item_sell.table_sell_rate').map((index, item) => {
                    var item = $(item);
                    item.html(item.data((cash ? '' : 'no') + 'cash'));
                })
            };
        $(function () {
            calculate();
            table();
        });
        $(document).on('click', '.change_rates .select_content a', function (e) {
            e.preventDefault();
            var t = $(this),
                c = t.closest('.change_rates'),
                title = t.text();
            c.find('.active_lang').html(title);
            c.find('.select_box').removeClass('open_select');
            t.parent('li').siblings().find('a').removeClass('active');
            t.addClass('active');
            calculate();
            table();
            return false;
        });
        $(document).on('change', '.s_curr', function (e) {
            var t = $(this),
                name = t.attr('name'),
                from = $('.s_curr[name=from]'),
                to = $('.s_curr[name=to]');
            if (name === "from") {
                if (t.val() === "azn") {
                    to.find('option[value!=azn]').show();
                    to.find('option[value=azn]').hide();
                    to.val(to.find('option:nth-child(2)').val());
                } else {
                    to.find('option[value=azn]').show();
                    to.find('option[value!=azn]').hide();
                    to.val(to.find('option').val());
                }
            }
            calculate();
            table();
        });
        $(document).on('keyup', '.input_value', calculate);