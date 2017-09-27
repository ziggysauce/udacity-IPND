/* JS File */


/*
 * Display the cards on the page
 *   - shuffle the list of cards using the provided "shuffle" method below
 *   - loop through each card and create its HTML
 *   - add each card's HTML to the page
 */



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
  shuffle(array);
  dealCards();
  flipCards();
};

var array = ['fa-facebook', 'fa-google-plus', 'fa-instagram', 'fa-pinterest', 'fa-tumblr', 'fa-reddit-alien', 'fa-snapchat-ghost', 'fa-twitter', 'fa-facebook', 'fa-google-plus', 'fa-instagram', 'fa-pinterest', 'fa-tumblr', 'fa-reddit-alien', 'fa-snapchat-ghost', 'fa-twitter'];
var cardId = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];
var currentPair = []; var storeId = [];
var clickNum = 0; var totalClick = 0;


// Shuffles cards and stores values in array
function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
};

/**
 * Creates an unordered list (deck)
 * Creates list items within the unordered last (cards)
 * Shows an arrangement of the cards face down
 * Cards are randomized based on shuffle function
 */
function dealCards() {
  let incnum = 1;
  let getDeck = document.getElementById('cont');
  let makeDeck = document.createElement('ul');
  makeDeck.className = 'deck';
  getDeck.appendChild(makeDeck);

  array.map(function(j) {
    let createCard = document.createElement('li');
    createCard.className = 'card ';
    createCard.setAttribute('id', 'card'+incnum);
    let createIcon = document.createElement('i');
    createIcon.className = 'fa ' + j;
    incnum++;
    createCard.appendChild(createIcon);
    makeDeck.appendChild(createCard);
  })
};



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
      totalClick++;
      storeId.push(i);
      currentPair.push(this.children[0].className);
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
    document.getElementById('card' + storeId[0]).classList.add('correct');
    document.getElementById('card' + storeId[1]).classList.add('correct');
    setTimeout(function() {
        correct();
        currentPair = [];
        storeId = [];
        clickNum = 0;
    }, 500)
  }
  // Cards don't match. Reset array, flip cards back
  else if (currentPair[0] !== currentPair[1]) {
    document.getElementById('card' + storeId[0]).classList.add('incorrect');
    document.getElementById('card' + storeId[1]).classList.add('incorrect');
    setTimeout(function() {
      incorrect();
      currentPair = [];
      storeId = [];
      clickNum = 0;
    }, 1000)
  };
};

// Correct cards stay visible
function correct() {
  document.getElementById('card' + storeId[0]).classList.add('match');
  document.getElementById('card' + storeId[1]).classList.add('match');
};

// Incorrect cards reset
function incorrect() {
  document.getElementById('card' + storeId[0]).classList.remove('show', 'open', 'incorrect');
  document.getElementById('card' + storeId[1]).classList.remove('show', 'open', 'incorrect');
};
