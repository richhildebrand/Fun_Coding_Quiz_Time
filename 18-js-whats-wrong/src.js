let attachListeners = function(dom) {
    var prizes = ['A Unicorn!', 'A Hug!', 'Fresh Laundry!'];
    for (var btnNum = 0; btnNum < prizes.length; btnNum++) {
        // for each of our buttons, when the user clicks it...
        dom.querySelector('#btn-' + btnNum).onclick = function() {
            // tell her what she's won!
            alert(prizes[btnNum]);
        };
    }
}

let workingAttachListeners = function(dom) {
    var prizes = ['A Unicorn!', 'A Hug!', 'Fresh Laundry!'];
    for (var btnNum = 0; btnNum < prizes.length; btnNum++) {
        // for each of our buttons, when the user clicks it...
        dom.querySelector('#btn-' + btnNum).onclick = function(frozenBtnNum){
            return function() {
                // tell her what she's won!
                alert(prizes[frozenBtnNum]);
            };
        }(btnNum);  // LOOK! We're passing btnNum to our anonymous function here!
    }
}