/* JS File */


/*
 * Display the cards on the page
 *   - shuffle the list of cards using the provided "shuffle" method below
 *   - loop through each card and create its HTML
 *   - add each card's HTML to the page
 */

// Shuffle function from http://stackoverflow.com/a/2450976
// function shuffle(array) {
//     var currentIndex = array.length, temporaryValue, randomIndex;
//
//     while (currentIndex !== 0) {
//         randomIndex = Math.floor(Math.random() * currentIndex);
//         currentIndex -= 1;
//         temporaryValue = array[currentIndex];
//         array[currentIndex] = array[randomIndex];
//         array[randomIndex] = temporaryValue;
//     }
//
//     return array;
// }


/*
 * set up the event listener for a card. If a card is clicked:
 *  - display the card's symbol (put this functionality in another function that you call from this one)
 *  - add the card to a *list* of "open" cards (put this functionality in another function that you call from this one)
 *  - if the list already has another card, check to see if the two cards match
 *    + if the cards do match, lock the cards in the open position (put this functionality in another function that you call from this one)
 *    + if the cards do not match, remove the cards from the list and hide the card's symbol (put this functionality in another function that you call from this one)
 *    + increment the move counter and display it on the page (put this functionality in another function that you call from this one)
 *    + if all cards have matched, display a message with the final score (put this functionality in another function that you call from this one)
 */

window.onload = function() {
  flipCards();
};

var cardId = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];
var currentPair = []; var storeId = []; var clickNum = 0;

/**
 * Shows contents of card when clicked on
 * Temporarily stores clicked cards in array to find match
 * If two cards match, they stay showing and change color
 * If two cards do not match, they flip back and click reset
 */
function flipCards() {
  let doThis = cardId.map(function(i) {
    let clickMe = document.getElementById('card' + i);
    clickMe.onclick = function() {
      this.classList.toggle('show');
      this.classList.toggle('open');
      clickNum++;
      storeId.push(i);
      currentPair.push(this.className);
      // pairs();
      console.log(currentPair);
      console.log(storeId);
      if (clickNum == 2) {
        checkCards();
      }
    };
  });
};

/**
 * Compares classes of two cards to see if they match
 * If match, add match class and have cards stay flipped
 * If no match, reset array and re-flip card to back
 */
function checkCards() {
  // Cards match
  if (currentPair[0] == currentPair[1]) {
      // Add match class to cards
      document.getElementById('card' + storeId[0]).classList.add('match');
      document.getElementById('card' + storeId[1]).classList.add('match');
      console.log(this.className);
      console.log("match");
      currentPair = [];
      storeId = [];
      clickNum = 0;
    }
  // Cards don't match. Reset array, flip cards back
  else if (currentPair[0] !== currentPair[1]) {
    document.getElementById('card' + storeId[0]).classList.remove('show', 'open');
    document.getElementById('card' + storeId[1]).classList.remove('show', 'open');
    currentPair = [];
    storeId = [];
    clickNum = 0;
    console.log("no match");
  };
};


// function pairs() {
//   let getPairs = cardId.map(function(j) {
//     let showMe = document.getElementById('card' + j);
//     console.log(showMe.classList);
//   })
// }
